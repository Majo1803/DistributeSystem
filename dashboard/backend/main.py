from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from redis_client import get_redis
from sql_client import get_sql_conn
import threading
from task_cleaner import clean_completed_tasks

app = FastAPI()

# Inicia limpiador de tareas completadas en segundo plano
threading.Thread(target=clean_completed_tasks, args=(10,), daemon=True).start()

redis_conn = get_redis()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/nodes")
def get_nodes():
    nodes = []
    for key in redis_conn.keys("node:*:resources"):
        node_id = key.split(":")[1]
        data = redis_conn.get(key)
        if data:
            res = json.loads(data)
            res['id'] = node_id
            nodes.append(res)
    return nodes

@app.get("/api/tasks")
def get_tasks():
    conn = get_sql_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 20 NodeID, TaskType, Result, Timestamp FROM TaskHistory ORDER BY Timestamp DESC")
    rows = cursor.fetchall()
    tasks = [{
        "node_id": row[0],
        "task_type": row[1],
        "result": row[2],
        "timestamp": row[3].strftime("%Y-%m-%d %H:%M:%S")
    } for row in rows]
    conn.close()
    return tasks

@app.get("/api/active-tasks")
def get_active_tasks():
    tasks = []
    for key in redis_conn.keys("node:*:tasks_active"):
        node_id = key.split(":")[1]
        tasks_active_data = redis_conn.hgetall(key)
        for task_id, task_json in tasks_active_data.items():
            task = json.loads(task_json)
            task.update({
                "node": node_id,
                "result": task.get("result", "PENDIENTE"),
                "type": task.get("type"),
            })
            tasks.append(task)
    return tasks
