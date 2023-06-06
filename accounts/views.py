from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(request, "accounts/login.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("list_projects")
        context = {"form": form}
        return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("login")


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]

            if password == password_confirmation:
                user = User.objects.create_user(
                    username=username, password=password
                )
                if user is not None:
                    login(request, user)
                    return redirect("list_projects")
            else:
                form.add_error("The passwords do not match.")
                context = {"form": form}
                return render(request, "registration/signup.html", context)

    else:
        form = SignUpForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
