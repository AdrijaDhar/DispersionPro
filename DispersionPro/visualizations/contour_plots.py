# visualizations/contour_plots.py

import matplotlib.pyplot as plt
import numpy as np

def generate_contour_plot(data, x_vals, y_vals, title="Dispersion Contour Plot"):
    """
    Generates a contour plot with improved scaling and color contrast.
    Includes dynamic level adjustment to better display dispersion patterns.

    Parameters:
        data (np.array): 2D array of concentration values.
        x_vals (np.array): 1D array of x-axis (downwind) values.
        y_vals (np.array): 1D array of y-axis (crosswind) values.
        title (str): Title of the plot.
    """
    # Replace NaNs in data with zero
    data = np.nan_to_num(data, nan=0.0)

    # Print data range for debugging
    print("Data Min:", np.min(data))
    print("Data Max:", np.max(data))

    plt.figure(figsize=(10, 6))
    
    # Define contour levels to capture subtle variations
    min_val, max_val = np.min(data), np.max(data)
    contour_levels = np.linspace(min_val, max_val, 100) if max_val > min_val else np.linspace(0, 1, 100)

    # Log scale if data has a wide range, using a small offset to avoid -inf
    if min_val > 0:
        plt.contourf(x_vals, y_vals, np.log10(data + 1e-10), levels=contour_levels, cmap='plasma')
        plt.colorbar(label="Log10(Concentration)")
    else:
        plt.contourf(x_vals, y_vals, data, levels=contour_levels, cmap='plasma')
        plt.colorbar(label="Concentration")

    # Set titles and labels
    plt.title(title)
    plt.xlabel("Downwind Distance (m)")
    plt.ylabel("Crosswind Distance (m)")

    # Show grid and adjust layout
    plt.grid(visible=True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    
    # Show the plot
    plt.show()
