"""This module defines the message broker interactions for the service."""

import asyncio
import secrets

from faststream.rabbit import RabbitMessage, RabbitRouter
from loguru import logger

from service.rmq.definition import service_broker, service_queue
from service.rmq.model import SimpleMessage

router = RabbitRouter()

RANDOM_FAILURE_RATE = 5


async def publish_message(message: SimpleMessage) -> None:
    """Publish a message to the message broker.

    Args:
        message (SimpleMessage): The message to publish.
    """
    await service_broker.connect()
    await service_broker.publish(message, service_queue)

    logger.info(f"Published message: {message.uuid=}")


@router.subscriber(service_queue, retry=True)
async def subscribe_message(message: SimpleMessage, rmq_message: RabbitMessage) -> None:
    """Subscribe to a message from the message broker.

    Args:
        message (SimpleMessage): The message received.
        rmq_message (RabbitMessage): The raw RabbitMQ message.
    """
    logger.info(f"Received message: {message.uuid=} with content: {message.content}")

    await asyncio.sleep(secrets.randbelow(5) + 1)

    # ...then, randomly it crashes with an error
    if secrets.randbelow(10) > RANDOM_FAILURE_RATE:
        msg = f"Simulated error for testing purposes: {message.uuid=}"

        logger.error(msg)
        await rmq_message.nack(requeue=True)

    logger.success(f"Processed message: {message.uuid=}")
