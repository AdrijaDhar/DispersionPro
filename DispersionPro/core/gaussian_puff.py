import numpy as np

def gaussian_puff(Q, t, x, y, z, u, sigma_x, sigma_y, sigma_z):
    """
    Calculate the concentration using the Gaussian Puff Model.

    Parameters:
    Q : float - Total mass released (g)
    t : float - Time after release (s)
    x, y, z : float - Coordinates of the point (m)
    u : float - Wind speed (m/s)
    sigma_x, sigma_y, sigma_z : float - Dispersion coefficients (m)

    Returns:
    C : float - Pollutant concentration at point (x, y, z)
    """
    exponent_x = -(x - u * t)**2 / (2 * sigma_x**2)
    exponent_y = -(y**2) / (2 * sigma_y**2)
    exponent_z = -(z**2) / (2 * sigma_z**2)
    
    C = (Q / (2 * np.pi * sigma_x * sigma_y * sigma_z)) * np.exp(exponent_x) * np.exp(exponent_y) * np.exp(exponent_z)
    
    return C
