import unittest
import json
from DispersionPro.api.api_endpoints import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_gaussian_plume(self):
        payload = {
            'Q': 100,
            'u': 5,
            'x': 100,
            'y': 0,
            'z': 0,
            'H': 50,
            'sigma_y': 30,
            'sigma_z': 10
        }
        response = self.app.post('/api/gaussian_plume', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertAlmostEqual(data['concentration'], 0.01792, places=5)

if __name__ == '__main__':
    unittest.main()
