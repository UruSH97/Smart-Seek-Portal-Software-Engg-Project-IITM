#!/bin/sh

echo "======================================================================"
echo "Welcome to the setup. This script will set up the local virtual environment"
echo "and install all the required Python libraries."
echo "You can rerun this script without any issues."
echo "----------------------------------------------------------------------"

if [ -d ".env" ]; then
    echo "Enabling virtual environment"
else
    echo "No virtual environment found. Please run setup.sh first."
    exit 1
fi

# Activate virtual environment
. .env/bin/activate

export ENV=testing

pytest --verbose --disable-warnings -s

deactivate
