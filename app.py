import os
from flask import Flask, render_template
from forms import WeatherForm
import requests

API_KEY = os.environ.get("API_KEY")

def get_data(city):

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"

    status_code = requests.get(url).status_code

    if status_code == 200:
        data = requests.get(url).json()
        required_info = {
            'time': data['location']['localtime'],
            'city': data['location']['name'],
            'country': data['location']['country'],
            'temp': data['current']['temp_c'],
            'weather': data['current']['condition']['text'],
            'icon': data['current']['condition']['icon'],
        }
    if status_code == 400:
        data = requests.get(url).json()
        required_info = {
            'error': data['error']['message']
        }
    return required_info



app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'

@app.route('/' , methods=['GET', 'POST'])
def home():
    form = WeatherForm()
    city = form.city.data
    data = get_data('Chennai')
    if form.validate_on_submit():
        data = get_data(city)

    return render_template('index.html', form=form, data=data)


if __name__ == '__main__':
    app.run(debug=True)