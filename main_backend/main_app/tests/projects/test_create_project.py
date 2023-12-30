from django.test import TestCase, Client
from main_app.models import User
from main_app.tests.configs.test_user_config import TestUserConfig
from main_app.tests.utils.test_authentication import TestAuthentication


class TestSignUpView(TestCase):
    def setUp(self):
        self.client = Client()

        self.CREATE_PROJECT_URL = "http://localhost:8000/api/projects/"

        self.user_strong_password = TestUserConfig.STRONG_PASSWORD
        self.user = User.objects.create_user(
            username="username", password=self.user_strong_password)

    def test_authentication(self):
        test_authentication_testcases = TestAuthentication(
            self.CREATE_PROJECT_URL, self.client, self.assertEqual)
        test_authentication_testcases.run_all_tests()
