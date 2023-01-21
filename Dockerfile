# Specify the base image python:3.11-slim
FROM python@sha256:1274a1fb3354baf78e80cc7485771175b506a4712e49e272765dceeb0528fad1

# Create a working directory inside the image
WORKDIR /app

# Copy directory files i.e all files
COPY . .

# Code file to execute when the docker container starts up
CMD ["python3", "replace.py"]
