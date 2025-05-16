import random
import json
from redis_client import get_redis_connection

redis_conn = get_redis_connection()

def get_available_nodes():
    keys = redis_conn.keys("node:*:resources")
    nodes = []

    for key in keys:
        data = redis_conn.get(key)
        if data:
            resource = json.loads(data)
            if resource['cpu'] < 85:  # solo nodos con menos de 85% de CPU
                nodes.append((key.split(":")[1], resource['cpu']))
    return sorted(nodes, key=lambda x: x[1])  # nodo con menor CPU primero

def generate_random_task():
    task_type = random.choice(["sum", "subtract", "multiply", "divide", "sqrt"])

    if task_type == "sqrt":
        return {
            "type": task_type,
            "payload": random.randint(1, 10000)  # solo un número para raíz
        }
    else:
        return {
            "type": task_type,
            "payload": {
                "a": random.randint(1, 10000),
                "b": random.randint(1, 100)
            }
        }

def assign_task(task_type=None):
    nodes = get_available_nodes()
    if not nodes:
        print("❌ No hay nodos disponibles.")
        return None

    node_id = nodes[0][0]

    # Si no se especifica tipo, generar uno aleatorio con tipos variados
    if task_type is None:
        task_data = generate_random_task()
    else:
        if task_type == "sqrt":
            task_data = {
                "type": "sqrt",
                "payload": random.randint(1, 10000)
            }
        else:
            task_data = {
                "type": task_type,
                "payload": {
                    "a": random.randint(1, 10000),
                    "b": random.randint(1, 100)
                }
            }

    redis_conn.rpush(f"node:{node_id}:tasks", json.dumps(task_data))
    print(f"🟢 Tarea '{task_data['type']}' enviada al nodo {node_id}")
    return node_id, task_data
