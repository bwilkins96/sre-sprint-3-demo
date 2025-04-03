#!/bin/bash

echo -e "STOPPING & REMOVING CONTAINERS AND VOLUMES\n"
docker-compose down --volumes

echo -e "\nCLEARING BUILD CACHE\n"
docker buildx prune -f