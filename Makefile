.PHONY: build

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## Build the Docker image
	docker-compose -p techmeet build

up: build ## Bring the container up
	docker-compose -p techmeet up -d

down: ## Stop the container
	docker-compose -p techmeet stop

enter: ## Enter the running container
	docker-compose -p techmeet exec backend /bin/bash

clean: down ## Remove stoped containers
	docker-compose -p techmeet rm
