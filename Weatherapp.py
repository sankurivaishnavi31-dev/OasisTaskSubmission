import requests

def get_coordinates(city_name):
    """Get latitude and longitude of the city"""
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}"
    response = requests.get(geo_url)
    data = response.json()

    if "results" in data:
        latitude = data["results"][0]["latitude"]
        longitude = data["results"][0]["longitude"]
        return latitude, longitude
    else:
        return None, None

def get_weather(latitude, longitude):
    """Get current weather using Open-Meteo API"""
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(weather_url)
    data = response.json()

    if 'current_weather' in data:
        weather = data['current_weather']
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Windspeed: {weather['windspeed']} km/h")
        print(f"Weather code: {weather['weathercode']}")
    else:
        print("Weather data not available.")

def main():
    city = input("Enter city name: ")
    latitude, longitude = get_coordinates(city)
    
    if latitude and longitude:
        print(f"{city} => Latitude: {latitude}, Longitude: {longitude}")
        get_weather(latitude, longitude)
    else:
        print("City not found!")

if __name__ == "__main__":
    main()
