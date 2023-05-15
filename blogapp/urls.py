from django.urls import path
from .views import blogList,blogDetail,blogCreate,updateBlog,userLoginView,userProfile,userRegister,deleteBlog,searchView,ChangePasswordView,resetPasswordView
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('', blogList, name="tasks"),
    path('detail/<int:id>', (blogDetail), name="detail"),
    path('login/', userLoginView.as_view(), name="login-user"),
    path('register/', userRegister, name="register-user"),
    path('blog_create/', (blogCreate),name="create"),
    path('update_blog/<int:id>',updateBlog, name="update"),
    path('delete_blog/<int:id>',deleteBlog,name="delete"),
    path('profile/<int:id>', userProfile,name="profile"),
    path('search', searchView, name="search"),
    path('password/', ChangePasswordView.as_view(), name="one"),
    path('reset',resetPasswordView.as_view(), name="password_reset" ),
    
]