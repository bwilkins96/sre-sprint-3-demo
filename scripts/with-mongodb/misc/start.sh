#!/bin/bash

# builds python docker image with latency_checker.py
# and runs docker compose up for latency checker and mongodb containers

echo -e "BUILDING IMAGE: lc-image\n"

docker build -t lc-image .

echo -e "\nDOCKER COMPOSE UP FOR CONTAINERS: lc-container and lc-mongodb\n"

docker compose up -d

echo -e "\n'latency-checker' or 'lc' is equivalent to 'python latency-checker.py'"
echo -e "Run 'exit' to close the container\n"

docker exec -it lc-container /bin/bash