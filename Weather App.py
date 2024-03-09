import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    print(data)  # Print the entire response data for debugging

    if data["cod"] != 401:
        main_data = data["main"]
        weather_data = data["weather"][0]
        wind_data = data["wind"]

        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        weather_description = weather_data["description"]
        wind_speed = wind_data["speed"]

        print(f"Weather in {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {weather_description}")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Invalid API key. Please check your API key and try again.")

if __name__ == "__main__":
    api_key = "4153e38aac1f7e63ba0421e1ad13af7e"
    location = input("Enter city name: ")
    get_weather(api_key, location)
