import re
from main_app.config.user_config import UserConfig
from django.core.exceptions import ValidationError
from rest_framework.validators import UniqueValidator


class UserValidator:
    def validate_unique_username(queryset):
        return UniqueValidator(queryset=queryset, message="An user with that username already existed")

    def validate_strong_password(password):
        if len(password) < UserConfig.MIN_PASSWORD_LENGTH:
            raise ValidationError(
                "Password must be at least 12 characters long.")
        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                "Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password):
            raise ValidationError(
                "Password must contain at least one lowercase letter.")
        if not re.search(r'[!@#$%^&*()_+{}[\]:;<>,.?~\\-]', password):
            raise ValidationError(
                "Password must contain at least one special character.")
