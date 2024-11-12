# main.py
import os
import matplotlib.pyplot as plt

import numpy as np
from core.gaussian_plume import GaussianPlumeModel
from core.gaussian_puff import GaussianPuffModel
from core.cfd_model import CFDModel
from core.pasquill_gifford import PasquillGiffordModel
from core.aermod import AERMODModel
from visualizations.contour_plots import generate_contour_plot
from visualizations.terrain_integration import modify_dispersion_for_terrain
from visualizations.weather_integration import adjust_dispersion_for_weather
from visualizations.toxicity_visualiser import toxicity_visualization
from visualizations.time_series_animation import animate_dispersion

def get_user_input():
    # Collect general user input for dispersion parameters
    test_name = input("Enter a unique name for this test (e.g., 'GaussianPlumeTest1'): ")
    Qm = float(input("Enter the emission rate (Qm, e.g., 5.0 g/s): "))
    u = float(input("Enter the wind speed (u, e.g., 2.0 m/s): "))
    model_type = input("Enter the model type (plume/puff/cfd/aermod/pasquill): ").strip().lower()
    x_max = float(input("Enter the maximum downwind distance (x_max, e.g., 100 m): "))
    y_max = float(input("Enter the maximum crosswind distance (y_max, e.g., 50 m): "))
    z = float(input("Enter the height above ground (z, e.g., 1.5 m): "))
    additional_inputs = {}

    # Collect additional inputs based on the model type
    if model_type == "plume":
        additional_inputs['H'] = float(input("Enter the effective stack height (H, e.g., 20 m): "))
        additional_inputs['stability_class'] = input("Enter the stability class (A-F, e.g., D): ").strip().upper()
    elif model_type == "puff":
        additional_inputs['t'] = float(input("Enter the time since release (t, e.g., 10 s): "))
    elif model_type == "cfd":
        additional_inputs['D'] = float(input("Enter the diffusion coefficient (D, e.g., 0.1 m^2/s): "))
        additional_inputs['t'] = float(input("Enter the time since release (t, e.g., 10 s): "))
    elif model_type == "aermod":
        additional_inputs['stability_class'] = input("Enter the stability class (A-F, e.g., D): ").strip().upper()
        if model_type == "aermod":
            additional_inputs['roughness_length'] = float(input("Enter the roughness length (e.g., 0.1 m): "))
    elif model_type == "pasquill":
        additional_inputs['stability_class'] = input("Enter the stability class (A-F, e.g., D): ").strip().upper()
        
    # Visualization and modification options
    modify_terrain = input("Would you like to adjust for terrain effects? (yes/no): ").strip().lower() == 'yes'
    adjust_for_weather = input("Would you like to adjust for real-time weather effects? (yes/no): ").strip().lower() == 'yes'
    visualize_toxicity = input("Would you like to visualize toxicity threshold? (yes/no): ").strip().lower() == 'yes'
    if visualize_toxicity:
        additional_inputs['toxicity_threshold'] = float(input("Enter the toxicity threshold (e.g., 0.5): "))
    
    # Return all collected inputs, including the test name
    return {
        "test_name": test_name, 
        "Qm": Qm, 
        "u": u, 
        "model_type": model_type, 
        "x_max": x_max, 
        "y_max": y_max, 
        "z": z, 
        "additional_inputs": additional_inputs, 
        "modify_terrain": modify_terrain,
        "adjust_for_weather": adjust_for_weather, 
        "visualize_toxicity": visualize_toxicity
    }


