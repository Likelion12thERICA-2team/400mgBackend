# accounts/urls.py
from django.urls import path
from .views import FollowUserView, UnfollowUserView, FollowingListView, FollowersListView, FollowUserByUsernameView

urlpatterns = [
    # path('friend/<int:user_id>/follow/',
    #      FollowUserView.as_view(), name='follow-user'),
    path('friend/<int:user_id>/unfollow/',
         UnfollowUserView.as_view(), name='unfollow-user'),
    path('friend/following/', FollowingListView.as_view(),
         name='user-following-list'),
    path('friend/followers/', FollowersListView.as_view(),
         name='user-followers-list'),
    path('friend/<str:username>/follow/',
         FollowUserByUsernameView.as_view(), name='follow-user'),
]
