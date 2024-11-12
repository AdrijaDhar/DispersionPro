# core/aermod.py

import numpy as np

class AERMODModel:
    @staticmethod
    def aermod_concentration(Qm, u, z, stability_class, roughness_length):
        """
        Simplified AERMOD-inspired concentration calculation.
        
        Parameters:
            Qm : float : Emission rate (e.g., g/s)
            u : float : Wind speed (e.g., m/s)
            z : float : Height above ground level (e.g., m)
            stability_class : str : Atmospheric stability class (A-F)
            roughness_length : float : Surface roughness length (e.g., m)

        Returns:
            C : float : Estimated concentration at height z
        """
        # Simplified stability factor based on class
        stability_factors = {'A': 0.5, 'B': 0.6, 'C': 0.7, 'D': 0.8, 'E': 0.9, 'F': 1.0}
        factor = stability_factors.get(stability_class, 1.0)
        
        # Calculate effective height adjustment based on surface roughness
        effective_height = z + roughness_length * factor
        
        # Simple Gaussian profile for concentration (AERMOD uses more complex calculations)
        C = (Qm / (u * effective_height)) * np.exp(-z / (2 * factor))
        return C
