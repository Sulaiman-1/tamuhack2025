#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Navigate to the script's directory so we can reliably create venv at the project root
# If your script is in "scripts/" and you want to run it from the project root,
# you can either:
#   - cd "$(dirname "$0")/.." to move up one directory
#   - or just ensure you reference the correct paths

# Option A: cd to project root by going one level up from "scripts/"
cd "$(dirname "$0")/.."

# Create the venv in the project root if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment in $(pwd)/venv..."
    python3 -m venv venv
fi

# Activate the venv
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies if requirements.txt exists in app/
REQ_FILE="app/requirements.txt"
if [ -f "$REQ_FILE" ]; then
    echo "Installing dependencies from $REQ_FILE..."
    pip install --upgrade pip
    pip install -r "$REQ_FILE"
else
    echo "No requirements.txt found at $REQ_FILE. Skipping installation."
fi

echo "Done! Virtual environment is ready and dependencies (if any) are installed."
echo "To activate the venv, run \"source venv/bin/activate\" "
