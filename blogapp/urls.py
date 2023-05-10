from django.urls import path
from .views import blogList,blogDetail,userLoginView
from django.contrib.auth.decorators import login_required


urlpatterns =[
    path('', blogList, name="tasks"),
    path('detail/<int:id>', login_required(blogDetail), name="detail"),
    path('login/', userLoginView.as_view(),name="login"),
]