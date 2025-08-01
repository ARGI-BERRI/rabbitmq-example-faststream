"""Models for RabbitMQ interactions."""

import uuid

from pydantic import BaseModel, Field


class SimpleMessage(BaseModel):
    """A simple message model for RabbitMQ interactions."""

    content: str
    uuid: str = Field(default_factory=lambda: uuid.uuid4().hex)
