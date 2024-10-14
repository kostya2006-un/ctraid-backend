#!/bin/sh
python manage.py migrate --no-input -v 0
python manage.py collectstatic --no-input -v 0
python manage.py ensure_admin --user-id admin --password admin
python manage.py compilemessages -v 0

exec python manage.py runserver 0.0.0.0:8000
