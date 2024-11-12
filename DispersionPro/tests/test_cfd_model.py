# tests/test_cfd_model.py

import unittest
from core.cfd_model import calculate_cfd_concentration  # Assume this function exists in `cfd_model.py`

class TestCFDModel(unittest.TestCase):
    def test_calculate_cfd_concentration(self):
        result = calculate_cfd_concentration(Qm=1.0, wind_speed=5.0, diffusivity=0.1, x=10, y=5)
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)  # Assuming concentration should be positive

if __name__ == "__main__":
    unittest.main()
