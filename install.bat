@echo off



REM Set installation directory
set INSTALL_DIR=%PROGRAMFILES%\AIFE
mkdir "%INSTALL_DIR%"

REM Copy necessary files to the installation directory
copy /Y .\bin "%INSTALL_DIR%"
xcopy /E /Y ".\bin\*" "%INSTALL_DIR%"
copy /Y ".\install.bat" "%INSTALL_DIR%"
copy /Y ".\.env" "%INSTALL_DIR%"

REM Set environment variables
setx PATH "%PATH%;%INSTALL_DIR%" /M

REM Create a batch file to run the application
echo @echo off>"%INSTALL_DIR%\run_aife.bat"
echo python "%INSTALL_DIR%\main.py" %%\*>>"%INSTALL_DIR%\run_aife.bat"

REM Create a shortcut in the Start Menu
set SCRIPT_PATH=%TEMP%\create_shortcut.vbs
echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT_PATH%
echo Set oLink = oWS.CreateShortcut("%%APPDATA%%\Microsoft\Windows\Start Menu\Programs\AIFE.lnk") >> %SCRIPT_PATH%
echo oLink.TargetPath = "%INSTALL_DIR%\run_aife.bat" >> %SCRIPT_PATH%
echo oLink.Save >> %SCRIPT_PATH%
cscript //nologo %SCRIPT_PATH%
del %SCRIPT_PATH%

REM Display a message to inform the user about the installation
echo AIFE has been installed successfully.
echo You can run the application from the Start Menu.

REM Cleanup
rmdir /s /q "%TEMP%\AIFE"
