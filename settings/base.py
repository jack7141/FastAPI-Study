import os
from functools import lru_cache

from pydantic import BaseSettings


class ISettings(BaseSettings):
    db_user: str = 'root'
    db_password: str = 'password'
    db_host: str = 'localhost'
    db_port: int = 5432
    db_database: str = 'database-dev'

    debug: bool = True

    @property
    def db_dsn(self):
        dsn = f"postgresql+psycopg2://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_database}"
        return dsn


class DevelopmentSettings(ISettings):
    pass

@lru_cache()
def get_settings():
    config = os.environ.get("FASTAPI_CONFIG", 'default')
    configs = {
        "development": DevelopmentSettings,
        "default": DevelopmentSettings
    }

    return configs.get(config, DevelopmentSettings)()
