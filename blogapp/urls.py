from django.urls import path
from .views import blogList,blogDetail,blogCreate,updateBlog,userLoginView,userProfile
from django.contrib.auth.decorators import login_required


urlpatterns =[
    path('', blogList, name="tasks"),
    path('detail/<int:id>', (blogDetail), name="detail"),
    path('login/', userLoginView.as_view(),name="login"),
    path('blog_create/', login_required(blogCreate),name="create"),
    path('update_blog/<int:id>',login_required(updateBlog),name="update"),
    path('profile/<int:id>', login_required(userProfile),name="profile"),
]