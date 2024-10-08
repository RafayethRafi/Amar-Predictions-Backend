from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    database_hostname : str
    database_port : str
    database_password : str
    database_name : str
    database_username : str
    secret_key :str
    algorithm : str
    access_token_expire_minutes : int

    # redis_port : str
    # redis_url : str
    # redis_password : str
    # redis_host : str
    # redis_tls_url : str


    class Config:
        env_file = ".env"

settings = Settings()
