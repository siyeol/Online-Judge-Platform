from django.test import TestCase, Client
from django.urls import reverse
import json

class CodeRunViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.code_run_url = reverse("code_run")  # Replace "code_run" with the actual URL name in your urls.py

    def test_code_run_success(self):
        sample_code = "print('Hello, world!')"
        response = self.client.post(
            self.code_run_url,
            data=json.dumps({"code": sample_code}),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertIn("stdout", response_data)
        self.assertIn("stderr", response_data)
        self.assertEqual(response_data["stdout"], "Hello, world!")
        self.assertEqual(response_data["stderr"], None)

    def test_code_run_error(self):
        sample_code = "print(undefined_variable)"
        response = self.client.post(
            self.code_run_url,
            data=json.dumps({"code": sample_code}),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertIn("stdout", response_data)
        self.assertIn("stderr", response_data)
        self.assertEqual(response_data["stdout"], None)
        self.assertIn("NameError: name 'undefined_variable' is not defined", response_data["stderr"])
