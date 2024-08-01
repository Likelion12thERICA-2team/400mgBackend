from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView
from .views import UserPostListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),  
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  
    path('posts/create/', PostCreateView.as_view(), name='post-create'),  
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  

    path('mypage/posts/', UserPostListView.as_view(), name='user-post-list'),

]
