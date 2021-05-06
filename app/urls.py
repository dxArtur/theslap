from django.urls import path

from app.views import login, register, home, post, hometest

app_name = "app"

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('home/', home, name="home"),
    path('post/', post, name="post"),
    path('hometest/', hometest, name="hometest")
]
