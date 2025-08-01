.PHONY: start-service stop-service

start-service:
	@echo "Starting service..."
	docker compose up -d

stop-service:
	@echo "Stopping service..."
	docker compose down
