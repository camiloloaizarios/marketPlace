from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('blogDetails/', views.blogDetails, name="blogDetails"),
]