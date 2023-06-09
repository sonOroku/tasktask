from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import CreateProjectForm


# Create your views here.
@login_required
def project_list_view(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"projects": projects}
    return render(request, "projects/project_list.html", context)


@login_required
def project_detail_view(request, id):
    project = get_object_or_404(Project, id=id)
    context = {"project": project}
    return render(request, "projects/project_detail.html", context)


@login_required
def create_project_view(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = CreateProjectForm()
        context = {"form": form}
        return render(request, "projects/create_project.html", context)
