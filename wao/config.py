from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_prefix='WAO_', extra='ignore')

    app_name: str = 'WAO-AI'
    environment: str = 'development'
    host: str = '0.0.0.0'
    port: int = 8000
    openai_api_key: str | None = None
    openai_model: str = 'gpt-5.6-luna'
    max_output_tokens: int = 12000
    request_timeout_seconds: float = 90.0
    auth_token: str | None = None
    mcp_server_name: str = 'wao-ai'


settings = Settings()
