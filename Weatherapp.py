import requests

# Step 1: Ask the user for the city name
city = input("Enter city name: ")

# Step 2: Define your API key and URL
api_key = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Step 3: Send a GET request
response = requests.get(url)

# Step 4: Process the JSON response
if response.status_code == 200:
    data = response.json()
    main = data['main']
    weather = data['weather'][0]
    
    temperature = main['temp']
    humidity = main['humidity']
    condition = weather['description']

    print(f"\nWeather in {city.title()}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition.capitalize()}")
else:
    print("\nCity not found or API request failed.")
