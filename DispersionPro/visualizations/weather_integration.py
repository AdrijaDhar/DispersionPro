# visualizations/weather_integration.py

import requests

def get_weather_data(api_key, location):
    """
    Fetches weather data from OpenWeatherMap API.

    Parameters:
    api_key: str - API key for OpenWeatherMap.
    location: str - Location query (e.g., city name).

    Returns:
    weather_data: dict - Dictionary containing weather information.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'wind_speed': data['wind']['speed'],
            'wind_direction': data['wind']['deg'],
            'temperature': data['main']['temp'],
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity']
        }
        return weather_data
    else:
        print("Failed to retrieve weather data.")
        return None
