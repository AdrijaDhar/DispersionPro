import numpy as np

def lagrangian_particle_dispersion(Q, x, y, z, u, dt, steps):
    """
    Simulate Lagrangian particle dispersion over time.

    Parameters:
    Q : float - Emission rate (g/s)
    x, y, z : float - Initial coordinates of the particles
    u : float - Wind speed (m/s)
    dt : float - Time step (s)
    steps : int - Number of time steps

    Returns:
    positions : np.array - Final positions of particles after dispersion
    """
    positions = np.zeros((steps, 3))
    positions[0] = [x, y, z]

    for t in range(1, steps):
        positions[t, 0] = positions[t-1, 0] + u * dt  # X-direction (wind)
        positions[t, 1] = positions[t-1, 1] + np.random.randn() * dt  # Y-direction (random spread)
        positions[t, 2] = positions[t-1, 2] + np.random.randn() * dt  # Z-direction (random spread)
    
    return positions
