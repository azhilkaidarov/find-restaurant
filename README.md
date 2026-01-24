# Find Restaurant

A Python project for searching and filtering restaurants using Pandas and Google Places API.

## Features

- **Geocoding**: Convert addresses to coordinates using Nominatim
- **Data Loading**: Fetch restaurant data from Google Places API
- **Filtering**: Filter restaurants by price level, rating, distance, and open status
- **Sorting**: Sort results by any column

## Project Structure

```
src/
├── geo_utils.py      # Geocoding and distance calculation
├── data_loader.py    # Google Places API integration
├── data_filter.py    # DataFrame filtering and sorting
└── main.py           # Main entry point
```

## Installation

```bash
# Clone the repository
git clone https://github.com/azhilkaidarov/find-restaurant.git
cd find-restaurant

# Install dependencies
uv sync
```

## Configuration

Create a `.env` file in the project root:

```
GOOGLE_MAP_API_KEY=your_google_places_api_key
```

## Usage

```python
from src.data_loader import fetch_restaurant
from src.data_filter import level_price_filter, rating_filter, distance_filter, sort_by
from src.geo_utils import get_coordinates

# Fetch restaurants near coordinates
df = fetch_restaurant(lat=41.553074, lon=-90.577842, radius=1000)

# Apply filters
df = level_price_filter(df, level_price=2)  # Price level <= 2
df = rating_filter(df, rating=4.0)          # Rating >= 4.0

# Sort by rating
df = sort_by(df, column="rating", ascending=False)

print(df)
```

## Dependencies

- pandas
- numpy
- geopy
- googlemaps
- python-dotenv
- requests

## License

MIT
