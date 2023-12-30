from django.test import TestCase, Client
from main_app.tests.utils.test_authentication import TestAuthentication
from main_app.models.user import User
from main_app.tests.configs.test_user_config import TestUserConfig
from main_app.utils.auth import generate_jwt
from main_app.config.jwt_config import JWTConfig
from main_app.tests.utils.send_request import RequestInfo, send_json_request


class TestCheckAuthView(TestCase):
    def setUp(self):
        self.client = Client()
        self.CHECK_AUTH_URL = "http://localhost:8000/api/auth/checkAuth"

        self.user_strong_password = TestUserConfig.STRONG_PASSWORD
        self.user = User.objects.create_user(
            username="username", password=self.user_strong_password)

        self.valid_token = generate_jwt(
            str(self.user.id), JWTConfig.EXPIRATION_TIME_IN_SECONDS)

    def test_authentication(self):
        test_authentication_testcases = TestAuthentication(
            self.CHECK_AUTH_URL, self.client, self.assertEqual)
        test_authentication_testcases.run_all_tests()

    def test_view_with_valid_token(self):
        headers = {
            "Cookie": f"token={self.valid_token}"
        }
        request_info = RequestInfo(
            self.CHECK_AUTH_URL, method="POST", headers=headers)
        response = send_json_request(self.client, request_info)
        self.assertEqual(response.status_code, 200)
