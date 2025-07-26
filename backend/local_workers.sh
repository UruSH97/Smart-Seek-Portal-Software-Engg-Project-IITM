#!/bin/bash

# Check if the virtual environment exists
if [ -d ".env" ]; then
    echo "Enabling virtual environment..."
else
    echo "No virtual environment found. Please run setup.sh first."
    exit 1
fi

# Activate the virtual environment
source .env/bin/activate

# Set the environment variable
export ENV=development

# Start the Celery worker
celery -A main.celery worker -l info

# Deactivate the virtual environment
deactivate