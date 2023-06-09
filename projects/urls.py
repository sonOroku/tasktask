from django.urls import path
from .views import project_list_view, project_detail_view, create_project_view


urlpatterns = [
    path("", project_list_view, name="list_projects"),
    path("<int:id>/", project_detail_view, name="show_project"),
    path("create/", create_project_view, name="create_project"),
]
