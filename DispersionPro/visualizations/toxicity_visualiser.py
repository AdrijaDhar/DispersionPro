# visualizations/toxicity_visualization.py

import matplotlib.pyplot as plt
import numpy as np

def generate_toxicity_heatmap(concentration_grid, threshold):
    """
    Generates a heatmap highlighting areas where concentration exceeds the threshold.

    Parameters:
    concentration_grid: np.array - 2D array of concentration values.
    threshold: float - Toxic concentration threshold.

    Returns:
    fig: matplotlib.figure.Figure - The generated heatmap figure.
    """
    exceedance = concentration_grid > threshold
    plt.figure(figsize=(8, 6))
    plt.imshow(exceedance, cmap='Reds', origin='lower')
    plt.colorbar(label='Exceeds Threshold')
    plt.title('Toxicity Threshold Exceedance Heatmap')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    fig = plt.gcf()
    return fig
