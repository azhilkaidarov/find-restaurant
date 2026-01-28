from file_handler import read_json, save_result
from geo_utils import get_coordinates
from data_loader import fetch_restaurant
import data_filter


def main():
    # Set up your Input
    config = read_json("configs/input.json")

    # Try to catch organizations in provided radius
    try:
        lat, lon = get_coordinates(config["address"])
        df = fetch_restaurant(
            lat=lat,
            lon=lon,
            radius=config["radius"],
            keyword=config["keyword"]
        )

        # APPLYING FILTERS OF ONLY THEY ARE IN CONFIGS

        # Rating filter
        if "min_rating" in config:
            df = data_filter.rating_filter(df, float(config["min_rating"]))

        # level_price filter
        if "min_level_price" in config:
            df = data_filter.level_price_filter(df, int(config["min_level_price"]))

        # only open filter
        if "only_open" in config:
            df = data_filter.only_open_filter(df)

        # [optional] if you want see distance to every organzation
        # df = data_filter.show_distance_filter(df, lat, lon)

        # Use any column to sort: "lat", "lon", rating, "review_count", "is_open", "distance_ml"
        # sorted_df = data_filter.sort_by(your_df_name, "rating")
        # save_result(df, "your_name")

    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
