import requests
import json
from datetime import datetime

# https://www.w3schools.com/python/python_json.asp
# https://docs.python.org/3/library/json.html

# get data from the API
def get_parking_status(): # rate limit 😂  -> every 10 mins (testing: 10 seconds)
    # API endpoint URL
    url = "https://api.exactpark.com/api/v2/arlington/status/zones"

    try:
        # Make GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        if response.status_code != 200:
            print(f"error in data retrieval with response code {response.status_code}")
            return None
        else:
            print("data received successfully with response code 200")

        # Parse the JSON response
        data = response.json()

        # Print basic information
        print(f"API Version: {data['version']}")
        print(f"Timezone: {data['timezone']}")
        print(f"\nTotal stalls retrieved: {len(data['data'])}")

        # Count vacant and occupied stalls
        vacant_count = sum(1 for stall in data['data'] if stall['status'] == 'vacant')
        occupied_count = sum(1 for stall in data['data'] if stall['status'] == 'occupied')

        print(f"Vacant stalls: {vacant_count}")
        print(f"Occupied stalls: {occupied_count}")

        # Example: Print details of first 5 stalls
        print("\nSample stall details:")
        for stall in data['data'][:5]:
            print(f"\nStall ID: {stall['stallID']}")
            print(f"Name: {stall['stallName']}")
            print(f"Block Face: {stall['blockfaceID']}")
            print(f"Status: {stall['status']}")
            print(f"Location: {stall['location']['lat']}, {stall['location']['long']}")
            print(f"Last Updated: {stall['payloadTimestamp']}")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing API: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
    except KeyError as e:
        print(f"Error accessing data structure: {e}")

# def post_data(url, data):
#     response = requests.post(url, json=data)
#     print(f"response status code: {response.status_code}")
#     print(response.text)
#     if response.status_code != 201:
#         print("error in data posting")
#         return None

#     print("data posted successfully")
#     return response.json()

if __name__ == "__main__":
    print("Fetching Arlington parking data...")
    get_parking_status()
