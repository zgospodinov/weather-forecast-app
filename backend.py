import requests
from dotenv import load_dotenv
import os

def get_data(city, forecast_days=None, kind=None):
    load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))

    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    
    response = requests.get(url)
    data = response.json()
    number_values = 8 * int(forecast_days) if forecast_days != None else 40
    filtered_data = data['list'][:number_values]

    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]

    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]

    return filtered_data


if __name__ == "__main__":

    # Example usage of the get_data function    
    data = get_data("Varna", 2, "Sky")
    print(data)