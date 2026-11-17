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

## Push the Image to a Private Docker Hub Repo

```bash
docker login
docker tag sysmetrics:latest YOUR_DOCKERHUB_USERNAME/sysmetrics:latest
docker push YOUR_DOCKERHUB_USERNAME/sysmetrics:latest
```

## Deploy on AWS EC2

1. Launch an EC2 instance (Amazon Linux or Ubuntu) and connect via SSH (Linux terminal) or PuTTY (Windows).
2. Install Docker:
   ```bash
   sudo dnf install -y docker          # Amazon Linux
   sudo systemctl enable --now docker
   sudo usermod -aG docker ec2-user
   ```
3. Log in and pull the private image:
   ```bash
   docker login
   docker pull YOUR_DOCKERHUB_USERNAME/sysmetrics:latest
   ```
4. Run the container:
   ```bash
   mkdir -p ~/metrics
   docker run -d --name sysmetrics --restart unless-stopped \
     -v ~/metrics:/app/data \
     YOUR_DOCKERHUB_USERNAME/sysmetrics:latest
   ```
5. Verify:
   ```bash
   docker ps
   docker logs sysmetrics
   ```

## Author

Sajjad Khan
GitHub: [Sajjadkhan21](https://github.com/Sajjadkhan21)
