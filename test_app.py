import unittest
from main import app
import io

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_home_data(self):
        result = self.app.get('/')
        self.assertIn(b'AI Resume Analyser', result.data)
        self.assertIn(b'Upload Resume', result.data)

    def test_upload_no_file(self):
        result = self.app.post('/', data={}, follow_redirects=True)
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()