def calculate_concentration_grid(input_data):
    model_type = input_data["model_type"]
    Qm = input_data["Qm"]
    u = input_data["u"]
    x_max = input_data["x_max"]
    y_max = input_data["y_max"]
    z = input_data["z"]
    additional_inputs = input_data["additional_inputs"]

    x_vals = np.linspace(0, x_max, 100)
    y_vals = np.linspace(-y_max, y_max, 100)
    concentration_grid = np.zeros((len(y_vals), len(x_vals)))
    
    # Model-specific calculations
    if model_type == "plume":
        for i, x in enumerate(x_vals):
            sigma_y, sigma_z = GaussianPlumeModel.calculate_dispersion_coefficients(x, additional_inputs['stability_class'])
            for j, y in enumerate(y_vals):
                concentration_grid[j, i] = GaussianPlumeModel.gaussian_plume_concentration(
                    Q=Qm, u=u, x=x, y=y, z=z, H=additional_inputs['H'], sigma_y=sigma_y, sigma_z=sigma_z
                )
        title = "Gaussian Plume Model - Steady State Dispersion"
        
    elif model_type == "puff":
        for i, x in enumerate(x_vals):
            for j, y in enumerate(y_vals):
                r = np.sqrt(x**2 + y**2)
                concentration_grid[j, i] = GaussianPuffModel.puff_no_wind(Qm=Qm, K=0.1, r=r, t=additional_inputs['t'])
        title = "Gaussian Puff Model - Instantaneous Release Dispersion"
        
    elif model_type == "cfd":
        for i, x in enumerate(x_vals):
            for j, y in enumerate(y_vals):
                concentration_grid[j, i] = CFDModel.calculate_concentration_cfd(
                    Qm=Qm, u=u, D=additional_inputs['D'], x=x, y=y, t=additional_inputs['t']
                )
        title = "CFD Model - Diffusion with Wind"
        
    elif model_type == "aermod":
        for i, x in enumerate(x_vals):
            for j, y in enumerate(y_vals):
                concentration_grid[j, i] = AERMODModel.aermod_concentration(
                    Qm=Qm, u=u, z=z, stability_class=additional_inputs['stability_class'], roughness_length=additional_inputs['roughness_length']
                )
        title = "AERMOD Model - Terrain and Stability Adjusted"
        
    elif model_type == "pasquill":
        for i, x in enumerate(x_vals):
            for j, y in enumerate(y_vals):
                concentration_grid[j, i] = PasquillGiffordModel.pasquill_gifford_concentration(
                    Qm=Qm, u=u, x=x, y=y, z=z, stability_class=additional_inputs['stability_class']
                )
        title = "Pasquill-Gifford Model - Stability Class Based Dispersion"
    
    return x_vals, y_vals, concentration_grid, title

def apply_modifications(input_data, concentration_grid, x_vals, y_vals):
    # Terrain adjustment
    if input_data["modify_terrain"]:
        terrain_data = np.random.rand(len(y_vals), len(x_vals)) * 10  # Simulated terrain data
        concentration_grid = modify_dispersion_for_terrain(concentration_grid, terrain_data)
    
    # Weather adjustment
    if input_data["adjust_for_weather"]:
        wind_direction = float(input("Enter the wind direction in degrees (0-360): "))
        concentration_grid = adjust_dispersion_for_weather(concentration_grid, input_data["u"], wind_direction)
    
    # Toxicity visualization
    if input_data["visualize_toxicity"]:
        toxicity_visualization(concentration_grid, input_data["additional_inputs"].get("toxicity_threshold", 0.5))

    return concentration_grid
def save_test_inputs(folder_path, input_data):
    """Save input parameters to a text file."""
    with open(os.path.join(folder_path, "input_parameters.txt"), "w") as f:
        for key, value in input_data.items():
            f.write(f"{key}: {value}\n")
def main():
    # Collect user input
    input_data = get_user_input()
    
    # Create a folder for this test
    folder_path = os.path.join("test_results", input_data["test_name"])
    os.makedirs(folder_path, exist_ok=True)

    
    # Save the input parameters
    save_test_inputs(folder_path, input_data)

    
    # Calculate the concentration grid
    x_vals, y_vals, concentration_grid, title = calculate_concentration_grid(input_data)
    
    # Apply any modifications for terrain, weather, or toxicity
    concentration_grid = apply_modifications(input_data, concentration_grid, x_vals, y_vals)
    
    # Generate and save the contour plot
    plt.figure()
    generate_contour_plot(data=concentration_grid, x_vals=x_vals, y_vals=y_vals, title=title)
    plt.savefig(os.path.join(folder_path, "dispersion_plot.png"))

    plt.close()

    # Optionally animate dispersion over time if requested
    if input("Would you like to animate the dispersion over time? (yes/no): ").strip().lower() == 'yes':
        animate_dispersion(Qm=input_data["Qm"], K=0.1, max_distance=input_data["x_max"])
        plt.savefig(os.path.join(folder_path, "dispersion_animation.png"))
        plt.close()

if __name__ == "__main__":
    main()