from .models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):

    class Meta:
        model = User

        fields = [
            "user_id",
            "is_bot",
            "first_name",
            "last_name",
            "username",
        ]


class UserListSerializer(ModelSerializer):

    class Meta:
        model = User

        fields = [
            "user_id",
        ]
