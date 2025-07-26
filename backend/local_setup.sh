#!/bin/sh

echo "======================================================================"
echo "Welcome to the setup. This script will set up the local virtual environment"
echo "and install all the required Python libraries."
echo "You can rerun this script without any issues."
echo "----------------------------------------------------------------------"

if [ -d ".env" ]; then
    echo "The .env folder already exists. Installing Python libraries using pip."
else
    echo "Creating .env folder and installing Python libraries using pip."
    python3 -m venv .env
fi

# Activate the virtual environment
. .env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required Python libraries
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate
