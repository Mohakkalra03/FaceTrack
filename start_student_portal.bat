@echo off
setlocal
cd /d "%~dp0"

call start_portal_exe.bat
exit /b %errorlevel%
