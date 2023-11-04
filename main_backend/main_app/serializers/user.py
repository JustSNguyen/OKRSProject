from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from main_app.models import User
from main_app.validators.user_validator import UserValidator


class UserSerializer(serializers.ModelSerializer):
    username_unique_validator = UniqueValidator(
        queryset=User.objects.all(),
        message="An user with that username already existed")

    username = serializers.CharField(
        error_messages={
            'required': 'Username is required',
        },

        validators=[username_unique_validator],
    )
    password = serializers.CharField(
        error_messages={
            'required': 'Password is required',
        },
        validators=[UserValidator.validate_strong_password]
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'date_created']

    def create(self, data):
        return User.objects.create_user(data["username"], data["password"])