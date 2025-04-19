import requests

'''Display current weather'''
def weather():
    url = "http://api.weatherstack.com/current?access_key=69e737841f87cb8f7d29fcd5ab0a0bf3&query=Mumbai"
    response = requests.get(url)
    data = response.json()
    if data:
        location = data['location']['name']
        temperature = data['current']['temperature']
        weather_description = data['current']['weather_descriptions'][0]
        sunrise = data['current']['astro']['sunrise']
        sunset = data['current']['astro']['sunset']
        humidity = data['current']['humidity']
        feels_like = data['current']['feelslike']
        wind_speed = data['current']['wind_speed']
        print(f"Current weather in {location}:\n{temperature}°C but feels like {feels_like}°C\nIt is {weather_description}today\nHumidity: {humidity}%\nWind Speed: {wind_speed} km/h\nSunrise: {sunrise}\nSunset: {sunset}")
    else:
        print("Unable to fetch weather data. Please try again.")
