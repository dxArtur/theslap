from django.urls import path

from app.views import login, register, home, post, hometest

app_name = "app"

urlpatterns = [
<<<<<<< HEAD
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
=======
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('home/', home, name="home"),
>>>>>>> develop
    path('post/', post, name="post"),
    path('hometest/', hometest, name="hometest")
]
