import time
import json
import random
from coordinator.redis_client import get_redis_connection

def simulate_intensive_operation(data):
    time.sleep(3)  # simula operación intensa
    return data * random.randint(2, 10)

def start_executing_tasks(node_id):
    redis_conn = get_redis_connection()

    while True:
        task_json = redis_conn.lpop(f"node:{node_id}:tasks")
        if task_json:
            task = json.loads(task_json)
            result = simulate_intensive_operation(task['payload'])
            print(f"✅ Tarea ejecutada en nodo {node_id}: {task['payload']} → {result}")

            log = {
                "node": node_id,
                "type": task['type'],
                "result": result,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            redis_conn.rpush("results:queue", json.dumps(log))  # cola de resultados
        time.sleep(2)
