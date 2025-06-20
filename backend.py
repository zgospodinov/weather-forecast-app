import requests
from dotenv import load_dotenv
import os

def get_data(city, forecast_days=None):
    load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))

    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get('cod') != '200':
            return None
        number_values = 8 * int(forecast_days) if forecast_days is not None else 40
        filtered_data = data['list'][:number_values]
        return filtered_data
    except Exception:
        return None


if __name__ == "__main__":

    # Example usage of the get_data function
    data = get_data("Varna", 2)
    print(data)