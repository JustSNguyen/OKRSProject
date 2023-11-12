import jwt

from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main_app.utils import data_sanitizer, error
from main_app.serializers.user import UserSerializer
from main_app.models.user import User
from main_app.config.user_config import UserConfig
from main_app.config.jwt_config import JWTConfig


class AuthViews:
    @api_view(["POST"])
    def sign_up_view(request):
        sanitized_request_data = data_sanitizer.sanitize_data(request.data,
                                                              UserConfig.ALLOWED_USER_SIGN_UP_FIELDS)
        user_serializer = UserSerializer(data=sanitized_request_data)

        if user_serializer.is_valid():
            user_serializer.save()
            return AuthViews.get_auth_response(user_serializer.data, status_code=201)
        else:
            error_message = error.generate_error_message_from_serializer_errors(
                user_serializer.errors)
            return Response({"status": "fail", "message": error_message}, 400)

    @api_view(["POST"])
    def login_view(request):
        username = request.data.get("username", "")
        password = request.data.get("password", "")

        if username == "" or password == "":
            return Response({"status": "fail", "message": "Username and password can not be empty"}, 400)

        incorrect_username_or_password_response = Response(
            {"status": "fail", "message": "Incorrect username or password"}, 400)

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            return incorrect_username_or_password_response

        is_correct_password = user.check_password(password)
        if not is_correct_password:
            return incorrect_username_or_password_response

        user_serializer = UserSerializer(user)
        return AuthViews.get_auth_response(user_serializer.data)

    def get_auth_response(user, status_code=200):
        response = Response(
            {"status": "success", "data": {"user": user}}, status_code)

        jwt = AuthViews.generate_jwt(user["id"])
        jwt_cookie_name = JWTConfig.COOKIE_NAME
        jwt_expiration_time_in_seconds = JWTConfig.EXPIRATION_TIME_IN_SECONDS
        response.set_cookie(jwt_cookie_name, jwt,
                            max_age=jwt_expiration_time_in_seconds, httponly=True, samesite="Strict")

        return response

    def generate_jwt(user_id):
        jwt_expiration_time_delta_in_seconds = JWTConfig.EXPIRATION_TIME_IN_SECONDS
        expiration_time_in_seconds = int(
            (datetime.utcnow() + timedelta(seconds=jwt_expiration_time_delta_in_seconds)).timestamp())

        payload = {
            "id": user_id,
            "exp": expiration_time_in_seconds
        }

        jwt_secret_key = JWTConfig.SECRET_KEY
        jwt_algorithm = JWTConfig.ALGORITHM

        jwt_token = jwt.encode(payload, jwt_secret_key,
                               algorithm=jwt_algorithm)

        return jwt_token
