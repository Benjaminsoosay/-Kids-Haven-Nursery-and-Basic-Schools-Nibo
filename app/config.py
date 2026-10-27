from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # These variables will be read from your .env file or Render's environment variables
    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_db_name: str = "kids_haven_db"
    secret_key: str = "your-super-secret-key"

    class Config:
        env_file = ".env"


# We create an instance of Settings to import elsewhere
settings = Settings()
