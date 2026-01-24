import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

FOURSQUARE_API_KEY = os.getenv("FOURSQUARE_API_KEY")
BASE_URL = "https://api.foursquare.com/v3/places/search"


def fetch_restaurant(lat: float, lon: float, radius: int = 1000, limit: int = 50) -> pd.DataFrame:
    headers = {
        "accept": "application/json",
        "Authorization": FOURSQUARE_API_KEY
    }
    params = {
        "ll": f"{lat},{lon}",
        "radius": radius,
        "categories": "13065",
        "limit": limit
    }
    response = requests.get(url=BASE_URL, headers=headers, params=params)

    print("Result = ", response.text)
    # Не заработало


def load_restaurant(filepath: str = "data/restaurant.csv") -> pd.DataFrame:
    return pd.read_csv(filepath)


def main():
    pass


if __name__ == "__main__":
    main()
