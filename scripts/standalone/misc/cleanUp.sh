#!/bin/bash

# removes latency checker container and image

echo -e "REMOVING CONTAINER: lc-container\n"

docker rm lc-container

echo -e "\nREMOVING IMAGE: lc-image\n"

docker rmi lc-image

echo -e "\nCLEARING BUILD CACHE\n"

docker buildx prune -f