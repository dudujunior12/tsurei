#!/bin/bash
set -e

echo "Running the project"

echo "Collect Static"
python3 manage.py makemigrations webform --noinput
python3 manage.py migrate --noinput

echo "Running Server"
python3 manage.py runserver 0.0.0.0:8000