# core/briggs_plume.py

import numpy as np
from scipy.special import erfc

class BriggsPlumeModel:
    @staticmethod
    def steady_state_no_wind(Qm, K, r):
        """Case 1: Steady-State Continuous Point Release with No Wind"""
        return Qm / (4 * np.pi * K * r)

    @staticmethod
    def non_steady_state_no_wind(Qm, K, r, t):
        """Case 3: Non-Steady-State Continuous Point Release with No Wind"""
        return (Qm / (4 * np.pi * K * r)) * erfc(r / (2 * np.sqrt(K * t)))

    @staticmethod
    def steady_state_with_wind(Qm, K, u, x, y, z):
        """Case 4: Steady-State Continuous Point Source Release with Wind"""
        distance = np.sqrt(x**2 + y**2 + z**2)
        return (Qm / (4 * np.pi * K * distance)) * np.exp(-u**2 * distance / (4 * K * x))
