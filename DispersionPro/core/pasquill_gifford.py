# core/pasquill_gifford.py

import numpy as np

class PasquillGiffordModel:
    @staticmethod
    def pasquill_gifford_concentration(Qm, u, x, y, z, stability_class):
        """Pasquill-Gifford Model with dispersion coefficients"""
        stability_factors = {'A': 1.0, 'B': 0.9, 'C': 0.8, 'D': 0.7, 'E': 0.6, 'F': 0.5}
        factor = stability_factors.get(stability_class, 1.0)
        sigma_y = factor * 0.1 * x  # Dispersion coefficient example
        sigma_z = factor * 0.05 * x
        return (Qm / (u * sigma_y * sigma_z)) * np.exp(-0.5 * ((y**2 / sigma_y**2) + (z**2 / sigma_z**2)))
