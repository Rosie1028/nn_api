from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_NAME: str = "ELiRF/NASES"
    MAX_LENGTH: int = 1000
    MIN_LENGTH: int = 80
    TEMPERATURE: float = 0.7
    NUM_BEAMS: int = 4
    LENGTH_PENALTY: float = 2.0
    

settings = Settings()

