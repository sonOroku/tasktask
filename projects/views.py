from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import CreateProjectForm


# Create your views here.


class ProjectList(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = "projects"
    template_name = "projects/project_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


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
