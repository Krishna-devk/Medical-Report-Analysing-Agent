from pydantic_settings import BaseSettings


class Config(BaseSettings):
    GEMINI_API_KEY : str ='None'
    GEMINI_MODEL : str ='gemini-2.5-flash'
    class Config:
        env_file = ".env"
        extra = "ignore"

config = Config()
