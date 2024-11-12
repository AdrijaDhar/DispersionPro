# core/gaussian_puff.py

import numpy as np

class GaussianPuffModel:
    @staticmethod
    def puff_no_wind(Qm, K, r, t):
        """Case 2: Puff with No Wind"""
        return (Qm / (8 * (np.pi * K * t)**1.5)) * np.exp(-r**2 / (4 * K * t))

    @staticmethod
    def puff_with_wind(Qm, u, Kx, Ky, Kz, x, y, z, t):
        """Case 5: Puff with Wind"""
        return (Qm / ((8 * np.pi * t)**1.5 * np.sqrt(Kx * Ky * Kz))) * \
               np.exp(-((x - u * t)**2 / (4 * Kx * t) + y**2 / (4 * Ky * t) + z**2 / (4 * Kz * t)))

    @staticmethod
    def puff_no_wind_ground(Qm, Kx, Ky, Kz, x, y, z, t):
        """Case 6: Puff with No Wind and with Source on Ground"""
        return (Qm / ((8 * np.pi * t)**1.5 * np.sqrt(Kx * Ky * Kz))) * \
               np.exp(-((x**2 / (4 * Kx * t)) + (y**2 / (4 * Ky * t)) + (z**2 / (4 * Kz * t))))
