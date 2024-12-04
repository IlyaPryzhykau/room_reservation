from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование перегородок'
    database_url: str

    class Config:
        env_file = '.env'


settings = Settings()
