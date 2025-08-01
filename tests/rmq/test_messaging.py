"""Test cases for RabbitMQ messaging functions."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from service.rmq.messaging import publish_message, subscribe_message
from service.rmq.model import SimpleMessage


@pytest.fixture
def simple_message() -> SimpleMessage:
    """Fixture to create a SimpleMessage instance."""
    return SimpleMessage(uuid="test-uuid", content="test-content")


@patch("service.rmq.messaging.service_queue")
@patch("service.rmq.messaging.service_broker.publish")
@patch("service.rmq.messaging.service_broker.connect", AsyncMock())
@pytest.mark.asyncio
async def test_publish_message(
    mock_publish: AsyncMock, mock_service_queue: MagicMock, simple_message: SimpleMessage
) -> None:
    """Test publishing a message to RabbitMQ."""
    await publish_message(simple_message)

    mock_publish.assert_awaited_once()
    mock_publish.assert_awaited_once_with(simple_message, mock_service_queue)


@patch("service.rmq.messaging.secrets.randbelow")
@patch("service.rmq.messaging.asyncio.sleep", AsyncMock())
@pytest.mark.asyncio
async def test_subscribe_message(mock_randbelow: MagicMock, simple_message: SimpleMessage) -> None:
    """Test subscribing to a message from RabbitMQ."""
    rmq_message = AsyncMock()

    mock_randbelow.return_value = 0  # Simulate no random failure
    await subscribe_message(simple_message, rmq_message)
    rmq_message.nack.assert_not_called()

    mock_randbelow.return_value = 6  # Simulate a random failure
    await subscribe_message(simple_message, rmq_message)
    rmq_message.nack.assert_called_once_with(requeue=True)
