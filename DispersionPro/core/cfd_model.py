# core/cfd_model.py

import numpy as np

class CFDModel:
    @staticmethod
    def calculate_concentration_cfd(Qm, u, D, x, y, t):
        """
        Simplified CFD-inspired model for dispersion.

        This function approximates the dispersion concentration using a Gaussian
        solution to the diffusion equation, assuming diffusion in x and y directions
        with a steady wind in the x-direction.

        Parameters:
            Qm : float : Source emission rate (mass/time)
            u : float : Wind speed in x-direction
            D : float : Diffusion coefficient
            x : float : Position in the x-direction
            y : float : Position in the y-direction
            t : float : Time since release started

        Returns:
            C : float : Concentration at (x, y) at time t
        """
        # Gaussian terms in x and y directions
        term_x = np.exp(-((x - u * t) ** 2) / (4 * D * t))
        term_y = np.exp(-(y ** 2) / (4 * D * t))
        
        # Simplified concentration formula
        C = (Qm / (4 * np.pi * D * t)) * term_x * term_y
        return C
