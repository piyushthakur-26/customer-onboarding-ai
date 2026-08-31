from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Customer Onboarding AI"
    app_version: str = "0.1.0"
    environment: str = "development"

    database_url: str = (
        "postgresql+psycopg://postgres:postgres@localhost:5432/customer_onboarding"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()