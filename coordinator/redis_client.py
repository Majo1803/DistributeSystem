import redis
from utils.config import CONFIG

def get_redis_connection():
    return redis.Redis(host=CONFIG['REDIS_HOST'], port=CONFIG['REDIS_PORT'], decode_responses=True)
