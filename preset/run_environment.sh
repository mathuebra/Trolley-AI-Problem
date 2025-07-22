#!/bin/bash

# Check if venv directory exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    virtualenv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install required packages
pip install pandas seaborn matplotlib openai dotenv

echo "Environment setup complete."