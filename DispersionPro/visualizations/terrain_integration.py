# visualizations/terrain_integration.py

import numpy as np

def modify_dispersion_for_terrain(concentration_data, elevation_data):
    """
    Modify concentration data based on terrain elevation.
    Parameters:
        concentration_data : np.array : Original concentration values
        elevation_data : np.array : Elevation data (e.g., from a digital elevation model)
    Returns:
        np.array : Adjusted concentration data
    """
    # Simple model: reduce concentration based on elevation
    adjusted_concentration = concentration_data * np.exp(-0.001 * elevation_data)
    return adjusted_concentration
