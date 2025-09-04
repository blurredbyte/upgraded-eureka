#!/bin/sh

# Initialize the database
echo "Initializing database..."
python -c 'from app import init_db; init_db()'

# Start the Flask application
echo "Starting application..."
exec gunicorn --bind 0.0.0.0:5001 app:app
