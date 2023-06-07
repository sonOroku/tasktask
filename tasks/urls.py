from django.urls import path
from .views import create_task_view, my_tasks_view


urlpatterns = [
    path("create/", create_task_view, name="create_task"),
    path("mine/", my_tasks_view, name="show_my_tasks"),
]
