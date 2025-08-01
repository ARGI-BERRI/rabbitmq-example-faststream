"""Configuration for RabbitMQ connection using Pydantic."""

from pydantic import Field
from pydantic_settings import BaseSettings


class RabbitConfig(BaseSettings):
    """Configuration for RabbitMQ connection."""

    host: str = Field(
        default="localhost",
        description="RabbitMQ host",
        alias="RMQ_HOST",
    )
    """Hostname for RabbitMQ connection."""

    port: int = Field(
        default=5672,
        description="RabbitMQ port",
        alias="RMQ_PORT",
    )
    """Port for RabbitMQ connection."""

    user: str = Field(
        default="rmq",
        description="RabbitMQ user",
        alias="RMQ_USER",
    )
    """User for RabbitMQ connection."""

    password: str = Field(
        default="rmq",
        description="RabbitMQ password",
        alias="RMQ_PASSWORD",
    )
    """Password for RabbitMQ connection."""

    @property
    def url(self) -> str:
        """Get the RabbitMQ connection URL.

        Returns:
            str: The RabbitMQ connection URL.
        """
        return f"amqp://{self.host}:{self.port}/"


rabbit_config = RabbitConfig()
