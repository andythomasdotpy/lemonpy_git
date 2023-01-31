from django.contrib.auth.mixins import LoginRequiredMixin
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


# LoginRequiredMixin will require login to access view
class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = "account/new_post.html"
    model = Post
    fields = ["title", "rating", "image", "content"]
    success_url = "/all-posts"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
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


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()

    return render(request, "blog_app/deleted_confirmation.html")



