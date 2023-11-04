from decouple import config


class JWTConfig:
    EXPIRATION_TIME_IN_SECONDS = int(config("JWT_EXPIRATION_IN_SECONDS"))
    SECRET_KEY = config("JWT_SECRET_KEY")
    ALGORITHM = config("JWT_ALGORITHM")
    COOKIE_NAME = config("JWT_COOKIE_NAME")
