import requests


def get_weather(city):
    geocode_url = "https://geocoding-api.open-meteo.com/v1/search"

    geocode_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(
        geocode_url,
        params=geocode_params,
        timeout=10
    )

    data = response.json()

    if "results" not in data:
        return {
            "error": f"City '{city}' not found."
        }

    location = data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m",
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh"
    }

    weather_response = requests.get(
        weather_url,
        params=weather_params,
        timeout=10
    )

    weather_data = weather_response.json()

    current = weather_data["current"]

    return {
        "city": location["name"],
        "country": location.get("country", ""),
        "temperature": current["temperature_2m"],
        "feels_like": current["apparent_temperature"],
        "humidity": current["relative_humidity_2m"],
        "precipitation": current["precipitation"],
        "wind_speed": current["wind_speed_10m"],
        "weather_code": current["weather_code"],
        "time": current["time"]
    }