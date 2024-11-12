# ui/results_display.py

from visualizations.contour_plots import generate_contour_plot
from visualizations.toxicity_visualiser import toxicity_visualization
from visualizations.terrain_integration import modify_dispersion_for_terrain
from visualizations.weather_integration import adjust_dispersion_for_weather
from visualizations.time_series_animation import animate_dispersion

def display_results(concentration_data, terrain_data, toxicity_threshold, wind_speed, wind_direction):
    print("Choose visualization type:")
    print("1. Contour Plot")
    print("2. Toxicity Map")
    print("3. Terrain Adjusted Plot")
    print("4. Weather Adjusted Plot")
    print("5. Time Series Animation")

    choice = int(input("Enter choice: "))

    if choice == 1:
        generate_contour_plot(concentration_data, range(concentration_data.shape[0]), range(concentration_data.shape[1]))
    elif choice == 2:
        toxicity_visualization(concentration_data, toxicity_threshold)
    elif choice == 3:
        adjusted_data = modify_dispersion_for_terrain(concentration_data, terrain_data)
        generate_contour_plot(adjusted_data, range(adjusted_data.shape[0]), range(adjusted_data.shape[1]), title="Terrain Adjusted Plot")
    elif choice == 4:
        adjusted_data = adjust_dispersion_for_weather(concentration_data, wind_speed, wind_direction)
        generate_contour_plot(adjusted_data, range(adjusted_data.shape[0]), range(adjusted_data.shape[1]), title="Weather Adjusted Plot")
    elif choice == 5:
        animate_dispersion(Qm=1.0, K=0.1)  # Example parameters for animation
    else:
        print("Invalid choice")
