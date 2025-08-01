"""This file sets up the FastStream server with RabbitMQ broker."""

import asyncio

from faststream import FastStream
from loguru import logger

from service.rmq.definition import service_broker
from service.rmq.messaging import router

service_broker.include_router(router)
app = FastStream(service_broker, logger=logger)


async def main() -> None:
    """Run the FastStream server."""
    await app.run()


if __name__ == "__main__":
    asyncio.run(main())
