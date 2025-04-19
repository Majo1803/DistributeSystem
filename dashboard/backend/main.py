from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from redis_client import get_redis
from sql_client import get_sql_conn

app = FastAPI()
redis_conn = get_redis()

# Permitir peticiones desde el dashboard en React
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
