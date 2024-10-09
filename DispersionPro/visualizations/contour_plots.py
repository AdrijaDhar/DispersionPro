import matplotlib.pyplot as plt
import numpy as np
from DispersionPro.core.gaussian_plume import gaussian_plume

def generate_contour_plot(Q, u, H, x_range, y_range, sigma_y, sigma_z):
    x_vals = np.linspace(0, x_range, 100)
    y_vals = np.linspace(-y_range, y_range, 100)
    
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = gaussian_plume(Q, u, X, Y, 0, H, sigma_y, sigma_z)
    
    plt.contourf(X, Y, Z, cmap="coolwarm")
    plt.colorbar(label="Concentration (g/m^3)")
    plt.title("Gaussian Plume Dispersion")
    plt.xlabel("Distance Downwind (m)")
    plt.ylabel("Crosswind Distance (m)")
    plt.show()
