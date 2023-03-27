#!/bin/bash

# Start Gunicorn
gunicorn server.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --timeout 120 &

# Start Nginx
nginx -g "daemon off;"
