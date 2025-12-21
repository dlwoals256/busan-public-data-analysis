import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DEBUG       = os.getenv('DEBUG', 'False').lower() == 'true'

    DB_HOST     = os.getenv('DB_HOST_LOCAL') if DEBUG == True else os.getenv('DB_HOST_DOCKER')
    DB_PORT     = int(os.getenv('DB_PORT'))
    DB_NAME     = os.getenv('DB_NAME')
    DB_USER     = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    API_KEY = os.getenv('API_KEY')

    @property
    def DATABASE_URL(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
settings = Settings()