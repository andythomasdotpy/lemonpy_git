from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all-posts", views.all_posts, name="all-posts"),
    path("single_post/<slug:slug>", views.post_detail, name="single-post"),
    path("register", views.register, name="register"),
    path("login", LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name='logout'),
]