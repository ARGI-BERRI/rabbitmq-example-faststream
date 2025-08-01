# RabbitMQ + Python Example App

An example of RabbitMQ Pub/Sub messaging with Python, thanks to the faststream framework.

## Installation

You should use `uv` to install dependencies:

```shell
uv sync
```

## Run applications

There're two applications:

1. Main application: Faststream. This starts the FastStream application, creates queues, and subscribes messages.
2. Sub application: Messenger. This publishes a message to RabbitMQ every 5 seconds.

### Main application (faststream)

```shell
uv run python -m service.app.server
```

### Sub application (messenger)

```shell
uv run service/app/messenger.py
```

## Configuration

Only RabbitMQ configurations are avaiable via environment variables:

```shell
export RMQ_HOST=localhost
export RMQ_PORT=5672
export RMQ_USER=rmq
export RMQ_PASSWORD=rmq
```
