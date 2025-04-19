import pyodbc
from utils.config import CONFIG

def get_sql_connection():
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={CONFIG['SQL_SERVER']};"
        f"DATABASE={CONFIG['SQL_DB']};"
        f"UID={CONFIG['SQL_USER']};"
        f"PWD={CONFIG['SQL_PASSWORD']}"
    )
    return pyodbc.connect(conn_str)

def insert_task_log(node_id, task_type, result, timestamp):
    conn = get_sql_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO TaskHistory (NodeID, TaskType, Result, Timestamp)
        VALUES (?, ?, ?, ?)
    """, node_id, task_type, result, timestamp)
    conn.commit()
    conn.close()
