from django.shortcuts import render
from .models import Project
from django.views.generic import ListView

# Create your views here.


class ProjectList(ListView):
    model = Project
    context_object_name = "projects"
    template_name = "projects/project_list.html"
