import requests

def get_weather(city, api_key):
    """
    Fetches weather information for a given city using OpenWeatherMap API.

    :param city: Name of the city to fetch weather data for.
    :param api_key: Your OpenWeatherMap API key.
    :return: A dictionary containing weather information or an error message.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'imperial'  
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather_info
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"error": f"Request error occurred: {req_err}"}
    except KeyError:
        return {"error": "Unexpected response structure from the API."}

def main():
    """
    Main function to interact with the user and display weather information.
    """
    print("Welcome to the Weather Program!")
    print("Enter City")
    city = input()  
    api_key = "d7920173570269f4c4f8d8af9c0a3f2e"  

    print("Fetching weather information...")
    weather = get_weather(city, api_key)

    if "error" in weather:
        print(f"Error: {weather['error']}")
    else:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°F")
        print(f"Description: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")

if __name__ == "__main__":
    main()
