def briggs_plume_rise(F, stability_class, u):
    """
    Calculate the plume rise using the Briggs equation for buoyancy-driven plumes.

    Parameters:
    F : float - Buoyancy flux parameter (m^4/s^3)
    stability_class : str - Stability class (A, B, C, D, E, F)
    u : float - Wind speed (m/s)

    Returns:
    plume_rise : float - Estimated plume rise (m)
    """
    if stability_class in ['A', 'B', 'C']:
        plume_rise = (F / (u ** 3)) ** 0.5
    else:
        plume_rise = (F / (u ** 2)) ** 0.33
    
    return plume_rise
