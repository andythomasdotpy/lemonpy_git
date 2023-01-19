from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all-posts", views.all_posts, name="all-posts"),
    path("all-posts/<slug:slug>", views.post_detail, name="post-detail"),
]