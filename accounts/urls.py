from django.urls import path
from .views import LoginView, logout_view, signup_view


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
]
