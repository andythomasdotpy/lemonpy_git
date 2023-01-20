from django.shortcuts import render

from .models import Post

# Create your views here.

def index(request):
    recent_posts = Post.objects.all().order_by("-date")[:3]
    content = {"recent_posts": recent_posts}

    return render(request, "blog_app/index.html", content)


def all_posts(request):
    recent_posts = Post.objects.all().order_by("-date")
    content = {"recent_posts": recent_posts}

    return render(request, "blog_app/all_posts.html", content)


def post_detail(request, slug):
    selected_post = Post.objects.get(slug=slug)
    content = {"post": selected_post}

    return render(request, "blog_app/single_post.html", content)