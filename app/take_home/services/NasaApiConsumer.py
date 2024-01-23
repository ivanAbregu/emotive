import requests
import os

URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"


class NasaApiConsumer:
    def __init__(self, limit = 100, offset = 0):
        self.limit = min(limit, 1000)
        self.offset = offset

    def get_default_header(self):
        return {
            "Content-Type": "application/json",
        }

    def get_data_by_date(self, earth_date):
        api_key = os.environ.get('NASA_API_KEY','DEMO_KEY')
        params = {
            "api_key": api_key,
            "earth_date": earth_date,
        }

        response = requests.get(URL, params=params, headers=self.get_default_header())
        if response.status_code == 200:
            data = response.json().get('photos', [])
            return data

        return []
