from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from .models import Topic
from functools import wraps
from django import forms
from django.contrib.auth.views import LoginView
from .forms import RegisterForm,UpdateForm,passwordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import AddForm,UpdateForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.urls import reverse_lazy
# from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden,HttpResponse
from django.core.paginator import Paginator
 

def is_author(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        blog_id = kwargs.get('id')
        blog = get_object_or_404(Topic, id=blog_id)
        #check if the author and the user who is requesting a function is same or not
        if request.user != blog.user:
        #if not then give an access forbidden error 
            return HttpResponseForbidden()
        return view_func(request, *args, **kwargs)

    return wrapper


@login_required
def blogCreate(request):
    form =AddForm()
    if request.method == "POST":
        form = AddForm(request.POST,request.FILES)
        if form.is_valid(): 
                form = form.save(commit=False)
                form.user = request.user
                form.save()           
                return redirect ('/')       
    return render(request, 'add_blog.html',{'form':form})
    
def blogList(request):
    topics = Topic.objects.all().order_by('-created_date')
    paginator= Paginator(topics,5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'topics': topics,
        'page_obj': page_obj
    }
    return render(request, 'topic_list.html', context)


@login_required
@is_author
def updateBlog(request,id):
    context={}
    blog= Topic.objects.get(id=id)
    # obj =get_object_or_404( Topic, id=id)
    form=UpdateForm()
    form = UpdateForm(request.POST or None,request.FILES or None, instance = blog)
    if request.method =='POST':
       
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/detail/'+ str(id) )
    context={
        'form': form,
        'blog': blog       
        }
    
    return render(request,'update_blog.html', context)

    
def blogDetail(request,id):
    context={}
    context["blog"]= Topic.objects.get(id = id)
    return render(request, 'topic_detail.html', context)

@login_required
def userProfile(request,id):
    num_post = Topic.objects.filter(user=request.user).count()
    topics =Topic.objects.all()
    context = {
        'topics': topics,
        'num_post':num_post
    }
    # context["blog"] = Topic.objects.get(id=id)
    return render(request, 'profile.html', context)
    

class userLoginView(LoginView):
    template_name= 'login.html'
    fields = "__all__"
    redirect_authenticated_user=True
    
    def get_success_url(self):
        return reverse_lazy('tasks')

def changePass(request):
    form = passwordChangeForm
    if request.method == 'POST':
        form= passwordChangeForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('tasks')    
    return render(request, 'update_password.html',{'form':form})
        
def userRegister(request):
    form=RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('tasks')
    return render(request, 'register.html', {'form':form})
  
@login_required
@is_author
def deleteBlog(request, id):
    # fetch the object related to passed id
    obj = get_object_or_404(Topic, id = id)
    obj.delete()
    return HttpResponseRedirect("/")
    
    
def error_404(request,exception):
    return render(request,'404.html')


def searchView(request):
    query = request.GET['query']
    topics = Topic.objects.filter(blog_title__icontains= query).order_by('-created_date')
    paginator= Paginator(topics,5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'topics': topics,
        'query':query,
        'page_obj': page_obj
    }
    return render(request, 'search.html', context)
    # return render(request,'search.html')
    # return HttpResponse("this is search")
   
    

