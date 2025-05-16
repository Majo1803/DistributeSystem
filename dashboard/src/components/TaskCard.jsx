import React from "react";

export default function TaskCard({ task }) {
    return (
      <div className="card">
        <h3>{task.type.toUpperCase()}</h3>
        <p><strong>Nodo:</strong> {task.node}</p>
        <p><strong>Resultado:</strong> {task.result}</p>
      </div>
    );
  }
  

