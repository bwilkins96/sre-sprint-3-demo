#!/bin/bash

# builds python docker image with latency_checker.py and runs container

echo -e "BUILDING IMAGE: lc-image\n"

docker build -t lc-image .

echo -e "\nRUNNING CONTAINER: lc-container"
echo "'latency-checker' or 'lc' is equivalent to 'python latency-checker.py'"
echo -e "Run 'exit' to close the container\n"

docker run -it --name lc-container lc-image /bin/bash