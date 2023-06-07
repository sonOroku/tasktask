from django.urls import path
from .views import ProjectList, project_detail_view


urlpatterns = [
    path("", ProjectList.as_view(), name="list_projects"),
    path("<int:id>/", project_detail_view, name="show_project"),
]
