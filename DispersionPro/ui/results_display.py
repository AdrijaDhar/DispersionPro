# ui/results_display.py

from flask import render_template

def display_results(concentration):
    """
    Renders the results page with the calculated concentration.

    Parameters:
    concentration: float - The calculated pollutant concentration.

    Returns:
    Rendered HTML page.
    """
    return render_template('results.html', concentration=concentration)
