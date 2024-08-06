from django.urls import path
from .views import CustomUserViewSet

urlpatterns = [
    # 새로운 사용자를 생성하는 URL
    path('users/', CustomUserViewSet.as_view({'post': 'create'}), name='user-create'),
    path('users/<int:pk>/', CustomUserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'}), name='user-detail'),
    # 로그인된 사용자의 정보를 조회, 업데이트 및 부분 업데이트하는 URL
    path('mypage/myinfo/', CustomUserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'}), name='user-detail'),
    path('users/profile_pic/', CustomUserViewSet.as_view({'patch': 'update_profile_picture'}), name='update-profile-picture'),
]