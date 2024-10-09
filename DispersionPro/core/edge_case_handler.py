# core/edge_case_handler.py

def adjust_for_low_wind(concentration, wind_speed):
    """
    Adjust the concentration calculation for low wind speed conditions.

    Parameters:
    concentration: float - Original concentration value.
    wind_speed: float - Wind speed in m/s.

    Returns:
    adjusted_concentration: float - Adjusted concentration value.
    """
    if wind_speed < 0.5:
        # Adjust concentration for low wind speed, e.g., by applying a correction factor
        adjusted_concentration = concentration * 1.5  # Example adjustment
        print("Low wind speed detected. Adjusting concentration.")
    else:
        adjusted_concentration = concentration
    return adjusted_concentration

def adjust_for_dense_gases(concentration, gas_density, air_density=1.225):
    """
    Adjust the concentration calculation for dense gas releases.

    Parameters:
    concentration: float - Original concentration value.
    gas_density: float - Density of the gas in kg/m^3.
    air_density: float - Density of air (default is 1.225 kg/m^3 at sea level).

    Returns:
    adjusted_concentration: float - Adjusted concentration value.
    """
    if gas_density > air_density:
        # Apply dense gas dispersion adjustments
        adjusted_concentration = concentration * 1.2  # Example adjustment
        print("Dense gas detected. Adjusting concentration.")
    else:
        adjusted_concentration = concentration
    return adjusted_concentration

def adjust_for_inversion_layers(concentration, inversion_present):
    """
    Adjust the concentration calculation for atmospheric inversion layers.

    Parameters:
    concentration: float - Original concentration value.
    inversion_present: bool - True if inversion layer is present.

    Returns:
    adjusted_concentration: float - Adjusted concentration value.
    """
    if inversion_present:
        # Adjust concentration due to limited vertical mixing
        adjusted_concentration = concentration * 2.0  # Example adjustment
        print("Inversion layer detected. Adjusting concentration.")
    else:
        adjusted_concentration = concentration
    return adjusted_concentration
