# core/gaussian_plume.py

import numpy as np

class GaussianPlumeModel:
    @staticmethod
    def calculate_dispersion_coefficients(x, stability_class):
        """
        Calculate sigma_y and sigma_z based on distance and stability class.

        Parameters:
            x : float : Downwind distance from the source
            stability_class : str : Stability class (A-F)

        Returns:
            Tuple[float, float] : sigma_y, sigma_z
        """
        stability_coeffs = {
            'A': (0.22, 0.20),
            'B': (0.16, 0.12),
            'C': (0.11, 0.08),
            'D': (0.08, 0.06),
            'E': (0.06, 0.03),
            'F': (0.04, 0.016)
        }
        a_y, b_y = stability_coeffs.get(stability_class, (0.08, 0.06))
        sigma_y = max(a_y * x ** 0.894, 1e-10)  # Small offset to prevent zero
        sigma_z = max(b_y * x ** 0.894, 1e-10)  # Small offset to prevent zero
        return sigma_y, sigma_z
    def gaussian_plume_concentration(Q, u, x, y, z, H, sigma_y, sigma_z):
        """
        Calculate the concentration using the Gaussian Plume Model.

        This model assumes a steady-state, continuous emission source in the
        presence of wind, typically applied to estimate ground-level concentrations.

        Parameters:
            Q : float : Emission rate (g/s)
            u : float : Wind speed (m/s)
            x : float : Downwind distance from the source (m)
            y : float : Crosswind distance (m)
            z : float : Vertical height above the ground (m)
            H : float : Effective stack height (m)
            sigma_y : float : Horizontal dispersion coefficient (m)
            sigma_z : float : Vertical dispersion coefficient (m)

        Returns:
            C : float : Pollutant concentration at point (x, y, z)
        """
        # Gaussian distribution in the crosswind (y) and vertical (z) directions
        exponent_y = -(y**2) / (2 * sigma_y**2)
        exponent_z = -(z - H)**2 / (2 * sigma_z**2)
        
        # Gaussian Plume concentration formula
        C = (Q / (2 * np.pi * u * sigma_y * sigma_z)) * np.exp(exponent_y) * np.exp(exponent_z)
        
        return C
