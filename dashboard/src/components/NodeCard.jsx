import React from "react";

function NodeCard({ node, compact }) {
  if (compact) {
    return (
      <div className="node-compact-card">
        <h4 style={{ margin: "0 0 4px 0" }}>🖥️ {node.id}</h4>
        <div>CPU: {node.cpu?.toFixed(1)}%</div>
        <div>RAM: {node.ram?.toFixed(1)}%</div>
      </div>
    );
  }

  return (
    <div className="card">
      <h3>🖥️ {node.id}</h3>
      <p><strong>CPU:</strong> {node.cpu}%</p>
      <p><strong>RAM:</strong> {node.ram}%</p>
      <p><strong>Disco:</strong> {node.disk}%</p>
      <p><strong>Red:</strong> {node.net}</p>
    </div>
  );
}

export default NodeCard;
