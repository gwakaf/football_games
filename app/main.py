import config
import json
from utils.api_handler import APIHandler
from utils.db import Database
from utils.csv_exporter import export_summary


def main():
    api_handler = APIHandler(config.API_KEY)
    
    competitions_json = api_handler.get_competitions()
    # print(competitions_json)
    
    competition_ids = []
    for competition in competitions_json['competitions']:
        competition_ids.append(competition['id'])
        filename = config.JSON_OUTPUT_DATA_FILE_PATH + "competition_" + str(competition['id']) + ".json"

        with open(filename, 'w') as json_file:
            json.dump(competition, json_file, indent=4)

    for id in competition_ids:
        file_name = config.JSON_OUTPUT_DATA_FILE_PATH + "teams_in_competition_" + str(id) + ".json"
        with open(file_name, 'w') as json_file:
            json.dump(api_handler.get_teams_in_competition(id), json_file, indent=4)
        
    db = Database(config.db_params)
    
    db.create_tables()
    
    db.insert_from_competitions(config.JSON_OUTPUT_DATA_FILE_PATH)
    db.insert_from_teams_in_competitions(config.JSON_OUTPUT_DATA_FILE_PATH)
    
    export_summary(config.JSON_OUTPUT_DATA_FILE_PATH, config.OUTPUT_CSV_FILE_PATH)
    
    
if __name__ == "__main__":
    main()