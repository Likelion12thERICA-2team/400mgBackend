from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, ReplyViewSet, ScrapViewSet, ScrapListView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'posts/(?P<post_id>\d+)/replies', ReplyViewSet, basename='reply')

post_router = DefaultRouter()
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

4. posts/<post_id>/replies/
- get : 특정 post의 댓글 목록 반환
- post : 특정 post의 댓글 생성

5. posts/<post_id>/replies/<pk>/
- get : 특정 reply의 세부 내용 반환
- put : 특정 reply 완전 수정
- patch : 특정 reply 일부 수정
- delete : 특정 reply 삭제

6. scraps/
- 내가 스크랩 한 글 리스트 
        *** mypage???? ***
"""