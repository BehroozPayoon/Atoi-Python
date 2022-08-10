## Atoi Project

The project developed by the help of Docker, Traefik and Redis. You can find a running version on: https://payoon.dev

1. The first step is to build the docker image using the Dockerfile => `Docker build -t atoi:latest .`
2. For development use `docker-compose.local.yml` for example => `docker-compose -f docker-compose.local.yml up -d`
3. After the project is running you can test the it using => `docker-compose -f docker-compose.local.yml exec app pytest`
