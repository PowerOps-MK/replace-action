#Specify the base image alpine:3.17.1
FROM alpine@sha256:f271e74b17ced29b915d351685fd4644785c6d1559dd1f2d4189a5e851ef753a

# Create a working directory inside the image
WORKDIR /app

# Copy directory files i.e all files
COPY . .

RUN chmod +x entrypoint.sh

# Code file to execute when the docker container starts up
#ENTRYPOINT ["/app/entrypoint.sh"]
ENTRYPOINT ["/app"]
