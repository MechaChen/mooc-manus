from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """MoocManus 後端配置信息，從 .env 或者環境變量中加載數據，並利用 pydantic 做環境變數的型別檢查"""

    # 給定預設值，就算沒有傳入環境變量，也會有預設值

    # project 基礎設置
    env: str = "development"
    log_level: str = "INFO"

    # Database 相關配置
    sqlalchemy_database_uri: str = ""

    # Redis 相關配置
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0
    redis_password: str | None = None

    # 使用 pydantic v2 的寫法來完成環境變量信息的告知
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # 忽略沒有定義在 Settings class 中，但存在於 .env 中的 file
    )


if __name__ == "__main__":
    settings = Settings()
    print(settings)
