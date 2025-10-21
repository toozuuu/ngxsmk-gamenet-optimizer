#!/bin/bash

echo "NGXSMK GameNet Optimizer"
echo "========================"
echo ""
echo "Starting application..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.7 or higher"
    exit 1
fi

# Check Python version
python_version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
required_version="3.7"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "Error: Python 3.7 or higher is required"
    echo "Current version: $python_version"
    exit 1
fi

echo "✅ Python version: $python_version"

# Check if requirements are installed
echo "Checking dependencies..."
python3 -c "import psutil, tkinter" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing required dependencies..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install dependencies"
        exit 1
    fi
fi

# Run the application
echo "Starting NGXSMK GameNet Optimizer..."
python3 launcher.py

# Check exit status
if [ $? -ne 0 ]; then
    echo ""
    echo "Application exited with an error"
    read -p "Press Enter to continue..."
fi
