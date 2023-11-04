from django.test import TestCase, Client
from decouple import config

from main_app.models import User
from main_app.tests.utils.send_request import send_json_request, RequestInfo


class TestSignUpView(TestCase):
    def setUp(self):
        self.client = Client()
        self.SIGN_UP_URL = "http://localhost:8000/api/auth/signUp"

        self.already_existed_username = "already_existed_username"
        self.valid_username = "valid_username"
        self.user_strong_password = config("TEST_USER_STRONG_PASSWORD")
        self.user_weak_password = config("TEST_USER_WEAK_PASSWORD")
        User.objects.create_user(username=self.already_existed_username,
                                 password=self.user_strong_password)

    def test_sign_up_with_no_data(self):
        response = send_json_request(
            self.client, RequestInfo(url=self.SIGN_UP_URL, method="POST"))
        message_if_test_fails = f"Status code should be 400, got {response.status_code}"
        self.assertEqual(response.status_code, 400, message_if_test_fails)

    def test_sign_up_with_existed_username(self):
        data = {
            "username": self.already_existed_username,
            "password": self.user_strong_password
        }
        request_info = RequestInfo(
            data=data, url=self.SIGN_UP_URL, method="POST")
        response = send_json_request(self.client, request_info)
        message_if_test_fails = f"Status code should be 400, got {response.status_code}"
        self.assertEqual(response.status_code, 400, message_if_test_fails)

    def test_sign_up_with_weak_password(self):
        data = {
            "username": self.valid_username,
            "password": self.user_weak_password
        }
        request_info = RequestInfo(
            data=data, url=self.SIGN_UP_URL, method="POST")
        response = send_json_request(self.client, request_info)
        message_if_test_fails = f"Status code should be 400, got {response.status_code}"
        self.assertEqual(response.status_code, 400, message_if_test_fails)

    def test_sign_up_successfully_status_code(self):
        data = {
            "username": self.valid_username,
            "password": self.user_strong_password
        }
        request_info = RequestInfo(
            data=data, url=self.SIGN_UP_URL, method="POST")
        response = send_json_request(self.client, request_info)
        message_if_test_fails = f"Status code should be 201, got {response.status_code}"
        self.assertEqual(response.status_code, 201, message_if_test_fails)

    def test_token_exists_in_cookie_if_sign_up_successfully(self):
        data = {
            "username": self.valid_username,
            "password": self.user_strong_password
        }
        request_info = RequestInfo(
            data=data, url=self.SIGN_UP_URL, method="POST")
        response = send_json_request(self.client, request_info)
        message_if_test_fails = f"Token should exist inside response cookie but not found."
        self.assertIn('token', response.cookies, message_if_test_fails)

    def test_password_should_be_hashed_if_sign_up_successfully(self):
        data = {
            "username": self.valid_username,
            "password": self.user_strong_password
        }
        request_info = RequestInfo(
            data=data, url=self.SIGN_UP_URL, method="POST")
        send_json_request(self.client, request_info)

        user = User.objects.get(username=self.valid_username)
        message_if_test_fails = f"Saved password should not be equal to sent password"
        self.assertNotEqual(
            user.password, self.user_strong_password, message_if_test_fails)

    def test_disallowed_fields_should_not_be_saved(self):
        data = {
            "username": self.valid_username,
            "password": self.user_strong_password,
            "is_staff": True,
            "is_superuser": True,
            "is_active": False
        }
        request_info = RequestInfo(
            data=data, url=self.SIGN_UP_URL, method="POST")
        send_json_request(self.client, request_info)

        user = User.objects.get(username=self.valid_username)

        self.assertEqual(user.is_staff, False, "is_staff should be False")
        self.assertEqual(user.is_superuser, False,
                         "is_superuser should be False")
        self.assertEqual(user.is_active, True, "is_active should be True")
