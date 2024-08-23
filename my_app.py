import requests
import json

URL = 'https://api.football-data.org'
TEAMS = '/v4/teams/'
COMPETITIONS = '/v4/competitions/'
HEADERS = { 'X-Auth-Token': '5947c680a0ab4718b860504baedca73b'}

# List all teams for a particular competition.
TEAMS_FOR_COMPETIOTIONS = "/v4/competitions/{id}/teams"
JSON_FILE_PATH = "/Users/bilberry/DE/Projects/de_take_home_test/"

def get_competitions():
    # Define the API endpoint URL
    url = URL + COMPETITIONS
    headers = { 'X-Auth-Token': '5947c680a0ab4718b860504baedca73b'}

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url,headers=headers)
        # print(response.json())
        # for match in response.json()['matches']:
        #     print(match)
        
        # for competition in response.json()['competitions']:
        #     print(competition['id'])
        
        # if response.status_code == 200:
        #     data = response.json()
        #     json_file_path = "/Users/bilberry/DE/Projects/de_take_home_test/response_data.json"
    
        #     with open(json_file_path, 'w') as json_file:
        #         json.dump(data, json_file, indent=4)
        
        competition_ids = []
        json_file_path = "/Users/bilberry/DE/Projects/de_take_home_test/"
        for competition in response.json()['competitions']:
            competition_ids.append(competition['id'])
            filename = json_file_path + "competition_" + str(competition['id']) + ".json"

            with open(filename, 'w') as json_file:
                json.dump(competition, json_file, indent=4)
        

        # Check if the request was successful (status code 200)
        # if response.status_code == 200:
        #     posts = response.json()
        #     return posts
        # else:
        #     print('Error:', response.status_code)
        #     return None

    except requests.exceptions.RequestException as e:
  
    # Handle any network-related errors or exceptions
        print('Error:', e)
    return competition_ids

def get_teams(ids):
    for id in ids:
        url = URL + f"/v4/competitions/{id}/teams"
        response = requests.get(url,headers=HEADERS)
        # print(response.json())
        
        filename = JSON_FILE_PATH + "teams_in_competition_" + str(id) + ".json"
        
        with open(filename, 'w') as json_file:
            json.dump(response.json(), json_file, indent=4)
        

# competition_ids = get_competitions()
# print(competition_ids)

# get_teams(competition_ids)

def workaround(id):
        url = URL + f"/v4/competitions/{id}/teams"
        response = requests.get(url,headers=HEADERS)
        # print(response.json())
        
        filename = JSON_FILE_PATH + "teams_in_competition_" + str(id) + ".json"
        
        with open(filename, 'w') as json_file:
            json.dump(response.json(), json_file, indent=4)
            

# workaround(2152)

