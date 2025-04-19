import random
import json
from redis_client import get_redis_connection
import json
redis_conn = get_redis_connection()

def get_available_nodes():
    keys = redis_conn.keys("node:*:resources")
    nodes = []

    for key in keys:
        data = redis_conn.get(key)
        if data:
            resource = json.loads(data)
            if resource['cpu'] < 85:  # sólo si CPU < 85%
                nodes.append((key.split(":")[1], resource['cpu']))
    return sorted(nodes, key=lambda x: x[1])  # menos CPU primero

def assign_task(task_type):
    nodes = get_available_nodes()
    if not nodes:
        print("No hay nodos disponibles.")
        return None

    node_id = nodes[0][0]  # nodo con menor uso de CPU
    task_data = {
        "type": task_type,
        "payload": random.randint(1000, 9999)
    }
    redis_conn.rpush(f"node:{node_id}:tasks", json.dumps(task_data))
    print(f"🟢 Tarea '{task_type}' enviada al nodo {node_id}")
    return node_id, task_data
