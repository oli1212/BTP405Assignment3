# Base image is python 3.11 slim
FROM python:3.11-slim

# Create the work directory
WORKDIR /app

# Copy all code to Docker image
COPY . /app

# Installing needed packages
RUN pip install --no-cache-dir mysql-connector-python

# Expose the applicaiton port
EXPOSE 8080

# Run the python Server
CMD ["python", "server.py"]