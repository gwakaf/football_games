import requests
import time


FOOTBALL_API_URL = 'https://api.football-data.org/v4/'
COMPETITIONS_ENDPOINT = 'competitions/'
TEAMS_FOR_COMPETIOTIONS_ENDPOINT = "competitions/{id}/teams"



class APIHandler:
    BASE_URL = FOOTBALL_API_URL
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {'X-Auth-Token': self.api_key}

    def fetch_data(self, endpoint):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 1))
            time.sleep(retry_after)
            return self.fetch_data(endpoint)
        response.raise_for_status()
        return response.json()

    def get_competitions(self):
        return self.fetch_data(COMPETITIONS_ENDPOINT)

    def get_teams_in_competition(self, competition_id):
        return self.fetch_data(f"competitions/{competition_id}/teams")
