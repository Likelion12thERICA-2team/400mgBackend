from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, ReplyViewSet, ScrapViewSet, ScrapListView

router = DefaultRouter()
router.register(r'posts', PostViewSet)

post_router = DefaultRouter()
post_router.register(r'replies', ReplyViewSet)
post_router.register(r'scraps', ScrapViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/', include(post_router.urls)),
    path('scraps/', ScrapListView.as_view()),
]
