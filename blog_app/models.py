from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=25)
    rating = models.FloatField(max_length=20, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    # image_name = models.TextField(max_length=300)
    image = models.ImageField(upload_to="posts")
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="posts")

    def __str__(self):
        return f"{self.title}"


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"user_id: {self.user} post_id: {self.post}"


class Comments(models.Model):
    comment = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    comments_username = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.comment}"

