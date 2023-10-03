# theinitium_exam

# Introduction

This exam project aims to provide the following features:
- User Registration/Login
- Display employee status
- Django admin site integration
- Containerization using Docker
- Web Server using Nginx

# Requirements
- Docker
- Docker Compose

## Installation & Setup

- Clone the repository

```shell
git clone https://github.com/your-username/theinitium_exam.git
cd theinitium_exam
```

- Build the Docker images
```shell
docker-compose build
```
- Start the Docker services
```shell
docker-compose up
```
This will start the Django application on port 8000 and Nginx on port 80.

- Create Superuser
To create a superuser for the Django admin panel, run:
```shell
docker-compose exec web python manage.py createsuperuser
```
Follow the prompts to create a superuser account.

# Usage
- Open your web browser and go to http://localhost:8000 to access the Django application.
- To access the admin panel, navigate to http://localhost:8000/admin and use the superuser credentials.
# Configuration
- The `docker-compose.yml` file contains the configuration for the web and nginx services.
- The `nginx.conf` file located in the root directory is used for the Nginx configuration.
