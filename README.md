# Tsurei
Tsurei is a online library of manga/manhwa, where the administrators can upload the content to the website, and the users can freely read. It's the capstone project for the CS50W Web Programming Course.

# How to Run the Project

## Requirements
- python3
- pip

## Create Virtual Environment
    python -m venv venv

## Download dependencies

    pip install -r requirements.txt

Set .env file

    touch .env

### With your favorite editor edit the file and include the line below

    SECRET_KEY=*GENERATE A SECRET KEY*
    DEBUG=TRUE

ex: https://djecrety.ir/

## Migrate django models

    python manage.py makemigrations manga
    python manage.py migrate

## Run server

    python manage.py runserver
