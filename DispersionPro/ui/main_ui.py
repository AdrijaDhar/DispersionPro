# ui/main_ui.py

from core.edge_case_handler import EdgeCaseHandler
from ui.results_display import display_results
import numpy as np

def main():
    # Collect basic inputs
    input_data = {
        'Qm': float(input("Enter mass release rate (Qm): ")),
        'K': float(input("Enter eddy diffusivity (K): ")),
        'r': float(input("Enter distance from source (r): ")),
        'wind': float(input("Enter wind speed (0 for no wind): ")),
        'continuous': input("Is it a continuous release? (yes/no): ").lower() == 'yes',
        'puff': input("Is it a puff release? (yes/no): ").lower() == 'yes',
        't': float(input("Enter time since release (for non-steady states): ")),
        'toxicity_threshold': float(input("Enter toxicity threshold: ")),
        'wind_direction': float(input("Enter wind direction (in degrees): "))
    }

    # Determine model and calculate concentration
    handler = EdgeCaseHandler()
    concentration = handler.select_model(input_data)

    # Generate sample concentration data grid for visualization
    concentration_data = np.full((100, 100), concentration)  # Simplified example
    terrain_data = np.random.rand(100, 100) * 10  # Random terrain elevation data for example

    # Display results based on user's choice of visualization
    display_results(concentration_data, terrain_data, input_data['toxicity_threshold'], input_data['wind'], input_data['wind_direction'])

if __name__ == "__main__":
    main()
