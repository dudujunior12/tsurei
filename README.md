# Tsurei
Tsurei is a online library of manga/manhwa, where the administrators can upload the content to the website, and the users can freely read. It's the capstone project for the CS50W Web Programming Course.

# How to Run the Project

## Requirements
- python3
- pip
- docker
- docker-compose

## Set .env file
    cd tsurei/tsurei
    touch .env

### With your favorite editor edit the file and include the lines below

    # Debug true for development, and debug false for production
    SECRET_KEY=*GENERATE A SECRET KEY*
    DEBUG=TRUE
    ALLOWED_HOSTS="0.0.0.0"

    # Create Super User (optional)
    DJANGO_SUPERUSER_USERNAME="yourusername"
    DJANGO_SUPERUSER_PASSWORD="yourpassword"
    DJANGO_SUPERUSER_EMAIL="youremail"

    # For production
    POSTGRES_URL="postgres://postgres:postgres@psql:5432/postgres"
    POSTGRES_PASSWORD="postgres"
    POSTGRES_HOST="psql"
    POSTGRES_PORT="5432"

ex: https://djecrety.ir/

## Run Project

### Development
    cd ..
    python3 manage.py runserver 0.0.0.0:8000

### Production
    cd ../../
    docker-compose up
