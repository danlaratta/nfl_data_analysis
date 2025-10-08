import os 

# Get database configs from .env
DB_USER = os.getenv('DB_USER')
DB_PWD = os.getenv('DB_PWD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'