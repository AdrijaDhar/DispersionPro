# DispersionPro

### A comprehensive air pollutant dispersion modeling software featuring Gaussian Plume, Puff, CFD simulations, and advanced visualizations.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Visualization](#visualization)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction
**DispersionPro** is an advanced software designed for environmental scientists, engineers, and researchers to simulate the dispersion of pollutants in the atmosphere. The software supports multiple dispersion models like Gaussian Plume, Puff models, and CFD-based simulations, offering real-time 2D/3D visualizations and an easy-to-use interface.

## Features
- **Gaussian Plume Model**: Simulate pollutant dispersion from continuous point sources.
- **Gaussian Puff Model**: Model instantaneous releases and dispersion over time.
- **CFD Simulations**: Perform computational fluid dynamics (CFD) simulations for more complex cases.
- **Real-Time Visualizations**: 2D contour plots and 3D visualizations of pollutant dispersion.
- **API Access**: Expose the core models via REST APIs for programmatic interaction.
- **Cloud-Ready**: Deploy the software on cloud platforms using Docker.

## Technologies Used
- Python 3.8+
- Flask (for API)
- PyQt5 (for desktop UI)
- Matplotlib, Plotly (for visualizations)
- NumPy (for numerical computation)
- Docker (for deployment)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DispersionPro.git
   cd DispersionPro
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
4. To start the desktop application:
    ```bash

    python DispersionPro/ui/main_ui.py
5. To start the web-based Flask application:
    ```bash
    Copy code
    python DispersionPro/api/api_endpoints.py
### Usage

6. Using the Desktop UI:
Input the emission rate, wind speed, and stack height.
Click the "Generate Visualization" button to visualize pollutant dispersion.
View real-time 2D contour plots of the dispersion.
7. Using the API:
POST requests can be made to endpoints like /api/gaussian_plume and /api/gaussian_puff to calculate pollutant concentrations programmatically.
Example API call:
    ```bash
    curl -X POST http://localhost:5000/api/gaussian_plume \
        -H "Content-Type: application/json" \
        -d '{"Q": 100, "u": 5, "x": 100, "y": 0, "z": 0, "H": 50, "sigma_y": 30, "sigma_z": 10}'
8. API Documentation

/api/gaussian_plume: Calculates pollutant concentration using the Gaussian Plume Model.
/api/gaussian_puff: Calculates pollutant concentration using the Gaussian Puff Model.
Make sure to pass the required parameters in JSON format when making requests.

9. Visualization

2D Contour Plots: Shows pollutant concentration levels in real time.
3D Visualizations: Visualize complex CFD simulations for pollutant dispersions.
Testing

10. To run unit tests for the core models and API:
    ```bash

    python -m unittest discover DispersionPro/tests/`
