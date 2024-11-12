# visualizations/3d_visualization.py

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from core.gaussian_puff import GaussianPuffModel

def visualize_3d_dispersion(Qm, u, Kx, Ky, Kz, time):
    """
    Real-time 3D visualization for puff with wind.
    Parameters:
        Qm : float : Mass release rate
        u : float : Wind speed
        Kx, Ky, Kz : float : Eddy diffusivities in x, y, z directions
        time : float : Time after release
    """
    x = np.linspace(-50, 50, 100)
    y = np.linspace(-50, 50, 100)
    X, Y = np.meshgrid(x, y)
    Z = GaussianPuffModel.puff_with_wind(Qm, u, Kx, Ky, Kz, X, Y, 0, time)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('X Distance')
    ax.set_ylabel('Y Distance')
    ax.set_zlabel('Concentration')
    plt.title("3D Dispersion Visualization")
    plt.show()
