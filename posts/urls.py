from django.urls import path
from .views import index, Home, post_detail, create_reply, CreatePost, PostDelete, like_post

app_name = 'posts'

urlpatterns = [
    path('', index),
    path('home/', Home.as_view(), name='home'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),
    path('posts/create_reply/', create_reply, name='create-reply'),
    path('posts/create_post/', CreatePost.as_view(), name='create-post'),
    path('posts/<int:pk>/delete', PostDelete.as_view(), name='delete-post'),
    path('posts/<int:pk>/like', like_post, name='like-post'),
]
