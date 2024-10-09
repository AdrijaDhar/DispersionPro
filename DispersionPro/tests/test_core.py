import unittest
from DispersionPro.core.gaussian_plume import gaussian_plume
from DispersionPro.core.gaussian_puff import gaussian_puff

class TestCoreModels(unittest.TestCase):
    def test_gaussian_plume(self):
        concentration = gaussian_plume(100, 5, 100, 0, 0, 50, 30, 10)
        self.assertAlmostEqual(concentration, 0.01792, places=5)

    def test_gaussian_puff(self):
        concentration = gaussian_puff(100, 60, 100, 0, 0, 5, 30, 20, 10)
        self.assertAlmostEqual(concentration, 0.00157, places=5)

if __name__ == '__main__':
    unittest.main()
