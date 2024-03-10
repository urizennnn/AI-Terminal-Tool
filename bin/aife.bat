@echo off
REM Check if a keyword is provided
if "%1" == "" (
    echo Error: No keyword provided.
    echo Usage: aife-tool [keyword] [command]
    exit /b 1
)

REM Check if a command is provided after the keyword
if "%2" == "" (
    echo Error: No command provided after the keyword.
    echo Input aife -h to see the possible commands aife offers.
    exit /b 1
)

REM Set the Python executable path
set PYTHON_PATH="%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\python.exe"

REM Run the Python script with the provided keyword and command
%PYTHON_PATH% "%PROGRAMFILES%\AIFE\run_aife.bat" %1 %2 %3 %4 %5 %6 %7 %8 %9
