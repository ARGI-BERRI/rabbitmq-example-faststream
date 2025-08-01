"""Test RabbitConfig class for RabbitMQ configuration handling."""

import os

from service.rmq.config import RabbitConfig


def test_rabbit_config() -> None:
    """Test RabbitConfig values and URL generation."""
    config = RabbitConfig(
        RMQ_HOST="dummy_host",
        RMQ_PORT=123456,
        RMQ_USER="dummy_user",
        RMQ_PASSWORD="dummy_password",
    )

    assert config.host == "dummy_host"
    assert config.port == 123456
    assert config.user == "dummy_user"
    assert config.password == "dummy_password"
    assert config.url == "amqp://dummy_host:123456/"

    os.environ["RMQ_HOST"] = "env_host"
    os.environ["RMQ_PORT"] = "654321"
    os.environ["RMQ_USER"] = "env_user"
    os.environ["RMQ_PASSWORD"] = "env_password"

    config = RabbitConfig()
    assert config.host == "env_host"
    assert config.port == 654321
    assert config.user == "env_user"
    assert config.password == "env_password"
    assert config.url == "amqp://env_host:654321/"
