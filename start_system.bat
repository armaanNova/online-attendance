@echo off
title Online Smart Face Recognition Attendance Management System
color 0b
echo =====================================================================
echo   ONLINE SMART FACE RECOGNITION ATTENDANCE MANAGEMENT SYSTEM
echo   BCA College Minor Project
echo =====================================================================
echo.
echo [1/2] Verifying Python Environment...
python --version
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH! Please install Python 3.10+
    pause
    exit /b
)
echo.
echo [2/2] Launching System Server and Web Interface...
python run.py
pause
