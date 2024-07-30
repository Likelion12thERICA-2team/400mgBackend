
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('caffeinintakes/', include('caffeinIntakes.urls')),
    path('', include('users.urls')),
    path('', include('post.urls')),
]
