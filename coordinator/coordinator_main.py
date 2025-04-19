import time
from coordinator.task_scheduler import assign_task
from coordinator.database import insert_task_log

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
