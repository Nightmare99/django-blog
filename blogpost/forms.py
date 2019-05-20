from django import forms
from django.utils import timezone
from .models import post

class NewBlogPostForm(forms.ModelForm):
    class meta:
        model = post
        fields = ["heading", "upload_date", "content"]

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)

