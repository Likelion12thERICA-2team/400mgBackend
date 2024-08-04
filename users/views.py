from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED
from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)

    def list(self, request):
        # Optional: If you need to list users
        queryset = self.get_queryset()
        serializer = CustomUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = self.get_queryset().first()
        if not user:
            return Response({'detail': 'Not found.'}, status=HTTP_404_NOT_FOUND)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=HTTP_200_OK)

    def create(self, request):
        # Logic for creating a new user
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(CustomUserSerializer(user).data, status=HTTP_201_CREATED)

    def get_permissions(self):
        if (self.action == 'create'):
            return []
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        serialzer = self.get_serializer(data=request.data)
        serialzer.is_valid(raise_exception=True)
        user = serialzer.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            'user': serialzer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

    def update(self, request, pk=None):
        user = self.get_queryset().first()
        if not user:
            return Response({'detail': 'Not found.'}, status=HTTP_404_NOT_FOUND)
        serializer = CustomUserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=HTTP_200_OK)

    def partial_update(self, request, pk=None):
        return self.update(request, pk)
