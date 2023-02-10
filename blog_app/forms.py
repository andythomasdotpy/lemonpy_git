from django import forms
from django.contrib.auth.models import User

from .models import Post, Comments


class UserRegistrationForm(forms.ModelForm):
    password_1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Password', widget=forms.PasswordInput)


    class Meta: 
        model = User
        fields = ('username', 'email')

    def check_passwords(self):
        cd = self.cleaned_data
        if cd["password_1"] != cd["password"]:
            raise forms.ValidationError('Your passwords do not match.')
        return cd["password_2"]


class MakePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "rating", "image", "content")


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "rating", "image", "content")


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = {"comment"}
        labels = {
            "comment": ""
        }
