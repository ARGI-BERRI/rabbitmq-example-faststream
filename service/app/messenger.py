"""This file is part of a service that publishes messages to a RabbitMQ broker."""

import asyncio
import secrets

from loguru import logger

from service.rmq.messaging import publish_message
from service.rmq.model import SimpleMessage


async def app() -> None:
    """Run the messaging application."""
    while True:
        await publish_message(message=SimpleMessage(content="Hello, World!"))

        delay = secrets.randbelow(10) / 10
        logger.debug(f"Sleeping for {delay} seconds before sending the next message.")

        await asyncio.sleep(delay)


if __name__ == "__main__":
    asyncio.run(app())
