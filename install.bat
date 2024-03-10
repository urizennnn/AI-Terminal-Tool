@echo off
setlocal enabledelayedexpansion

REM Set Python version
set PYTHON_VERSION=3.9.5

REM Download Python installer
echo Downloading Python %PYTHON_VERSION% installer...
powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe -OutFile python-installer.exe"

REM Run Python installer interactively
echo Please run the Python installer manually by double-clicking on python-installer.exe.
echo Once installation is complete, please press any key to continue...
pause >nul

REM Check if Python is installed
python --version >nul 2>nul
if !errorlevel! neq 0 (
    echo Failed to install Python %PYTHON_VERSION%
    exit /b 1
)

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install openai redis

REM Create package directory
mkdir "%USERPROFILE%\Program Files\AIFE"

REM Copy necessary files to package directory
copy /Y ".\\bin\\ai-tool\\main.py" "%USERPROFILE%\Program Files\AIFE"

REM Create package archive
echo Creating package archive...
powershell -Command "Compress-Archive -Path '%USERPROFILE%\Program Files\AIFE' -DestinationPath '%USERPROFILE%\AIFE.zip'"

REM Clean up package directory
rmdir /S /Q "%USERPROFILE%\Program Files\AIFE"

echo Done
