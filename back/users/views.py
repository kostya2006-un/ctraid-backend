from .models import User
from .serializers import UserSerializer, UserListSerializer
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserList(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_class = [permissions.IsAdminUser]
