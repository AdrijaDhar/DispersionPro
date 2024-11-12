# visualizations/toxicity_visualiser.py

import numpy as np
import matplotlib.pyplot as plt

def toxicity_visualization(concentration_data, toxicity_threshold):
    """
    Visualize areas where concentration exceeds toxicity threshold.
    Parameters:
        concentration_data : np.array : Concentration data array
        toxicity_threshold : float : Threshold concentration for toxicity
    """
    toxic_areas = concentration_data > toxicity_threshold

    plt.imshow(toxic_areas, cmap='Reds', interpolation='nearest')
    plt.colorbar(label="Toxicity")
    plt.title("Toxic Areas")
    plt.show()
