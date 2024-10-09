def pasquill_gifford_class(stability_class, distance):
    """
    Calculate the horizontal and vertical dispersion coefficients using the Pasquill-Gifford method.

    Parameters:
    stability_class : str - Stability class (A, B, C, D, E, F)
    distance : float - Distance from the source (m)

    Returns:
    sigma_y : float - Horizontal dispersion coefficient (m)
    sigma_z : float - Vertical dispersion coefficient (m)
    """
    if stability_class == 'A':
        sigma_y = 0.22 * distance * (1 + 0.0001 * distance) ** -0.5
        sigma_z = 0.2 * distance
    elif stability_class == 'B':
        sigma_y = 0.16 * distance * (1 + 0.0001 * distance) ** -0.5
        sigma_z = 0.12 * distance
    elif stability_class == 'C':
        sigma_y = 0.11 * distance * (1 + 0.0001 * distance) ** -0.5
        sigma_z = 0.08 * distance
    elif stability_class == 'D':
        sigma_y = 0.08 * distance * (1 + 0.0001 * distance) ** -0.5
        sigma_z = 0.06 * distance
    elif stability_class == 'E':
        sigma_y = 0.06 * distance * (1 + 0.0001 * distance) ** -0.5
        sigma_z = 0.03 * distance
    elif stability_class == 'F':
        sigma_y = 0.04 * distance * (1 + 0.0001 * distance) ** -0.5
        sigma_z = 0.016 * distance
    else:
        raise ValueError(f"Unknown stability class: {stability_class}")
    
    return sigma_y, sigma_z
