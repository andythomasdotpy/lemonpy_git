from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic.edit import CreateView

from .forms import UserRegistrationForm, MakePostForm
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


# @login_required
# def post_form(request):
#     post_form = MakePostForm(request.POST) 

#     if request.method == "POST":
#         if post_form.is_valid():
#             post = post_form.save(commit=False)
#             post.author = request.user
#             post = post_form.save()
#             return redirect("all-posts")

        
#     else: 
#         post_form = MakePostForm()
    
#     return render(request, "account/new_post.html", {"post_form": post_form})


class CreatePostView(CreateView):
    template_name = "account/new_post.html"
    model = Post
    fields = ["title", "rating", "image", "content", "author"]
    success_url = "/all-posts"


def update_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    print(request.POST)
    
    update_form = MakePostForm(request.POST or None, instance=post)

    if update_form.is_valid():
        update_form.save()
        return redirect("all-posts")

    print(post)
    context = {"update_form": update_form}
    return render(request, "account/update.html", context)


def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()

    return render(request, "blog_app/deleted_confirmation.html")



