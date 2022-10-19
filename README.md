# sampleRedisWithFlask
This project has been created for DevOps intern interview tasks.

## Quick start
Clone the repository, cd into in and run the following commands:
```
docker build --build-arg GIT_COMMIT=$(git rev-parse --short HEAD) -t app_image .
docker-compose up -d 
```
After that, the application runs on http://localhost:5000

## Requierements

The application has been built with the following verisons:
- Docker version 20.10.12
- Docker Compose version v2.10.2

## Docker containers
There are two running containers:
- samplerediswithflask-web-1: where the Flask application runs
- samplerediswithflask-redis-1: containing the redis server

## Application
The application has four endpoints, it communicate with the Redis service.
- /healthz: return the string "ok" 
- /alert: increment a counter in redis (key:counter)
- /counter: print the value of the counter
- /version: return the short git commit hash

## Working with containers
Following the log of a specific container
```
sudo docker-compose logs -f server
```
Getting a shell in a container
```
sudo docker-compose exec -i -t server /bin/bash
```
Stopping containers and cleaning up
```
sudo docker-compose down --volumes
```