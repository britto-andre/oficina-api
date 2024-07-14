from pydantic import Field
from pydantic_settings import BaseSettings

class CommonSettings(BaseSettings):
    environment: str = Field(default='homolog')
    firebase_apiKey: str
    firebase_authDomain: str
    firebase_databaseURL: str
    firebase_storageBucket: str
    FIREBASE_CONFIG: str

    class Config:
        env_file_encoding = 'utf-8'
        env_file = '.env'
