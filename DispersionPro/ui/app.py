# ui/app.py

from core.edge_case_handler import EdgeCaseHandler
from visualizations.contour_plots import generate_contour_plot
import numpy as np

def main():
    # Collect user input
    input_data = {
        'Qm': float(input("Enter mass release rate (Qm): ")),
        'K': float(input("Enter eddy diffusivity (K): ")),
        'r': float(input("Enter distance from source (r): ")),
        'wind': float(input("Enter wind speed (0 for no wind): ")),
        'continuous': input("Is it a continuous release? (yes/no): ").lower() == 'yes',
        'puff': input("Is it a puff release? (yes/no): ").lower() == 'yes',
        't': float(input("Enter time since release (for non-steady states): ")),
        'x': float(input("Enter x-coordinate: ")),
        'y': float(input("Enter y-coordinate: ")),
        'z': float(input("Enter z-coordinate: ")),
        'Kx': float(input("Enter eddy diffusivity in x direction (Kx): ")),
        'Ky': float(input("Enter eddy diffusivity in y direction (Ky): ")),
        'Kz': float(input("Enter eddy diffusivity in z direction (Kz): ")),
    }

    # Determine model and calculate concentration
    handler = EdgeCaseHandler()
    concentration = handler.select_model(input_data)

    # Generate contour plot
    x_vals = np.linspace(0, 100, 100)  # Example x-axis range
    y_vals = np.linspace(0, 100, 100)  # Example y-axis range
    data = np.array([[concentration for _ in x_vals] for _ in y_vals])  # Simplified data generation

    generate_contour_plot(data, x_vals, y_vals, title="Generated Concentration Contour")

if __name__ == "__main__":
    main()
