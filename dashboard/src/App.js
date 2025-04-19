import React, { useEffect, useState } from 'react';
import './App.css';
import NodeCard from './components/NodeCard';
import TaskTable from './components/TaskTable';

function App() {
  const [nodes, setNodes] = useState([]);
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("http://localhost:8000/api/nodes")
        .then(res => res.json())
        .then(data => setNodes(data));

      fetch("http://localhost:8000/api/tasks")
        .then(res => res.json())
        .then(data => setTasks(data));
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="container">
      <h1>Sistema Distribuido - Dashboard</h1>
      <div className="grid">
        {nodes.map(node => (
          <NodeCard key={node.id} node={node} />
        ))}
      </div>

      <h2>Histórico de Tareas</h2>
      <TaskTable tasks={tasks} />
    </div>
  );
}

export default App;
