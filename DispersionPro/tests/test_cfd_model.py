import unittest
import numpy as np
from DispersionPro.core.cfd_model import cfd_dispersion_simulation

class TestCFDModel(unittest.TestCase):
    def test_cfd_simulation(self):
        grid_size = (10, 10, 10)  # 3D grid size
        emission_rate = 100       # Emission rate
        wind_speed = (5, 0, 0)    # Wind in x-direction
        diffusion_coeff = 0.1     # Diffusion coefficient
        time_steps = 10           # Number of simulation steps
        dt = 0.01                 # Time step duration

        # Simulate the CFD model
        grid = cfd_dispersion_simulation(grid_size, emission_rate, wind_speed, diffusion_coeff, time_steps, dt)
        self.assertEqual(grid.shape, grid_size)  # Ensure grid size is correct

if __name__ == '__main__':
    unittest.main()
