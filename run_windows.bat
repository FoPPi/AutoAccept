@echo off

REM Check if Python is installed
python --version 2>nul
if %errorlevel%==0 (
    echo Python is installed.
) else (
    echo Python is not installed. Installing Python...
    echo You can download Python from https://www.python.org/downloads/windows/
    echo Make sure to add Python to your system PATH during installation.
)

REM Check if pip is installed
pip --version 2>nul
if %errorlevel%==0 (
    echo pip is installed.
) else (
    echo pip is not installed. Installing pip...
    REM Install pip using the Python installer
    python get-pip.py
)

REM Install required packages using pip
if exist "requirements.txt" (
    echo Installing required packages...
    pip install -r requirements.txt
) else (
    echo requirements.txt file not found. Skipping package installation.
)

REM Run main.py
if exist "main.py" (
    echo Running main.py...
    python main.py
) else (
    echo main.py file not found. Cannot run the program.
)

pause
