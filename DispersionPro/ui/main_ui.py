from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from DispersionPro.visualizations.contour_plots import generate_contour_plot

class DispersionProApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setWindowTitle('DispersionPro')

        self.q_input = QLineEdit(self)
        self.q_input.setPlaceholderText('Emission rate (g/s)')
        layout.addWidget(QLabel('Emission Rate (g/s):'))
        layout.addWidget(self.q_input)

        self.u_input = QLineEdit(self)
        self.u_input.setPlaceholderText('Wind speed (m/s)')
        layout.addWidget(QLabel('Wind Speed (m/s):'))
        layout.addWidget(self.u_input)

        self.visualize_button = QPushButton('Generate Visualization', self)
        self.visualize_button.clicked.connect(self.visualize_dispersion)
        layout.addWidget(self.visualize_button)

        self.setLayout(layout)

    def visualize_dispersion(self):
        q = float(self.q_input.text())
        u = float(self.u_input.text())

        generate_contour_plot(Q=q, u=u, H=50, x_range=500, y_range=100, sigma_y=30, sigma_z=10)

if __name__ == '__main__':
    app = QApplication([])
    ex = DispersionProApp()
    ex.show()
    app.exec_()
