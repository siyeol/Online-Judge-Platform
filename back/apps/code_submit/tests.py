from django.test import TestCase, Client
from django.urls import reverse
import json

class CodeSubmitViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_code_submit_view(self):
        code = """
        def minus(a, b):
            return (a-b)
        a, b = 2, 3
        result = minus(a, b)
        print(result)
        """
        class_id = 1
        assign_id = 1
        user_id = 1

        # send a POST request to the view with the code, class_id, assign_id, and user_id
        url = reverse('code_submit')
        data = {'code': code, 'class_id': class_id, 'assign_id': assign_id, 'user_id': user_id}
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertIn('result', response_data)
        self.assertIn('score', response_data)
        score = response_data['score']
        self.assertIn('code_efficiency', score)
        self.assertIn('code_explain', score)
        self.assertIn('code_readability', score)
        self.assertIn('copy_detect', score)
        self.assertIn('code_diff_str', score)
        self.assertIn('total', score)

        result = response_data['result']
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)

        self.assertIsInstance(score['code_efficiency'], dict)
        self.assertIsInstance(score['code_explain'], str)
        self.assertIsInstance(score['code_readability'], list)
        self.assertIsInstance(score['copy_detect'], float)
        self.assertIsInstance(score['code_diff_str'], str)
        self.assertIsInstance(score['total'], float)
