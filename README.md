# 🧠 Sistema Distribuido con Monitoreo Automático de Recursos y Procesamiento Cooperativo

Este proyecto implementa un sistema distribuido académico que permite:

- 🚀 Ejecutar tareas intensivas desde un **coordinador central**
- 🖥️ Monitorear el estado de múltiples **nodos agentes** en tiempo real
- 🧮 Ejecutar tareas matemáticas (operaciones intensivas) de forma cooperativa
- 📊 Visualizar los recursos y el histórico en un **dashboard moderno (React)**
- 🗃️ Guardar los resultados en **SQL Server**
- ⚡ Usar **Redis** para comunicación y monitoreo rápido

---

## 📁 Estructura del Proyecto

```plaintext
DistributeSystem/
├── dashboard/
│   ├── backend/           ← Backend FastAPI
│   └── frontend/          ← Frontend React
├── agents/                ← Nodos de procesamiento
├── coordinator/           ← Coordinador central
├── Redis-x64-5.0.14.1/    ← Redis local
├── iniciar_sistema_completo.bat ← Script para iniciar todo
└── .env                   ← Variables de entorno
```
---
##⚙️ Requisitos
Windows 11
Python 3.10+
Node.js (v18+)
Redis (ya incluido)
SQL Server + SQL Server Management Studio
Visual Studio Code
---
##📦 Instalación
1. Clona el proyecto
2. Instala dependencias del backend
   ```bash
   cd dashboard/backend
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
    ```
3. Instala dependencias del frontend
    ```bash
    cd ../frontend
    npm install
    ```
4. Configura SQL Server
   ```sql
    CREATE DATABASE DistributedSystem;
      GO
      USE DistributedSystem;
      
      CREATE TABLE TaskHistory (
          ID INT IDENTITY(1,1) PRIMARY KEY,
          NodeID NVARCHAR(50),
          TaskType NVARCHAR(50),
          Result NVARCHAR(MAX),
          Timestamp DATETIME DEFAULT GETDATE()
      );
    ```
   ---
## 🧪 Ejecución
Opción rápida ✅
Haz doble clic en el archivo:
``` bash
iniciar_sistema_completo.bat
```
Esto abrirá:
   - Redis
   - Backend (FastAPI)
   - Frontend (React)
   - Coordinador
   - Nodos nodo1 y nodo2

Opción manual
- Puedes correr cada parte en terminales separadas si lo deseas.

