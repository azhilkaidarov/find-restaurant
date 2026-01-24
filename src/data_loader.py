import os
import googlemaps
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAP_API_KEY")
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)


def fetch_restaurant(
    lat: float, lon: float, radius: float, keyword: str = "restaurant"
) -> pd.DataFrame:
    try:
        results = gmaps.places_nearby(
            location=(lat, lon),
            radius=radius,
            keyword=keyword,
            type="restaurant"
        )
    except Exception as e:
        print(f"Error - : {e}")

    places = results.get("results", [])

    df = pd.json_normalize(places)
    if df.empty:
        raise ValueError("data_loader/fetch_restaurant(), no result with such params.")

    columns = {
        "name": "name",
        "geometry.location.lat": "lat",
        "geometry.location.lng": "lon",
        "rating": "rating",
        "user_ratings_total": "review_count",
        "price_level": "price_level",
        "vicinity": "address",
        "opening_hours.open_now": "is_open"
    }
    df = df.rename(columns=columns)
    available_cols = [c for c in columns.values() if c in df.columns]

    return df[available_cols]
