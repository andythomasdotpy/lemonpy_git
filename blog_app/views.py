from django.shortcuts import render

from .models import Post

# Create your views here.

def index(request):
    recent_posts = Post.objects.all().order_by("-date")[:3]
    # print(recent_posts)

    for post in recent_posts:
        print(post.title)
        print(post.author)

    content = {"recent_posts": recent_posts}

    return render(request, "blog_app/index.html", content)


def all_posts(request):
    recent_posts = Post.objects.all().order_by("-date")
    # print(recent_posts)

    for post in recent_posts:
        print(post.title)
        print(post.author)

    content = {"recent_posts": recent_posts}

    return render(request, "blog_app/all_posts.html", content)


def post_detail(request, slug):
    return render(request, "blog_app/post-detail.html")