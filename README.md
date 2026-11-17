# System Health Monitor

A simple Python tool that periodically collects system health metrics and saves them as timestamped records in a file. It is packaged as a Docker container and deployed on an AWS EC2 instance.

## Metrics Collected

- CPU usage (%)
- Memory usage (%)
- Disk usage (%)
- System uptime

Each record is saved with a timestamp so you can track system health over time.

## Project Structure

```
.
├── Dockerfile           # Builds the custom Python container image
├── requirements.txt     # Python dependencies (e.g. psutil)
├── system_health.py     # Main script that collects the metrics
├── monitor.py           # Monitoring script
├── system_health.csv    # Sample output: collected metrics
└── health_log.txt       # Sample output: log file
```

## Requirements

- Python 3.x
- Docker
- Python packages listed in `requirements.txt`

## Run Locally (without Docker)

```bash
pip install -r requirements.txt
python3 system_health.py
```

## Run with Docker

Build the image:

```bash
docker build -t sysmetrics .
```

Run the container:

```bash
docker run -d --name sysmetrics -v $(pwd)/data:/app/data sysmetrics
```

View the output:

```bash
docker logs sysmetrics
cat data/system_health.csv
```

> Adjust `/app/data` to the folder your script writes to inside the container.


## Author

Sajjad Khan
GitHub: [Sajjadkhan21](https://github.com/Sajjadkhan21)
