import pandas as pd

from geo_utils import get_distance


def level_price_filter(df: pd.DataFrame, level_price: float) -> pd.DataFrame:
    # в GOOGLE MAPS ср. чека нет, только price level. Вернет организации с level_price <=
    if df.empty or not (0 <= level_price <= 3):
        raise ValueError("data_filter/cost_filter() - check input.")

    filtered = df[df["price_level"] <= level_price]

    if filtered.empty:
        print(f"No organization found with price level <=: {level_price}")

    return filtered


def isopen_filter(df: pd.DataFrame) -> pd.DataFrame:
    # Возвращает открытые организации
    if df.empty:
        raise ValueError("data_filter/isopen_filter() - check input.")

    filtered = df[df["is_open"] == True]

    if filtered.empty:
        print("No ioen organization found this time.")

    return filtered


def rating_filter(df: pd.DataFrame, rating: float) -> pd.DataFrame:
    # Возвращает организации с рейтингом >= min_rating
    if df.empty or not (0.0 <= rating <= 5.0):
        raise ValueError("data_filter/rating_filter() - check input.")

    filtered = df[df["rating"] >= rating]

    if filtered.empty:
        print(f"No organization with rating >=: {rating}")

    return filtered


def distance_filter(df: pd.DataFrame, lat: float, lon: float, max_dist_ml: float) -> pd.DataFrame:
    # Возвращает организации в выбранном диапазоне поиска
    if df.empty or not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
        raise ValueError("data_filter/distance_filter() - check input.")

    df = add_distance_column(df, lat, lon)
    filtered = df[df["distance_ml"] <= max_dist_ml]

    if filtered.empty:
        print(f"No organization found in: {max_dist_ml} miles")

    return filtered


def add_distance_column(df: pd.DataFrame, user_lat: float, user_lon: float) -> pd.DataFrame:
    # Добавляет к df фичу текущего расстония от юзера от организации
    df = df.copy()

    df["distance_ml"] = df.apply(
        lambda row: get_distance(
            (user_lat, user_lon),
            (row["lat"], row["lon"])
        ),
        axis=1
    )

    return df


def sort_by(df: pd.DataFrame, column: str, ascending: bool = True) -> pd.DataFrame:
    # Отсортирует организации по выбранной фиче
    return df.sort_values(by=column, ascending=ascending)
