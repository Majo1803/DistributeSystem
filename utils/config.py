import os
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    "REDIS_HOST": os.getenv("REDIS_HOST", "localhost"),
    "REDIS_PORT": int(os.getenv("REDIS_PORT", 6379)),
    "SQL_SERVER": os.getenv("SQL_SERVER", "localhost"),
    "SQL_DB": os.getenv("SQL_DB", "MonitoreoBase"),
    "SQL_USER": os.getenv("SQL_USER", "admin"),
    "SQL_PASSWORD": os.getenv("SQL_PASSWORD", "admin"),
}
