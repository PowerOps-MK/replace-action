#Specify the base image alpine:3.17.1
FROM alpine:3.17.1

# Create a working directory inside the image
WORKDIR /app

# Copy directory files i.e all files
# COPY . .

# Download modules and dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# Command to be used to execute when the image is used to start a container
# Container image that runs your code

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
