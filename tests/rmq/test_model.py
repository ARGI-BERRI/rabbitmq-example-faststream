"""Test cases for models in the RMQ service."""

from service.rmq.model import SimpleMessage


def test_simple_message() -> None:
    """Test SimpleMessage instance creation."""
    message = SimpleMessage(uuid="test-uuid", content="test-content")

    assert message.uuid == "test-uuid"
    assert message.content == "test-content"
    assert isinstance(message, SimpleMessage)
