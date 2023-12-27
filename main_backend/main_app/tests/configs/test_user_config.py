from .test_config import test_config


class TestUserConfig:
    STRONG_PASSWORD = test_config("TEST_USER_STRONG_PASSWORD")
    WEAK_PASSWORD = test_config("TEST_USER_WEAK_PASSWORD")
