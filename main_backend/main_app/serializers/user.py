from rest_framework import serializers
from main_app.models import User
from main_app.validators.user_validator import UserValidator


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        error_messages={
            'required': 'Username is required',
        },

        validators=[UserValidator.validate_unique_username(
            queryset=User.objects.all())],
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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password', None)
        return data

    def create(self, data):
        return User.objects.create_user(data["username"], data["password"])
