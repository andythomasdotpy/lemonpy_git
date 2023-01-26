from django.shortcuts import render
from .forms import UserRegistrationForm

from .models import Post

# Create your views here.

def index(request):
    recent_posts = Post.objects.all().order_by("-date")[:3]
    content = {"recent_posts": recent_posts}

    return render(request, "blog_app/index.html", content)


def all_posts(request):
    recent_posts = Post.objects.all().order_by("-date")
    content = {"recent_posts": recent_posts}

    return render(request, "blog_app/all_posts_new.html", content)


def post_detail(request, slug):
    selected_post = Post.objects.get(slug=slug)
    content = {"post": selected_post}

    return render(request, "blog_app/single_post.html", content)


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():

            # Create new user object but don't save yet. Check passwords.
            new_user = user_form.save(commit=False)

            # Set password
            new_user.set_password(user_form.cleaned_data["password_1"])
            new_user.save()
            content = {"user_form": user_form}

            return render(request, "account/register_done.html", content)

    else:
        user_form = UserRegistrationForm()
        {"user_form": user_form}

    return render(request, "account/register.html", {"user_form": user_form})

