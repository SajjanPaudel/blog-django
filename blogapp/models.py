from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=500)
    blog_summary = models.CharField(max_length=1000,null=True)
    blog_content = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.blog_title
    
# Create your models here.
