from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.urls import reverse

from .forms import LoginForm


# Create your views here.
def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                username=request.POST["username"],
                password=request.POST["password"]
            )

            if user is not None:
                return redirect(reverse("app:home"))

    return render(request, 'login.html', context={"form": form})


def register(request):
    return render(request, 'register.html')


def home(request):
    return render(request, 'home.html')


def hometest(request):
    return render(request, 'hometest.html')


def post(request):
    return render(request, 'post.html')