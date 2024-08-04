from rest_framework import generics, viewsets
from .models import Post, Reply, Scrap
from .serializers import PostSerializer, ReplySerializer, ScrapSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 모든 게시물 또는 로그인된 사용자가 작성한 게시물만 반환
        user = self.request.user
        if self.request.query_params.get('my_posts', 'false') == 'true':
            return Post.objects.filter(user=user)
        return Post.objects.all()

    def perform_create(self, serializer):
        # 새 게시물을 생성할 때 현재 로그인한 사용자를 작성자로 설정
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        # 게시물을 삭제하기 전에 사용자 권한을 확인
        post = self.get_object()
        if post.user != request.user:
            return Response({"detail": "You do not have permission to delete this post."},
                            status=status.HTTP_403_FORBIDDEN)

        return super().destroy(request, *args, **kwargs)



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
    
    def destroy(self, request, *args, **kwargs):
        reply = self.get_object()
        if reply.user != request.user:
            return Response({"detail": "You do not have permission to delete this reply."},
                            status=status.HTTP_403_FORBIDDEN)

        return super().destroy(request, *args, **kwargs)



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
