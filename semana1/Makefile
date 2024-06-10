# Define the project name for docker-compose
COMPOSE_PROJECT_NAME=redshift-instance

# Define the service name for the redshift container
PG_SERVICE_NAME=redshift-instance

# Define the port mapping for the redshift container (default: 5432)
PG_PORT=5432

DOCKER_PATH=./redshift/docker-compose.yml
DATABASE_SCRIPT=/sql_nivelacion/database_ddl.sql

.PHONY: all up psql

all: up psql

up:
	@echo "Starting redshift container and importing database (if configured)"
	docker-compose -f $(DOCKER_PATH) up -d --build
	@echo "Running script.sql inside the container"
	docker exec -it $(PG_SERVICE_NAME) psql -h db -p $(PG_PORT) -U postgres -f $(DATABASE_SCRIPT)

psql:
	@echo "Opening psql console in redshift container"
	docker exec -it $(PG_SERVICE_NAME) psql -h db -p $(PG_PORT) -U postgres

down:
	@echo "Clean all project"
	docker compose -f $(DOCKER_PATH) down

clean:
	@echo "Delete all"
	docker system prune -a
	@echo "Bye"