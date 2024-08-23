import json
import psycopg2
import os


class Database:
    def __init__(self,db_params):
        self.conn = psycopg2.connect(**db_params)
        self.cur = self.conn.cursor()
        
    
    def create_tables(self):
        create_dim_competitions_table_statement = """CREATE TABLE IF NOT EXISTS dim_competitions (id INT PRIMARY KEY, name VARCHAR(100))"""
        create_dim_teams_table_statement = """CREATE TABLE IF NOT EXISTS dim_teams (id INT PRIMARY KEY, name VARCHAR(100))"""
        create_fact_competitions_table_statement = """CREATE TABLE IF NOT EXISTS fact_competitions (competition_id INT, team_id INT)"""
        
        self.cur.execute(create_dim_competitions_table_statement)
        self.cur.execute(create_dim_teams_table_statement)
        self.cur.execute(create_fact_competitions_table_statement)
        
        self.conn.commit()
    
    """Insert data from competitions file to dim_competitions table"""    
    def insert_from_competitions(self, json_folder_path):
        for file_name in os.listdir(json_folder_path):
            if file_name.startswith("competition"):
                file_path = os.path.join(json_folder_path, file_name)
                with open(file_path, 'r') as file:
                    content = json.load(file)
                    self.cur.execute("""INSERT INTO dim_competitions (id, name) VALUES (%s,%s) ON CONFLICT DO NOTHING""",(content["id"], content["name"]))
        self.conn.commit()
        
        
    def insert_from_teams_in_competitions(self, json_folder_path):
        for file_name in os.listdir(json_folder_path):
            if file_name.startswith("teams_in_competition"):
                file_path = os.path.join(json_folder_path, file_name)
                with open(file_path, 'r') as file:
                    content = json.load(file)
                    competition_id = content["competition"]["id"]
        
                    for team in content["teams"]:
                        self.cur.execute("""INSERT INTO dim_teams (id, name) VALUES (%s,%s) ON CONFLICT DO NOTHING""",(team["id"], team["name"]))
                        self.cur.execute("""INSERT INTO fact_competitions (competition_id, team_id) VALUES (%s,%s) ON CONFLICT DO NOTHING""",(competition_id, team["id"]))
        self.conn.commit()
        
    def close_conn(self):
        self.cur.close()
        self.conn.close()