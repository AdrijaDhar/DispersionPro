# ui/inputs_form.py

from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired

class DispersionInputForm(FlaskForm):
    Q = FloatField('Emission Rate (g/s)', validators=[DataRequired()])
    u = FloatField('Wind Speed (m/s)', validators=[DataRequired()])
    x = FloatField('Downwind Distance (m)', validators=[DataRequired()])
    y = FloatField('Crosswind Distance (m)', validators=[DataRequired()])
    z = FloatField('Height Above Ground (m)', validators=[DataRequired()])
    H = FloatField('Effective Stack Height (m)', validators=[DataRequired()])
    stability_class = SelectField('Stability Class', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')])
    gas_density = FloatField('Gas Density (kg/m^3)', validators=[DataRequired()])
    inversion_present = BooleanField('Inversion Layer Present')
    submit = SubmitField('Calculate')
