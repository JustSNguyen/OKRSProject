from .test_config import test_config


class TestLoginViewConfig:
    CORRECT_PASSWORD = test_config("TEST_LOGIN_CORRECT_PASSWORD")
    WRONG_PASSWORD = test_config("TEST_LOGIN_WRONG_PASSWORD")
