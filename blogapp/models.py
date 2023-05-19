from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=140, default='UNCATEGORIZED')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='categories'
        ordering= ['id']
    
    
class Topic(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    blog_header_image = models.ImageField(blank=True, null=True, upload_to="images/", default='default.jpg' )
    blog_title = models.CharField(max_length=500)
    blog_summary = models.CharField(max_length=1000,null=True)
    # blog_content = models.TextField(null=True,blank=True)
    blog_content = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category , on_delete=models.CASCADE)
    blog_slug= AutoSlugField(populate_from='blog_title',unique=True,null=True,default=None)
    
    def __str__(self):
        return self.blog_title   
        return self.user
         

    class Meta:
        ordering = ['updated_date']
# Create your models here.


    