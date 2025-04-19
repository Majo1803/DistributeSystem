@echo off
echo ================================
echo INICIANDO SISTEMA DISTRIBUIDO
echo ================================

REM === INICIAR REDIS DESDE RUTA PERSONALIZADA
echo Iniciando Redis...
start "REDIS" cmd /k "cd /d C:\Users\marij\OneDrive\Escritorio\DistributeSystem\DistributedSystem\DistributeSystem\Redis-x64-5.0.14.1 && redis-server.exe"

REM === INICIAR BACKEND (FastAPI)
echo Iniciando backend FastAPI...
start "BACKEND" cmd /k "cd /d C:\Users\marij\OneDrive\Escritorio\DistributeSystem\DistributedSystem\DistributeSystem\dashboard\backend && call venv\Scripts\activate && uvicorn main:app --reload"

REM === INICIAR FRONTEND (React)
echo Iniciando frontend React...
start "FRONTEND" cmd /k "cd /d C:\Users\marij\OneDrive\Escritorio\DistributeSystem\DistributedSystem\DistributeSystem\dashboard && npm start"

REM === INICIAR COORDINADOR (usando coordinator_main.py)
echo Iniciando coordinador...
start "COORDINADOR" cmd /k "cd /d C:\Users\marij\OneDrive\Escritorio\DistributeSystem\DistributedSystem\DistributeSystem\coordinator && call ..\dashboard\backend\venv\Scripts\activate && python coordinator_main.py"

REM === INICIAR AGENTE nodo1
echo Iniciando nodo1...
start "AGENTE1" cmd /k "cd /d C:\Users\marij\OneDrive\Escritorio\DistributeSystem\DistributedSystem\DistributeSystem && python -m agents.agent nodo1"

REM === INICIAR AGENTE nodo2
echo Iniciando nodo2...
start "AGENTE2" cmd /k "cd /d C:\Users\marij\OneDrive\Escritorio\DistributeSystem\DistributedSystem\DistributeSystem && python -m agents.agent nodo2"

echo ========================================
echo Sistema Distribuido ejecutándose...
echo Abre http://localhost:3000 en tu navegador.
echo ========================================
pause
