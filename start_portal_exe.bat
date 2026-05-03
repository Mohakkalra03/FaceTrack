@echo off
setlocal
cd /d "%~dp0"

echo Starting FACETRACK portal using Python runtime...
start "FACETRACK Portal" cmd /k "set FACETRACK_SERVER_HOST=0.0.0.0 && python api_server.py"
timeout /t 3 /nobreak >nul
start "" "http://127.0.0.1:8000"
for /f "usebackq delims=" %%I in (`powershell -NoProfile -ExecutionPolicy Bypass -Command "(Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.IPAddress -notlike '127.*' -and $_.IPAddress -notlike '169.254*' -and $_.InterfaceAlias -notmatch 'Loopback|vEthernet' } | Select-Object -First 1 -ExpandProperty IPAddress)"`) do set FACETRACK_IP=%%I
echo.
echo FACETRACK portal server started.
echo Open on laptop: http://127.0.0.1:8000
if defined FACETRACK_IP (
  echo Open on phone using your Wi-Fi IPv4: http://%FACETRACK_IP%:8000
) else (
  echo Open on phone using your Wi-Fi IPv4: http://YOUR-IP:8000
)
pause
