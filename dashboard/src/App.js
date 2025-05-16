import React, { useEffect, useState } from "react";
import NodeCard from "./components/NodeCard";
import TaskCard from "./components/TaskCard";
import TaskTable from "./components/TaskTable";
import "./App.css";

function App() {
  const [nodes, setNodes] = useState([]);
  const [activeTasks, setActiveTasks] = useState([]);
  const [taskHistory, setTaskHistory] = useState([]);

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("http://localhost:8000/api/nodes")
        .then((res) => res.json())
        .then(setNodes);

      fetch("http://localhost:8000/api/active-tasks")
        .then((res) => res.json())
        .then(setActiveTasks);

      fetch("http://localhost:8000/api/tasks")
        .then((res) => res.json())
        .then(setTaskHistory);
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ display: "flex", flexDirection: "column", height: "100vh", padding: 20 }}>
      {/* Sección superior: tareas activas y nodos */}
      <div style={{ display: "flex", flex: 1, marginBottom: 20 }}>
        {/* Columna principal - tareas activas */}
        <div style={{ flex: 1, marginRight: 20 }}>
          <h2>Tareas Activas en Ejecución</h2>
          <div className="task-grid">
            {activeTasks.map((task, idx) => (
              <TaskCard key={idx} task={task} />
            ))}
          </div>
        </div>

        {/* Columna derecha - nodos */}
        <div
          style={{
            width: 300,
            backgroundColor: "#f9f9f9",
            padding: 10,
            borderRadius: 8,
            boxShadow: "0 0 10px rgba(0,0,0,0.1)",
            overflowY: "auto",
            maxHeight: "90vh",
          }}
        >
          <h3>Nodos</h3>
          {nodes.map((node, idx) => (
            <NodeCard key={idx} node={node} compact />
          ))}
        </div>
      </div>

      {/* Sección inferior: tabla de historial */}
      <div style={{ flexShrink: 0 }}>
        <h2>Histórico de Resultados</h2>
        <TaskTable tasks={taskHistory} />
      </div>
    </div>
  );
}

export default App;
