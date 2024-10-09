def toxic_threshold(concentration, threshold):
    """
    Check if the concentration exceeds the toxic threshold.

    Parameters:
    concentration: float - Pollutant concentration at a point (g/m^3)
    threshold: float - Toxicity threshold (g/m^3)

    Returns:
    is_toxic: bool - True if concentration exceeds threshold
    """
    return concentration > threshold
