from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView
from .views import CreateScrapView, DeleteScrapView
from .views import UserPostListView, UserScrapListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),  
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  
    path('posts/create/', PostCreateView.as_view(), name='post-create'),  
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  

    path('posts/<int:post_id>/scrap/', CreateScrapView.as_view(), name='create-scrap'),
    path('posts/<int:post_id>/scrap/delete/', DeleteScrapView.as_view(), name='delete-scrap'),

    path('mypage/scraps/', UserScrapListView.as_view(), name='user-scrap-list'),
    path('mypage/posts/', UserPostListView.as_view(), name='user-post-list'),

]
