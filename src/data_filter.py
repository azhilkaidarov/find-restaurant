import pandas as pd

from geo_utils import get_distance


def level_price_filter(df: pd.DataFrame, level_price: float) -> pd.DataFrame:
    # Google Places API doesn't provide an average bill, only price_level.
    # Returns places with price_level <= level_price.
    if df.empty or not (0 <= level_price <= 3):
        raise ValueError("data_filter/cost_filter() - check input.")

    filtered = df[df["price_level"] <= level_price]

    if filtered.empty:
        print(f"No organization found with price level <=: {level_price}")

    return filtered


def only_open_filter(df: pd.DataFrame) -> pd.DataFrame:
    # Returns only currently open places.
    if df.empty:
        raise ValueError("data_filter/isopen_filter() - check input.")

    filtered = df[df["is_open"] == True]

    if filtered.empty:
        print("No open organization found this time.")

    return filtered


def rating_filter(
    df: pd.DataFrame,
    rating: float,
    min_r: float = 0.0,
    max_r: float = 5.0
    ) -> pd.DataFrame:
    # Returns places with ratings >= params.rating .
    if df.empty or not (min_r <= rating <= max_r):
        raise ValueError("data_filter/rating_filter() - check input.")

    filtered = df[df["rating"] >= rating]

    if filtered.empty:
        print(f"No organization with rating >=: {rating}")

    return filtered


def show_distance_filter(df: pd.DataFrame, user_lat: float, user_lon: float) -> pd.DataFrame:
    # Adds a distance_ml column (miles) from the user to each place.
    df["distance_ml"] = df.apply(
        lambda row: get_distance(
            (user_lat, user_lon),
            (row["lat"], row["lon"])
        ),
        axis=1
    )

    return df


def sort_by(df: pd.DataFrame, column: str, ascending: bool = True) -> pd.DataFrame:
    # Sorts places by the selected column.
    return df.sort_values(by=column, ascending=ascending)
