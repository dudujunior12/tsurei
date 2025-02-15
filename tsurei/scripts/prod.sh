#!/bin/sh
set -e

echo "Running the project"
export DJANGO_SETTINGS_MODULE=tsurei.settings.prod

echo "Collect Static"
python3 manage.py makemigrations webform --noinput
python3 manage.py migrate --noinput 
python3 manage.py collectstatic --noinput

echo "Running Server"
gunicorn --workers 4 --bind 0.0.0.0:8000 --access-logfile - tsurei.wsgi 