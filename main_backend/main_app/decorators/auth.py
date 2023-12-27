import jwt
from functools import wraps
from rest_framework.response import Response
from main_app.config.jwt_config import JWTConfig
from main_app.config.error_code_config import ErrorCodeConfig


def check_authentication(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        token = request.COOKIES.get(JWTConfig.COOKIE_NAME)

        if not token:
            return Response(
                {"status": "fail", "message": "You are not logged in. Please login to perform this action",
                    "code": ErrorCodeConfig.NOT_FOUND_TOKEN},
                status=401
            )

        try:
            jwt_secret_key = JWTConfig.SECRET_KEY
            jwt_algorithm = JWTConfig.ALGORITHM

            payload = jwt.decode(token, jwt_secret_key,
                                 algorithms=[jwt_algorithm])
            request.user_id = payload.get('id')

        except jwt.ExpiredSignatureError:
            return Response(
                {"status": "fail", "message": "JWT has expired",
                    "code": ErrorCodeConfig.EXPIRED_TOKEN},
                status=401
            )
        except jwt.InvalidTokenError:
            return Response(
                {"status": "fail", "message": "Invalid JWT",
                    "code": ErrorCodeConfig.INVALID_TOKEN},
                status=401
            )

        return view_func(request, *args, **kwargs)

    return _wrapped_view
