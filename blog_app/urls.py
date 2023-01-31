from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
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
    path("password-change/", PasswordChangeView.as_view(), name="password-change"),
    path("password-change/done/", PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("new-post", views.CreatePostView.as_view(), name="new_post"),
    path("update-post/<slug:slug>", views.update_post, name="update-post"),
    path("delete-post<slug:slug>", views.delete_post, name="delete-post"),
]