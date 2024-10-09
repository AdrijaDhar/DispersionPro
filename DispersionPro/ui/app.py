from flask import Flask, render_template, request
from DispersionPro.visualizations.contour_plots import generate_contour_plot
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualize', methods=['POST'])
def visualize():
    # Get parameters from form
    Q = float(request.form['Q'])
    u = float(request.form['u'])
    H = float(request.form['H'])
    sigma_y = 30
    sigma_z = 10

    fig = generate_contour_plot(Q, u, H, 500, 100, sigma_y, sigma_z)

    # Convert plot to PNG image and display in web page
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    plot_data = base64.b64encode(output.getvalue()).decode('utf8')

    return render_template('visualize.html', plot_data=plot_data)

if __name__ == '__main__':
    app.run(debug=True)
