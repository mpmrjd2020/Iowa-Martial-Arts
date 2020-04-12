web: gunicorn Iowa_Martial_Arts.wsgi:application --preload --workers 1 --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate