from django import forms
from .models import Topic


class AddForm(forms.ModelForm):
    blog_title = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "title"
    }))
    blog_summary = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "summary"
    }))
    blog_content = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "description"
    }))
    class Meta:
        model = Topic
        fields = [
            'blog_title', 'blog_summary','blog_content'
        ]
        
        
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            'blog_title', 'blog_summary','blog_content'
        ]

