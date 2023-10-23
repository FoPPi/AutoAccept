#!/bin/bash

# Check if Python is installed
if command -v python &>/dev/null; then
    echo "Python is installed."
else
    echo "Python is not installed. Installing Python..."
    if [ "$(uname)" == "Darwin" ]; then
        # macOS
        brew install python
    else
        # Linux (Ubuntu/Debian)
        sudo apt-get update
        sudo apt-get install -y python3
    fi
fi

# Check if pip is installed
if command -v pip &>/dev/null; then
    echo "pip is installed."
else
    echo "pip is not installed. Installing pip..."
    if [ "$(uname)" == "Darwin" ]; then
        # macOS
        brew install python
    else
        # Linux (Ubuntu/Debian)
        sudo apt-get install -y python3-pip
    fi
fi

# Install required packages using pip
if [ -f "requirements.txt" ]; then
    echo "Installing required packages..."
    pip install -r requirements.txt
else
    echo "requirements.txt file not found. Skipping package installation."
fi

# Run main.py
if [ -f "main.py" ]; then
    echo "Running main.py..."
    python main.py
else
    echo "main.py file not found. Cannot run the program."
fi
