from rest_framework import generics, viewsets
from .models import Post, Reply, Scrap
from .serializers import PostSerializer, ReplySerializer, ScrapSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Reply.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(id=post_id)
        return serializer.save(user=self.request.user, post=post)


class ScrapViewSet(viewsets.ModelViewSet):
    queryset = Scrap.objects.all()
    serializer_class = ScrapSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        if post_id:
            return Scrap.objects.filter(post_id=post_id)
        return Scrap.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(id=post_id)
        user = self.request.user

        serializer.save(user=user, post=post)

    def create(self, request, *args, **kwargs):
        post_id = self.kwargs.get('post_id')
        user = request.user

        if Scrap.objects.filter(user=user, post_id=post_id).exists():
            return Response({"detail": "이미 스크랩된 게시물입니다."}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        post_id = self.kwargs.get('post_id')
        user = request.user

        # 게시물 ID와 사용자 ID를 기준으로 스크랩 삭제
        try:
            scrap = Scrap.objects.get(post_id=post_id, user=user)
        except Scrap.DoesNotExist:
            raise NotFound(
                "Scrap not found or you do not have permission to delete it.")

        # 스크랩 삭제
        scrap.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ScrapListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(scrap__user=self.request.user)
