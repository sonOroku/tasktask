from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateTaskForm
from .models import Task


# Create your views here.
@login_required
def create_task_view(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = CreateTaskForm()
        context = {"form": form}
        return render(request, "tasks/create_task.html", context)


@login_required
def my_tasks_view(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {"tasks": tasks}
    return render(request, "tasks/my_tasks.html", context)
