from django import forms
from .models import Topic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class AddForm(forms.ModelForm):
    blog_header_image = forms.ImageField(required=False)
    blog_title = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "title"
    }))
    blog_summary = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "summary"
    }))
    blog_content = RichTextField()
    
    class Meta:
        model = Topic
        fields = [
            'blog_header_image','blog_title', 'blog_summary','blog_content'
        ]
        
        
class UpdateForm(forms.ModelForm):
    blog_header_image = forms.ImageField(required=False)
    blog_title = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "title"
    }))
    blog_summary = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "summary"
    }))
    blog_content = RichTextField()
    class Meta:
        model = Topic
        fields = [
            'blog_header_image','blog_title', 'blog_summary','blog_content'
        ]


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        