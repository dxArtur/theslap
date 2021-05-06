from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.urls import reverse

from .forms import LoginForm


# Create your views here.
def login_view(request):
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


def register_view(request):
    return render(request, 'register.html')


def home_view(request):
    return render(request, 'home.html')


def hometest_view(request):
    return render(request, 'hometest.html')


def new_post_view(request):
    return render(request, 'post.html')


def post_view(request, post_id):
    posts = {
        1: {
            "user": "Arthur",
            "content": "to deixando de assistir one piece p fazer seu "
                       "trabalho me da 10 pfvr ;-;",
            "img": "profiledaniel.jpeg"
        },
        2: {
            "user": "BolsonaroEGirl",
            "content": "gente só eu que acho lula muito bonito? s2",
            "img": "bolsonaroegrilo.jpg"
        }
    }

    post = posts[post_id]

    return render(request, template_name="see_post.html", context={"post": post})


def about_view(request):
    return render(request, template_name="about.html")


def dev_view(request):
    return render(request, template_name="dev.html")


def contact_view(request):
    return render(request, template_name="contact.html")


def contact_result_view(request):
    return render(
        request,
        template_name="contact_result.html",
        context={"form": request.POST}
    )
