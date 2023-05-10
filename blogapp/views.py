from django.shortcuts import render,redirect
from.models import Topic
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate


# class blogList(ListView):
#     model = Topic    
#     context_object_name= 'blogs'
#     template_name = 'topic_list.html'
    
#     def get_queryset(self):
#         return Topic.objects.values_list('blog_title', flat=True)
# @login_required
def blogList(request ):
    topics = Topic.objects.all()
    context = {
        'topics': topics,
    }
    return render(request, 'topic_list.html', context)



# @login_required
def blogDetail(request,id):
    topics = Topic.objects.all()
    context = {
        'topics': topics,
    }
    return render(request, 'topic_detail.html', context)
    

class userLoginView(LoginView):
      template_name= 'login.html'
      fields = "__all__"
      
   
    

