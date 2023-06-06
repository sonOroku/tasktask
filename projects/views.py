from django.shortcuts import render
from .models import Project
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ProjectList(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = "projects"
    template_name = "projects/project_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset
