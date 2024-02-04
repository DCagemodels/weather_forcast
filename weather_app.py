import requests

def get_weather(city, api_key):
    web_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=13cbf0b17a35101ca9bbee33cfc52a60&units=metric"
    response = requests.get(web_url)
    data = response.json()
    return data

def display_weather(weather_data):
    if weather_data["cod"] == 200:
        city_name = weather_data["name"]
        temp_c = weather_data["main"]["temp"]
        temp_f = celsius_to_fahrenheit(temp_c)
        humidity = weather_data["main"]["humidity"]
        weather_condition = weather_data["weather"][0]["description"]
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temp_c}°C ({temp_f}°F)")
        print(f"Humidity: {humidity}%")
        print(f"Weather Condition: {weather_condition}")
    else:
        print("City not found.")
        
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
    
    
def main():
    city_input = input("Enter the city name ")
    api_key = "13cbf0b17a35101ca9bbee33cfc52a60"
    weather_data = get_weather(city_input, api_key)
    display_weather(weather_data)
    
if __name__ == "__main__":
    main()
    
    