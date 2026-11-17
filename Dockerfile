# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .
# Install dependencies
RUN pip install -r requirements.txt

# Copy script
COPY monitor.py .

# Command to run
CMD ["python", "monitor.py"]
