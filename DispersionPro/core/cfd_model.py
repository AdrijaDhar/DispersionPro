import numpy as np

def cfd_dispersion_simulation(grid_size, emission_rate, wind_speed, diffusion_coeff, time_steps, dt):
    """
    Perform a basic CFD-inspired simulation for pollutant dispersion using finite difference approximation.

    Parameters:
    grid_size : tuple - (nx, ny, nz), dimensions of the 3D grid
    emission_rate : float - Rate of pollutant emission (g/s)
    wind_speed : tuple - (ux, uy, uz), wind speed components in x, y, z directions (m/s)
    diffusion_coeff : float - Diffusion coefficient (m^2/s)
    time_steps : int - Number of simulation steps
    dt : float - Time step (s)

    Returns:
    grid : np.array - Final pollutant concentration grid after simulation (g/m^3)
    """
    nx, ny, nz = grid_size
    grid = np.zeros((nx, ny, nz))

    emission_source = (nx // 2, ny // 2, nz // 2)
    grid[emission_source] = emission_rate

    for t in range(time_steps):
        new_grid = np.copy(grid)
        for i in range(1, nx-1):
            for j in range(1, ny-1):
                for k in range(1, nz-1):
                    advection_x = wind_speed[0] * (grid[i+1, j, k] - grid[i-1, j, k]) / (2 * dt)
                    advection_y = wind_speed[1] * (grid[i, j+1, k] - grid[i, j-1, k]) / (2 * dt)
                    advection_z = wind_speed[2] * (grid[i, j, k+1] - grid[i, j, k-1]) / (2 * dt)

                    diffusion_x = diffusion_coeff * (grid[i+1, j, k] - 2 * grid[i, j, k] + grid[i-1, j, k]) / dt**2
                    diffusion_y = diffusion_coeff * (grid[i, j+1, k] - 2 * grid[i, j, k] + grid[i, j-1, k]) / dt**2
                    diffusion_z = diffusion_coeff * (grid[i, j, k+1] - 2 * grid[i, j, k] + grid[i, j, k-1]) / dt**2

                    new_grid[i, j, k] = grid[i, j, k] + dt * (advection_x + advection_y + advection_z + diffusion_x + diffusion_y + diffusion_z)

        grid = new_grid

    return grid
