from rest_framework import generics
from .models import Post
from .models import Scrap
from .serializers import ScrapSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticated

# post 관련 기능(마이페이지의 내가 쓴 글 포함)
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # 로그인된 사용자만 허용


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # 로그인된 사용자만 허용


class UserPostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(user=user)
    


# Scrap 관련 기능(마이페이지의 내가 스크랩 한 글 포함)
class CreateScrapView(generics.CreateAPIView):
    queryset = Scrap.objects.all()
    serializer_class = ScrapSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(id=post_id)
        serializer.save(user=user, post=post)


class DeleteScrapView(generics.DestroyAPIView):
    queryset = Scrap.objects.all()
    serializer_class = ScrapSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        post_id = self.kwargs.get('post_id')
        # Get the Scrap object for the logged-in user and the specific post
        return Scrap.objects.get(user=user, post_id=post_id)


class UserScrapListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Get all posts that the user has scrapped
        return Post.objects.filter(scrap__user=user)