from geopy.geocoders import Nominatim
from geopy import distance

GEOLOCATOR = Nominatim(user_agent="my_unique_find_restaurant_app_v1", timeout=10)


def get_coordinates(address: str) -> tuple[float, float]:
    location = GEOLOCATOR.geocode(address, timeout=10)
    if location is None:
        raise ValueError(f"Address not found: {address}")
    return (location.latitude, location.longitude)


def get_distance(user_coord: tuple[float, float], org_coord: tuple[float, float]):
    if not user_coord or not org_coord:
        raise ValueError("geo-utils.py, get_distance(), params error.")
    return round(distance.distance(user_coord, org_coord).miles, 2)
