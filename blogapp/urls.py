from django.urls import path
from .views import blogList,blogDetail,blogCreate,updateBlog,userLoginView,userProfile,userRegister,deleteBlog,searchView,ChangePasswordView
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
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html',email_template_name='reset_email.html'),name="reset_password"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="reset_password_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="reset_password_confirm"),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),   
]