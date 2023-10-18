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

### With your favorite editor edit the file and include the line below

    SECRET_KEY=*GENERATE A SECRET KEY*
    DEBUG=TRUE

    # Create Super User (optional)
    DJANGO_SUPERUSER_USERNAME="yourusername"
    DJANGO_SUPERUSER_PASSWORD="yourpassword"
    DJANGO_SUPERUSER_EMAIL="youremail"
    

ex: https://djecrety.ir/

## Run Docker
    cd ../../
    docker-compose up
