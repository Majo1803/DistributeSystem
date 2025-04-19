import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
from task_scheduler import assign_task
from result_processor import start_result_processor
from database import insert_task_log
import threading


def main():
    print("🚀 Coordinador iniciado...")

    while True:
        task_type = "operation-intensive"  # Se puede hacer aleatorio o por consola
        result = assign_task(task_type)

        if result:
            node_id, task = result
            insert_task_log(node_id, task['type'], "PENDIENTE", time.strftime("%Y-%m-%d %H:%M:%S"))

        time.sleep(10)  # cada 10 segundos asigna nueva tarea

if __name__ == "__main__":
    main()
