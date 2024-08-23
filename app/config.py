API_KEY = '5947c680a0ab4718b860504baedca73b' 
JSON_OUTPUT_DATA_FILE_PATH = "/data/"
OUTPUT_CSV_FILE_PATH = '/outputs/competition_summary.csv'

"""Data base connection parameters"""
DATABASE_USER = 'pgrs_admin'
DATABASE_PASSWORD = 'pgrs_password'
DATABASE_HOST = 'postgres_db'  # Hostname is the service name in docker-compose
DATABASE_PORT = '5432'
DATABASE_NAME = 'pgrs_db'

db_params = {
    'dbname': DATABASE_NAME,
    'user': DATABASE_USER,
    'password': DATABASE_PASSWORD,
    'host': DATABASE_HOST, 
    'port': DATABASE_PORT
}