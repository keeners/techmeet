.PHONY: build

CONTAINERNAME=techmeet_frontend
IMAGENAME=techmeet_frontend

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## Build the Docker image
	docker build -t $(IMAGENAME) .

up: build ## Bring the container up
	docker run -d \
		--name $(CONTAINERNAME) \
		-v "$(PWD):/usr/src/app" \
		-v "/usr/src/app/node_modules" \
		-p "3000" \
		$(IMAGENAME) tail -f /dev/null

down: ## Stop the container
	docker stop $(CONTAINERNAME)

enter: ## Enter the running container
	docker exec -it $(CONTAINERNAME) /bin/sh

clean: down ## Remove stopped containers
	docker rm $(CONTAINERNAME)
