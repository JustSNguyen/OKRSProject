import jwt
from datetime import datetime, timedelta
from main_app.config.jwt_config import JWTConfig


def generate_jwt(user_id, max_age_in_seconds=JWTConfig.EXPIRATION_TIME_IN_SECONDS):
    expiration_time_in_seconds = int(
        (datetime.utcnow() + timedelta(seconds=max_age_in_seconds)).timestamp())

    payload = {
        "id": user_id,
        "exp": expiration_time_in_seconds
    }

    jwt_secret_key = JWTConfig.SECRET_KEY
    jwt_algorithm = JWTConfig.ALGORITHM

    jwt_token = jwt.encode(payload, jwt_secret_key,
                           algorithm=jwt_algorithm)

    return jwt_token
