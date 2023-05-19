from django import forms
from .models import Topic,Category
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
        
class CategoryForm(forms.ModelForm):
    name= forms.ModelChoiceField(label="Category name", queryset=Category.objects.all())
    class Meta:
        model=Category
        fields=['name']
        
class AddCategory(forms.ModelForm):
    name = forms.CharField(max_length=100, label="Category name" ,widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "ADD A CATEGORY",
    }))
    
    class Meta:
        model=Category
        fields = ['name']
        

          
        
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
        