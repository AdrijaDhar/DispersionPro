import numpy as np

def gaussian_plume(Q, u, x, y, z, H, sigma_y, sigma_z):
    """
    Calculate the concentration using the Gaussian Plume Model.

    Parameters:
    Q : float - Emission rate (g/s)
    u : float - Wind speed (m/s)
    x : float - Downwind distance from the source (m)
    y : float - Crosswind distance (m)
    z : float - Vertical height above the ground (m)
    H : float - Effective stack height (m)
    sigma_y : float - Horizontal dispersion coefficient (m)
    sigma_z : float - Vertical dispersion coefficient (m)

    Returns:
    C : float - Pollutant concentration at point (x, y, z)
    """
    exponent_y = -(y**2) / (2 * sigma_y**2)
    exponent_z = -(z - H)**2 / (2 * sigma_z**2)
    
    C = (Q / (2 * np.pi * u * sigma_y * sigma_z)) * np.exp(exponent_y) * np.exp(exponent_z)
    
    return C
