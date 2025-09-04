#!/bin/sh

# Set up the challenge files
echo "Setting up challenge files..."
python -c 'from app import setup_challenge; setup_challenge()'

# Start the Flask application
echo "Starting application..."
exec gunicorn --bind 0.0.0.0:5003 app:app
