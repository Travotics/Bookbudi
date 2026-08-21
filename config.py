# import os
# from typing import Literal

# from pydantic_settings import BaseSettings, SettingsConfigDict

# # os.getenv("VARIABLE_NAME","default value")
# APP_ENV = os.getenv("APP_ENV", "dev")

# if APP_ENV not in ("dev", "prd"):
#     raise ValueError(
#         f"Invalid APP_ENV: {APP_ENV}. "
#         "Expected 'dev' or 'prd'."
#     )

# class Settings(BaseSettings):
#     APP_ENV: Literal["dev", "prd"]
#     DB_URL: str

#     model_config = SettingsConfigDict(env_file=f".env.{APP_ENV}", extra="ignore")


# settings = Settings(APP_ENV=APP_ENV)

import os
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

APP_ENV = os.getenv("APP_ENV", "dev")

class Settings(BaseSettings):
    APP_ENV: Literal["dev", "prd"] = "dev"
    DB_URL: str
    FIREBASE_SERVICE_ACCOUNT_JSON: str | None = None
    FIREBASE_SERVICE_ACCOUNT_FILE: str | None = None

    model_config = SettingsConfigDict(
        env_file=f".env.{APP_ENV}",
        extra="ignore",
    )


settings = Settings()