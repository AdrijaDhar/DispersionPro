import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from DispersionPro.core.cfd_model import cfd_dispersion_simulation

def visualize_cfd(grid_size, emission_rate, wind_speed, diffusion_coeff, time_steps, dt):
    """
    Visualize the 3D pollutant dispersion using the CFD model.

    Parameters:
    grid_size : tuple - (nx, ny, nz), dimensions of the 3D grid
    emission_rate : float - Pollutant emission rate (g/s)
    wind_speed : tuple - Wind speed in x, y, z directions
    diffusion_coeff : float - Diffusion coefficient (m^2/s)
    time_steps : int - Number of time steps for the simulation
    dt : float - Time step size

    Returns:
    None - Displays 3D visualization.
    """
    grid = cfd_dispersion_simulation(grid_size, emission_rate, wind_speed, diffusion_coeff, time_steps, dt)

    nx, ny, nz = grid_size
    x = np.arange(nx)
    y = np.arange(ny)
    z = np.arange(nz)
    
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Visualize the concentration at a certain plane (e.g., z=nx//2)
    ax.scatter(X[:, :, nz//2], Y[:, :, nz//2], grid[:, :, nz//2], c=grid[:, :, nz//2], cmap="coolwarm")
    
    ax.set_xlabel("X (downwind)")
    ax.set_ylabel("Y (crosswind)")
    ax.set_zlabel("Concentration (g/m^3)")
    plt.title("CFD Dispersion Model Visualization")
    plt.show()
