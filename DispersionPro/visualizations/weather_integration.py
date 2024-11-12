# visualizations/weather_integration.py

import numpy as np

def adjust_dispersion_for_weather(concentration_data, wind_speed, wind_direction):
    """
    Adjust dispersion data based on weather (wind speed and direction).
    Parameters:
        concentration_data : np.array : Original concentration values
        wind_speed : float : Current wind speed
        wind_direction : float : Wind direction in degrees
    Returns:
        np.array : Adjusted concentration data
    """
    direction_factor = np.cos(np.radians(wind_direction))  # Simplified adjustment
    adjusted_concentration = concentration_data * (1 + wind_speed * 0.1 * direction_factor)
    return adjusted_concentration
