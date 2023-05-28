#!/bin/bash

echo "Building the project..."
python3.9 -m pip install -r requirements.txt

echo "Running the project"
python3.9 manage.py makemigrations manga --noinput
python3.9 manage.py migrate --noinput

echo "Collect Static"
python3.9 manage.py collectstatic --noinput --clear

echo "TEST"
