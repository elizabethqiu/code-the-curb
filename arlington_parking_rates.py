import requests
import json
from datetime import datetime


def get_current_rates():
    # Base rates from Arlington County website
    base_rates = {
        'long_term': 1.50,  # Long-term meter rate per hour
        'short_term': 1.75  # Short-term meter rate per hour
    }
    return base_rates


def get_dynamic_parking_data():
    # ExactPark API endpoint for real-time parking data
    url = "https://api.exactpark.com/api/v2/arlington/status/zones"

    try:
        # Get real-time occupancy data
        response = requests.get(url)
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        return data

    except requests.exceptions.RequestException as e:
        print(f"Error accessing ExactPark API: {e}")
        return None


def get_historical_rates():
    # URL for the GIS Open Data rate history
    # gis_url = "https://gisdata-arlgis.opendata.arcgis.com/datasets/parking-meters-rate-history.geojson"
    gis_url = "https://arlgis.arlingtonva.us/arcgis/rest/services/Open_Data/od_Parking_Meter_Points/FeatureServer/2/query?outFields=*&where=1%3D1&f=geojson"

    try:
        # Get historical rate data
        response = requests.get(gis_url)
        response.raise_for_status()

        # Parse GeoJSON response
        data = response.json()

        return data

    except requests.exceptions.RequestException as e:
        print(f"Error accessing GIS Open Data: {e}")
        return None


def print_parking_info(file):
    # Get current base rates
    base_rates = get_current_rates()
    print("Current Base Rates:")
    print(f"Long-term meters: ${base_rates['long_term']:.2f}/hour")
    print(f"Short-term meters: ${base_rates['short_term']:.2f}/hour")

    # Get real-time parking data
    print("Fetching real-time parking data...")
    parking_data = get_dynamic_parking_data()

    if parking_data and 'data' in parking_data:
        total_spaces = len(parking_data['data'])
        occupied = sum(
            1 for space in parking_data['data'] if space['status'] == 'occupied')
        vacancy_rate = ((total_spaces - occupied) / total_spaces) * 100

        print("Real-time Parking Statistics:")
        print("Total monitored spaces:", total_spaces)
        print("Currently occupied:", occupied)
        print("Vacancy rate: {:.1f}%".format(vacancy_rate))

    # Get historical rate data
    print("Fetching historical rate data...")
    historical_data = get_historical_rates()

    if historical_data:
        print("Historical rate data is available")
        file.write(json.dumps(historical_data, indent=4))
    else:
        print("Historical rate data is currently unavailable")


if __name__ == "__main__":
    print("Arlington County Parking Rate Information\n")
    print("----------------------------------------")
    with open('parking_rate_info.txt', 'w') as file:
        print_parking_info(file)
    print("Parking information saved to parking_rate_info.txt")
