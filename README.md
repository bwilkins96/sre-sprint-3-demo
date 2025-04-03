# Network Latency Checker

A lightweight Python-based tool to monitor network latency by pinging target servers and logging high-latency or unreachable events.

---

## Installation Instructions

1. Clone the repo:
```bash
git clone https://github.com/your-org-or-username/network-latency-checker.git

cd network-latency-checker
```
2. Install Dependencies:
```bash
pip install -r requirements.txt
```

## Containerization

This repo contains a [Dockerfile](Dockerfile) for the latency checker tool and a [docker-compose.yml](docker-compose.yml) file for running the latency checker with a MongoDB container for storing logs.

The [scripts](scripts) folder contains bash scripts for starting/cleaning up the Docker containers.

### How to Run:
Execute the script to run the containers:
```bash
# must be run inside 'sre-sprint-3-demo' folder

cd ./sre-sprint-3-demo
./scripts/run.sh
```
Now inside the container, run the python script:
```bash
python latency_checker.py [targets] [options]
```

| Argument | Description | Default |
| -------- | ------- | ------ |
| targets | Target domains or IPs to ping (e.g. google.com) | *Required* |
| -c, --count | Number of pings per target | 10 |
| -i, --interval | Time (in seconds) between each ping | 5 |
| -t, --threshold | Latency threshold in milliseconds | 100 |

#### Example run:
```bash
python latency_checker.py google.com cloudflare.com -c 5 -i 2 -t 50
```

## Output
- Results are printed to the terminal
- High-latency or unreachable events are logged to: ```latency_log.txt``` inside the container
- All events are logged to MongoDB

## MongoDB logs
Logs are saved to the ```latency_monitor.latency_logs``` collection inside MongoDB

Run the script to enter the Mongo shell in another terminal: 
```bash
./scripts/enterMongo.sh
```

Then inside the Mongo shell:
```bash
use latency_monitor
db.latency_logs.find()
```

#### Examples
High latency:
```bash
db.latency_logs.find({ status: "high_latency" })
```
Unreachable:
```bash
db.latency_logs.find({ status: "unreachable" })
```

