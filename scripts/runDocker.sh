#!/bin/bash

# starts and stops docker container with latency checker

# must be run inside 'sre-sprint-3-demo' folder

# example commands:
# cd ./sre-sprint-3-demo
# ./scripts/runDocker.sh

echo -e "\nRUNNING START SCRIPT\n"
./scripts/docker/start.sh

echo -e "\nRUNNING CLEAN UP SCRIPT\n"
./scripts/docker/cleanUp.sh
echo ""