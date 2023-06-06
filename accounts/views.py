from django.shortcuts import render, redirect
from .forms import LoginForm
from django.views import View
from django.contrib.auth import authenticate, login, logout


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
