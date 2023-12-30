from django.test import TestCase, Client

from main_app.tests.configs.test_login_view_config import TestLoginViewConfig
from main_app.models import User
from main_app.tests.utils.send_request import send_json_request, RequestInfo


class TestLoginView(TestCase):
    def setUp(self):
        self.client = Client()

        self.LOGIN_URL = "http://localhost:8000/api/auth/login"

        self.correct_username = "correct_username"
        self.wrong_username = "wrong_username"
        self.correct_password = TestLoginViewConfig.CORRECT_PASSWORD
        self.wrong_password = TestLoginViewConfig.WRONG_PASSWORD

        User.objects.create_user(username=self.correct_username,
                                 password=self.correct_password)

    def test_login_no_data(self):
        response = send_json_request(
            self.client, self.create_login_request_info())
        self.assertEqual(response.status_code, 400,
                         f"Expected 400 but got {response.status_code}")

    def test_login_with_wrong_username(self):
        data = {
            "username": self.wrong_username,
            "password": self.wrong_password
        }
        login_request_info = self.create_login_request_info(data)
        response = send_json_request(self.client, login_request_info)
        self.assertEqual(response.status_code, 400,
                         f"Expected 400 but got {response.status_code}")

    def test_login_with_correct_username_but_wrong_password(self):
        data = {
            "username": self.correct_username,
            "password": self.wrong_password
        }
        login_request_info = self.create_login_request_info(data)
        response = send_json_request(self.client, login_request_info)
        self.assertEqual(response.status_code, 400,
                         f"Expected 400 but got {response.status_code}")

    def test_login_with_correct_credentials(self):
        data = {
            "username": self.correct_username,
            "password": self.correct_password
        }
        login_request_info = self.create_login_request_info(data)
        response = send_json_request(self.client, login_request_info)

        self.assertEqual(response.status_code, 200,
                         f"Expected 200 but got {response.status_code}")

        self.assertNotIn("password", response.json(),
                         "Password should not be in response")

        self.assertIn('token', response.cookies,
                      "No token found in cookie when login successfully.")

    def create_login_request_info(self, data={}):
        return RequestInfo(self.LOGIN_URL, method="POST", data=data)
