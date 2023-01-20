#Specify the base image alpine:3.17.1
FROM alpine@sha256:f271e74b17ced29b915d351685fd4644785c6d1559dd1f2d4189a5e851ef753a

# Copy directory files i.e all files
COPY . .

# Download modules and dependencies
# RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
