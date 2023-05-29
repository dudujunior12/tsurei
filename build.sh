#!/bin/bash

echo "Building the project..."
python3.9 -m pip install -r requirements.txt

echo "Running the project"
python3.9 manage.py makemigrations manga --noinput
python3.9 manage.py migrate --noinput

echo "Creating super user"

DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}

python3.9 manage.py createsuperuser \
    --email $DJANGO_SUPERUSER_EMAIL \
    --username $DJANGO_SUPERUSER_USERNAME \
    --noinput || true

echo "Collect Static"
python3.9 manage.py collectstatic --noinput --clear
