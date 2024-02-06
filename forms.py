from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class WeatherForm(FlaskForm):
    city = StringField('city', validators=[DataRequired()],  render_kw={"placeholder": "Enter city name"})
    add_city = SubmitField('Get Weather')