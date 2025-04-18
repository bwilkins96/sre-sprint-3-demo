#!/bin/bash

# starts and stops docker containers 
# with latency checker and mongodb database for logging

# must be run inside 'sre-sprint-3-demo' folder

# example commands:
# cd ./sre-sprint-3-demo
# ./scripts/run.sh

echo -e "\nRUNNING START SCRIPT\n"
./scripts/misc/start.sh

echo -e "\nRUNNING CLEAN UP SCRIPT\n"
./scripts/misc/cleanUp.sh
echo ""