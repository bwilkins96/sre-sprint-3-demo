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
## How to Run
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
python latency_checker.py google.com cloudflare.com -c 5 -i 2 -t 150
```

## Output
- Results are printed to the terminal
- High-latency or unreachable events are logged to:
```bash
latency_log.txt
```

## Containerization

This repo contains a [Dockerfile](Dockerfile) for the latency checker tool and a [docker-compose.yml](docker-compose.yml) file for running the latency checker with a MongoDB container for storing logs.

The [scripts](scripts) folder contains bash scripts for starting/cleaning up the Docker containers.

### How to Run:

#### Standalone (only the latency checker container)
```bash
# must be run inside 'sre-sprint-3-demo' folder

cd ./sre-sprint-3-demo
./scripts/standalone/run.sh
```

#### With MongoDB (both the latency checker and MongoDB containers)
```bash
# must be run inside 'sre-sprint-3-demo' folder

cd ./sre-sprint-3-demo
./scripts/with-mongodb/run.sh
```
