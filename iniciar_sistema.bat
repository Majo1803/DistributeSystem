@echo off
echo ===========================
echo INICIANDO SISTEMA DISTRIBUIDO
echo ===========================

REM Abre el backend en nueva ventana de consola
start "BACKEND" cmd /k "cd /d C:\Users\marij\OneDrive\Escritorio\DistributeSystem\DistributedSystem\DistributeSystem\dashboard\backend && call venv\Scripts\activate && uvicorn main:app --reload"

REM Abre el frontend en nueva ventana de consola
start "FRONTEND" cmd /k "cd /d C:\Users\marij\OneDrive\Escritorio\DistributeSystem\DistributedSystem\DistributeSystem\dashboard && npm start"

echo Esperando inicio del sistema...
