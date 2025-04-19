import React from 'react';

function NodeCard({ node }) {
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
