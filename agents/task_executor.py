import time
import json
import random
from coordinator.redis_client import get_redis_connection

def simulate_intensive_operation(op_type, payload):
    print(f"DEBUG - Operación: {op_type}, Payload: {payload}")
    time.sleep(3)  

    a = payload.get("a") if isinstance(payload, dict) else payload
    b = payload.get("b") if isinstance(payload, dict) else None

    if op_type == "sum":
        return a + b
    elif op_type == "subtract":
        return a - b
    elif op_type == "multiply":
        return a * b
    elif op_type == "divide":
        if b == 0:
            return "Error: división por cero"
        return round(a / b, 2)
    elif op_type == "sqrt":
        return round(a ** 0.5, 2)
    else:
        print(f"DEBUG - Tipo de operación desconocido: {op_type}")
        return None

def start_executing_tasks(node_id):
    redis_conn = get_redis_connection()

    operaciones = ["sum", "subtract", "multiply", "divide", "sqrt"]

    while True:
        task_json = redis_conn.lpop(f"node:{node_id}:tasks")
        if task_json:
            task = json.loads(task_json)
            task_id = str(time.time())  # ID único basado en timestamp

            # Elige aleatoriamente el tipo de operación (ignora el 'type' recibido)
            op_type = random.choice(operaciones)

            # Ajustar el payload según la operación seleccionada
            if op_type == "sqrt":
                # Si es raíz, solo un número (a)
                payload = {"a": task["payload"] if isinstance(task["payload"], int) else task["payload"].get("a")}
            else:
                # Para otras operaciones, aseguramos que payload tenga 'a' y 'b'
                if isinstance(task["payload"], dict):
                    payload = task["payload"]
                else:
                    payload = {
                        "a": task["payload"],
                        "b": random.randint(1, 100)  # si no venía con 'b', generamos uno random
                    }

            # Guardar como tarea activa (resultado pendiente)
            task_active_key = f"node:{node_id}:tasks_active"
            task_active_data = {
                "type": op_type,
                "payload": payload,
                "result": "PENDIENTE",
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            redis_conn.hset(task_active_key, task_id, json.dumps(task_active_data))

            # Ejecutar operación
            result = simulate_intensive_operation(op_type, payload)
            print(f"✅ Tarea ejecutada en nodo {node_id}: {payload} → {result}")

            # Actualizar resultado
            task_active_data["result"] = result
            redis_conn.hset(task_active_key, task_id, json.dumps(task_active_data))

            # Guardar en cola de resultados
            log = {
                "node": node_id,
                "type": op_type,
                "result": result,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            redis_conn.rpush("results:queue", json.dumps(log))

        time.sleep(2)
