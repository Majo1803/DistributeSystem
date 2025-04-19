import React from 'react';

function TaskTable({ tasks }) {
  return (
    <table className="table">
      <thead>
        <tr>
          <th>Nodo</th>
          <th>Tarea</th>
          <th>Resultado</th>
          <th>Hora</th>
        </tr>
      </thead>
      <tbody>
        {tasks.map((t, i) => (
          <tr key={i}>
            <td>{t.node_id}</td>
            <td>{t.task_type}</td>
            <td>{t.result}</td>
            <td>{t.timestamp}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default TaskTable;
