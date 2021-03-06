from django.urls import path

from app.views import (
    login_view, register_view, home_view, new_post_view, hometest_view,
    post_view, about_view, dev_view, contact_view, contact_result_view
)


app_name = "app"

urlpatterns = [
    path('', home_view, name="home"),
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('new_post/', new_post_view, name="new_post"),
    path('hometest/', hometest_view, name="hometest"),
    path('post/<int:post_id>/', post_view, name="post"),
    path('about/', about_view, name="about"),
    path('dev/', dev_view, name="dev"),
    path('contact/', contact_view, name="contact"),
    path('contact_result', contact_result_view, name="contact_result")
]
