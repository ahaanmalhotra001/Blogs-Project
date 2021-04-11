from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path('', views.PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name="post-detail"),
    path('post/new', views.PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update') ,
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/', views.UserPostListView.as_view(), name='user-post'),
    path('about', views.about, name="blog-about"),

]