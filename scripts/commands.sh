#!/bin/sh
set -e

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    echo "Waiting for Postgres Database Setup ($POSTGRES_HOST $POSTGRES_PORT)..."
    sleep 0.1
done

echo "Running the project"

python3 manage.py makemigrations manga --noinput
python3 manage.py migrate --noinput

echo "Creating super user"

python3 manage.py createsuperuser \
    --email $DJANGO_SUPERUSER_EMAIL \
    --username $DJANGO_SUPERUSER_USERNAME \
    --noinput || true

echo "Collect Static"
python3 manage.py collectstatic --noinput --clear

echo "Running Server"
pwd
gunicorn --bind 0.0.0.0:8000 tsurei.wsgi
