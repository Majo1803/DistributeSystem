import psutil
import json
import time
from coordinator.redis_client import get_redis_connection



def get_resource_status():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "net": psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    }

def start_monitoring(node_id):
    redis_conn = get_redis_connection()

    while True:
        status = get_resource_status()
        redis_conn.set(f"node:{node_id}:resources", json.dumps(status))
        time.sleep(5)
