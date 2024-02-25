import requests

def get_weather_data(city):
    api_key = "b37e65471cf69827d915487775e8ef8b"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main_data = data["main"]
        weather_data = data["weather"][0]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        description = weather_data["description"]
        wind_speed = data["wind"]["speed"]
        return temperature, humidity, description, wind_speed
    else:
        return None

def main():
    city = input("Enter the name of a city: ")
    weather_data = get_weather_data(city)

    if weather_data:
        temperature, humidity, description, wind_speed = weather_data
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found. Please try again.")

if __name__ == "__main__":
    main()
