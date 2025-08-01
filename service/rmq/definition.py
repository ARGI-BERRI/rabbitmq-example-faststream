"""This module defines the RabbitMQ broker and queue configurations for the service."""

from faststream.rabbit import RabbitBroker, RabbitQueue
from faststream.rabbit.schemas.queue import QueueType
from faststream.security import SASLPlaintext
from loguru import logger

from service.rmq.config import rabbit_config

# Queue definition
service_queue = RabbitQueue(
    name="service_queue", durable=True, queue_type=QueueType.QUORUM, timeout=180
)

# Broker configuration
service_broker = RabbitBroker(
    url=rabbit_config.url,
    security=SASLPlaintext(username=rabbit_config.user, password=rabbit_config.password),
    validate=True,
    apply_types=True,
    logger=logger,
)
