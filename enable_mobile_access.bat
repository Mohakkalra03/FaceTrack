@echo off
setlocal

echo Enabling FACETRACK mobile portal access through Windows Firewall...
netsh advfirewall firewall add rule name="FACETRACK Portal 8000" dir=in action=allow protocol=TCP localport=8000

echo.
echo If the rule was added successfully, your phone can open the portal on the same Wi-Fi.
echo Run this file as Administrator if Windows blocks the command.
pause
