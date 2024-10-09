# visualizations/terrain_integration.py

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from osgeo import gdal

def integrate_terrain(elevation_data_path):
    """
    Reads terrain elevation data and returns arrays for plotting.

    Parameters:
    elevation_data_path: str - Path to the DEM file.

    Returns:
    X, Y, Z: np.array - Arrays representing terrain elevation.
    """
    ds = gdal.Open(elevation_data_path)
    band = ds.GetRasterBand(1)
    elevation = band.ReadAsArray()
    xsize = ds.RasterXSize
    ysize = ds.RasterYSize
    x = np.linspace(0, xsize, xsize)
    y = np.linspace(0, ysize, ysize)
    X, Y = np.meshgrid(x, y)
    Z = elevation
    return X, Y, Z

def plot_terrain(X, Y, Z):
    """
    Plots the terrain elevation data.

    Parameters:
    X, Y, Z: np.array - Terrain data arrays.

    Returns:
    fig: matplotlib.figure.Figure - The generated terrain figure.
    """
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='terrain')
    ax.set_title('Terrain Elevation')
    return fig
