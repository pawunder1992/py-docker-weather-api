import os

from load_dotenv import load_dotenv
import requests

load_dotenv()


def get_weather() -> None:
    URL = "http://api.weatherapi.com/v1/current.json"
    payload_params = {
        "q": "Paris",
        "key": os.getenv("WEATHER_API_KEY"),
    }
    result = requests.get(URL, params=payload_params)
    data = result.json()
    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['location']['localtime']} Weather: "
        f"{data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
