#!/bin/bash

# Start MongoDB in background, build image, and drop into latency checker container interactively

echo -e "STARTING MONGODB SERVICE\n"
docker-compose up -d lc-mongodb

echo -e "\nBUILDING LATENCY CHECKER IMAGE\n"
docker-compose build latency-checker

echo -e "\nRUNNING LATENCY CHECKER CONTAINER"
echo "'python latency_checker.py google.com -c 5 -i 2 -t 50' to test"
echo -e "Run 'exit' to leave the container\n"

docker run -it --rm \
  --name lc-container \
  --network sre-sprint-3-demo_default \
  -e MONGO_HOST=lc-mongodb \
  -e MONGO_PORT=27017 \
  lc-image /bin/bash