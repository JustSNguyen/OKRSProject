
from django.test import TestCase
from main_app.tests.utils.send_request import send_json_request, RequestInfo
from main_app.config.error_code_config import ErrorCodeConfig
from main_app.utils.auth import generate_jwt
from main_app.config.jwt_config import JWTConfig


class TestAuthentication():
    def __init__(self, URL_TO_TEST, client, assert_equal_func):
        self.URL_TO_TEST = URL_TO_TEST

        self.outdated_jwt = generate_jwt("test_id", max_age_in_seconds=0)
        self.jwt_with_not_found_user = generate_jwt(
            "tet_id", max_age_in_seconds=JWTConfig.EXPIRATION_TIME_IN_SECONDS)
        self.client = client
        self.assertEqual = assert_equal_func

        self.invalid_jwt = "invalid_jwt"
        self.outdated_jwt = generate_jwt("user_id", 0)

    def run_all_tests(self):
        self.test_view_with_no_token()
        self.test_view_with_outdated_jwt()
        self.test_view_with_invalid_jwt()

    def test_view_with_no_token(self):
        request_info = RequestInfo(self.URL_TO_TEST, method="POST")
        response = send_json_request(self.client, request_info)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["code"],
                         ErrorCodeConfig.NOT_FOUND_TOKEN)

    def test_view_with_outdated_jwt(self):
        headers = {
            "Cookie": f"token={self.outdated_jwt}"
        }
        request_info = RequestInfo(
            self.URL_TO_TEST, method="POST", headers=headers)
        response = send_json_request(self.client, request_info)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["code"],
                         ErrorCodeConfig.EXPIRED_TOKEN)

    def test_view_with_invalid_jwt(self):
        headers = {
            "Cookie": f"token={self.invalid_jwt}"
        }
        request_info = RequestInfo(
            self.URL_TO_TEST, method="POST", headers=headers)
        response = send_json_request(self.client, request_info)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["code"],
                         ErrorCodeConfig.INVALID_TOKEN)

    def test_view_with_user_id_in_token_not_found(self):
        headers = {
            "Cookie": f"token={self.jwt_with_not_found_user}"
        }
        request_info = RequestInfo(
            self.URL_TO_TEST, method="POST", headers=headers)
        response = send_json_request(self.client, request_info)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["code"],
                         ErrorCodeConfig.USER_NOT_FOUND)
