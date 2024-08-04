from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Follow
from users.models import CustomUser
from .serializers import FollowSerializer

class FollowUserView(generics.CreateAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user_to_follow_id = self.kwargs.get('user_id')
        user_to_follow = CustomUser.objects.get(id=user_to_follow_id)
        user = self.request.user

        if user == user_to_follow:
            raise serializers.ValidationError("You cannot follow yourself.")
        
        Follow.objects.create(user=user_to_follow, follower=user)

class UnfollowUserView(generics.DestroyAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_to_unfollow_id = self.kwargs.get('user_id')
        user_to_unfollow = CustomUser.objects.get(id=user_to_unfollow_id)
        return Follow.objects.get(user=user_to_unfollow, follower=self.request.user)

    def delete(self, request, *args, **kwargs):
        try:
            self.get_object().delete()
            return Response({"detail": "Unfollowed successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Follow.DoesNotExist:
            return Response({"detail": "Follow relationship does not exist."}, status=status.HTTP_404_NOT_FOUND)


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
