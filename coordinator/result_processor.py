import json
import time
from coordinator.redis_client import get_redis_connection
from coordinator.database import insert_task_log

def start_result_processor():
    redis_conn = get_redis_connection()

    print("📥 Procesador de resultados iniciado...")

    while True:
        result_json = redis_conn.lpop("results:queue")

        if result_json:
            try:
                result = json.loads(result_json)
                print(f"📦 Resultado recibido de nodo {result['node']}: {result['result']}")

                insert_task_log(
                    node_id=result['node'],
                    task_type=result['type'],
                    result=result['result'],
                    timestamp=result['timestamp']
                )

            except Exception as e:
                print("❌ Error procesando resultado:", e)

        time.sleep(1)
