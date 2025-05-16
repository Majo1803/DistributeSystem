from coordinator.redis_client import get_redis_connection

def clear_redis():
    redis_conn = get_redis_connection()
    redis_conn.flushall()
    print("Redis limpiado exitosamente.")

if __name__ == "__main__":
    clear_redis()
