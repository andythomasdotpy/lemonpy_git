from django.contrib import admin
from .models import Author, Post, User


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ["author", "rating", "date"]
    list_display = ["title", "date", "author", "rating"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(User)