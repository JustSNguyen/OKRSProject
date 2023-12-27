from django.test import TestCase, Client

from main_app.tests.configs.test_login_view_config import TestLoginViewConfig
from main_app.models import User
from main_app.tests.utils.send_request import send_json_request, RequestInfo
from main_app.utils.auth import generate_jwt
from main_app.tests.configs.test_user_config import TestUserConfig
from main_app.config.error_code_config import ErrorCodeConfig


class TestSignUpView(TestCase):
    def setUp(self):
        self.client = Client()

        self.CREATE_PROJECT_URL = "http://localhost:8000/api/projects/"

        self.user_strong_password = TestUserConfig.STRONG_PASSWORD
        self.user = User.objects.create_user(
            username="username", password=self.user_strong_password)
        self.outdated_jwt = generate_jwt(
            str(self.user.id), max_age_in_seconds=0)
        self.invalid_jwt = "invalid_jwt"

    def test_create_project_route_exists(self):
        request_info = RequestInfo(self.CREATE_PROJECT_URL, method="POST")
        response = send_json_request(self.client, request_info)

        self.assertNotEqual(response.status_code, 404)

    def test_create_project_unauthenticated(self):
        request_info = RequestInfo(self.CREATE_PROJECT_URL, method="POST")
        response = send_json_request(self.client, request_info)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["code"],
                         ErrorCodeConfig.NOT_FOUND_TOKEN)

    def test_create_project_with_outdated_jwt(self):
        headers = {
            "Cookie": f"token={self.outdated_jwt}"
        }
        request_info = RequestInfo(
            self.CREATE_PROJECT_URL, method="POST", headers=headers)
        response = send_json_request(self.client, request_info)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["code"],
                         ErrorCodeConfig.EXPIRED_TOKEN)

    def test_create_project_with_invalid_jwt(self):
        headers = {
            "Cookie": f"token={self.invalid_jwt}"
        }
        request_info = RequestInfo(
            self.CREATE_PROJECT_URL, method="POST", headers=headers)
        response = send_json_request(self.client, request_info)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["code"],
                         ErrorCodeConfig.INVALID_TOKEN)
