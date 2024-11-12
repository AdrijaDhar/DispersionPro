# tests/test_api.py

import unittest
import requests

class TestAPI(unittest.TestCase):
    BASE_URL = "http://localhost:5000"  # Change to actual API endpoint

    def test_dispersion_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/dispersion", params={'Qm': 1.0, 'K': 0.1, 'r': 10})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("concentration", data)

if __name__ == "__main__":
    unittest.main()
