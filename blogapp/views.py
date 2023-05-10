from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from .models import Topic
from django.forms import ModelForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import AddForm,UpdateForm
from django.urls import reverse_lazy

# class blogList(ListView):
#     model = Topic    
#     context_object_name= 'blogs'
#     template_name = 'topic_list.html'
    
#     def get_queryset(self):
#         return Topic.objects.values_list('blog_title', flat=True)
@login_required
def blogCreate(request):
    form = AddForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid(): 
            form = form.save(commit=False)
            form.user = request.user
            form.save()           
            return redirect ('/')
    context = {
        "form":form
    }
    return render(request, 'add_blog.html', context)

# class updateBlog(UpdateView):
#     model = Topic
#     template_name= 'topic_form.html'
#     fields = ['blog_title','blog_summary','blog_content']
#     success_url = reverse_lazy('/')

    
    

def blogList(request ):
    topics = Topic.objects.all()
    context = {
        'topics': topics,
    }
    return render(request, 'topic_list.html', context)

@login_required
def updateBlog(request,id):
    topics =Topic.objects.all()
    context={}
    obj =get_object_or_404( Topic, id=id)
    form = UpdateForm(request.POST or None, instance = obj)
    context['form']=form
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/detail/'+str(id))

    return render(request,'update_blog.html', context)
    
def blogDetail(request,id):
    context={}
    context["blog"]= Topic.objects.get(id = id)
    return render(request, 'topic_detail.html', context)

@login_required
def userProfile(request,id):
    context={}
    context["blog"] = Topic.objects.get(id=id)
    return render(request, 'profile.html', context)
    

class userLoginView(LoginView):
      template_name= 'login.html'
      fields = "__all__"
      
   
    

