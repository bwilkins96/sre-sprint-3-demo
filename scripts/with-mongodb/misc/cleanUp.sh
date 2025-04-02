#!/bin/bash

# runs docker compose down for latency checker and mongodb containers 
# removes latency checker image and clears the build cache

echo -e "DOCKER COMPOSE DOWN FOR CONTAINERS: lc-container and lc-mongodb\n"

docker compose down

echo -e "\nREMOVING IMAGE: lc-image\n"

docker rmi lc-image

echo -e "\nCLEARING BUILD CACHE\n"

docker buildx prune -f