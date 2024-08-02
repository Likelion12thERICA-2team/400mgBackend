# accounts/views.py
from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated
from .models import Follow
from .serializers import FollowSerializer
from users.models import CustomUser

class FollowUserView(generics.CreateAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user_to_follow_id = self.kwargs.get('user_id')
        user_to_follow = CustomUser.objects.get(id=user_to_follow_id)
        user = self.request.user

        if user == user_to_follow:
            raise serializers.ValidationError("You cannot follow yourself.")
        
        # Create the Follow instance with the current user as the follower
        Follow.objects.create(user=user_to_follow, follower=user)

class UnfollowUserView(generics.DestroyAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_to_unfollow_id = self.kwargs.get('user_id')
        user_to_unfollow = CustomUser.objects.get(id=user_to_unfollow_id)
        return Follow.objects.get(user=user_to_unfollow, follower=self.request.user)

class FollowingListView(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(follower=user)

class FollowersListView(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(user=user)
