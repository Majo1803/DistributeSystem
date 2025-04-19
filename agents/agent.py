from agents.monitor import start_monitoring
from agents.task_executor import start_executing_tasks
import threading
import sys

def main():
    if len(sys.argv) < 2:
        print("❌ Debes especificar el ID del nodo (ej: python -m agents.agent nodo1)")
        return

    node_id = sys.argv[1]
    print(f"🚀 Agente '{node_id}' iniciado...")

    t1 = threading.Thread(target=start_monitoring, args=(node_id,))
    t2 = threading.Thread(target=start_executing_tasks, args=(node_id,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
