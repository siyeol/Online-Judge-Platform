from django.test import TestCase, Client
from django.urls import reverse
import json

class CodeGradeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.code_grade_url = reverse('code_grade')

    def test_code_grade_view_with_prohibited_lib(self):
        payload = {
            "code": "import sys",
            "class_id": 1,
            "assign_id": 1,
            "user_id": 1
        }
        response = self.client.post(self.code_grade_url, json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertIn('result', response_data)
        self.assertEqual(response_data['result'], "Prohibited library Detected")

    def test_code_grade_view_without_prohibited_lib(self):
        payload = {
            "code": "print('Hello, World!')",
            "class_id": 1,
            "assign_id": 1,
            "user_id": 1
        }
        response = self.client.post(self.code_grade_url, json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertIn('result', response_data)
        self.assertNotEqual(response_data['result'], [False,"Time out"])
        self.assertNotEqual(response_data['result'], [False, "Error occur"])