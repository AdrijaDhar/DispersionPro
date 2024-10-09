# ui/3d_visualization.py

from flask import render_template
from DispersionPro.visualizations.real_time_3d_visualizer import generate_3d_visualization

def display_3d_visualization(params):
    """
    Generates and displays a 3D visualization based on input parameters.

    Parameters:
    params: dict - Dictionary of input parameters.

    Returns:
    Rendered HTML page with embedded 3D plot.
    """
    fig = generate_3d_visualization(**params)
    graph_json = fig.to_json()
    return render_template('3d_visualization.html', graph_json=graph_json)
