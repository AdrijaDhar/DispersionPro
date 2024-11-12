# tests/test_core.py

import unittest
from core.briggs_plume import BriggsPlumeModel
from core.gaussian_puff import GaussianPuffModel
from core.pasquill_gifford import PasquillGiffordModel

class TestCoreModels(unittest.TestCase):
    def test_steady_state_no_wind(self):
        result = BriggsPlumeModel.steady_state_no_wind(Qm=1.0, K=0.1, r=10)
        self.assertGreater(result, 0)

    def test_puff_no_wind(self):
        result = GaussianPuffModel.puff_no_wind(Qm=1.0, K=0.1, r=10, t=5)
        self.assertGreater(result, 0)

    def test_pasquill_gifford_concentration(self):
        result = PasquillGiffordModel.pasquill_gifford_concentration(Qm=1.0, u=5.0, x=10, y=5, z=0, stability_class="D")
        self.assertGreater(result, 0)

if __name__ == "__main__":
    unittest.main()
