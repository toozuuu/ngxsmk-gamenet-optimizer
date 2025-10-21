@echo off
echo NGXSMK GameNet Optimizer
echo ========================
echo.
echo Starting application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher from https://python.org
    pause
    exit /b 1
)

REM Check if requirements are installed
echo Checking dependencies...
python -c "import psutil, tkinter" >nul 2>&1
if errorlevel 1 (
    echo Installing required dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Run the application
echo Starting NGXSMK GameNet Optimizer...
python launcher.py

REM Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo Application exited with an error
    pause
)
