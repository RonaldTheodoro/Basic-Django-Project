#!/bin/bash

echo "Apply database migrations"
python3 manage.py migrate

echo "Collect static files"
python3 manage.py collectstatic --noinput
exec "$@"