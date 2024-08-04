from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, ReplyViewSet, ScrapViewSet, ScrapListView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

post_router = DefaultRouter()
post_router.register(r'replies', ReplyViewSet)
post_router.register(r'scraps', ScrapViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('scraps/', ScrapListView.as_view()),
]

"""
1. posts/
- get : post 리스트
- post : 로그인 된 user의 post 작성

2. posts/?my_posts=true/
- get : 로그인 된 사용자가 작성한 post 리스트
        *** mypage에서 내가 쓴 글 확인 시 사용 ***

3. posts/<int:pk>/
- get : 특정 post의 세부 내용 반환
- put : update(완전 수정)
- patch : partial_update(일부 수정)
- delete : 특정 post 삭제
"""