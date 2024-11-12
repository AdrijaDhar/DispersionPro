# visualizations/time_series_animation.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from core.briggs_plume import BriggsPlumeModel

def animate_dispersion(Qm, K, max_distance=100, duration=10):
    """
    Generate a time series animation of dispersion.
    Parameters:
        Qm : float : Mass release rate
        K : float : Eddy diffusivity
        max_distance : int : Maximum distance for the plot
        duration : int : Duration of animation (in frames)
    """
    fig, ax = plt.subplots()
    r_values = np.linspace(1, max_distance, 100)

    def update(frame):
        t = frame + 1  # Time step
        C_values = BriggsPlumeModel.non_steady_state_no_wind(Qm, K, r_values, t)
        ax.clear()
        ax.plot(r_values, C_values, label=f'Time {t}s')
        ax.set_xlabel('Distance (r)')
        ax.set_ylabel('Concentration (C)')
        ax.set_title('Dispersion Over Time')
        ax.legend()

    ani = animation.FuncAnimation(fig, update, frames=duration, repeat=False)
    plt.show()
