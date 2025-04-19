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
