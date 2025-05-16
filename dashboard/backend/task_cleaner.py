import time
import json
from redis_client import get_redis

def clean_completed_tasks(expire_seconds=10):
    redis_conn = get_redis()

    while True:
        for key in redis_conn.keys("node:*:tasks_active"):
            tasks = redis_conn.hgetall(key)
            for task_id, task_json in tasks.items():
                task = json.loads(task_json)
                if task.get("result") != "PENDIENTE":
                    task_time = time.mktime(time.strptime(task["timestamp"], "%Y-%m-%d %H:%M:%S"))
                    age = time.time() - task_time
                    if age > expire_seconds:
                        redis_conn.hdel(key, task_id)
                        print(f"🗑️ Tarea {task_id} eliminada de {key} tras {int(age)} seg")
        time.sleep(5)
