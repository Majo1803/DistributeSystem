import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def get_sql_connection():
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('SQL_SERVER')};"
        f"DATABASE={os.getenv('SQL_DB')};"
        f"UID={os.getenv('SQL_USER')};"
        f"PWD={os.getenv('SQL_PASSWORD')}"
    )
    print(f"🧪 Conectando a base: {os.getenv('SQL_DB')} en {os.getenv('SQL_SERVER')} como {os.getenv('SQL_USER')}")
    return pyodbc.connect(conn_str)

def insert_task_log(node_id, task_type, result, timestamp):
    try:
        conn = get_sql_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO TaskHistory (NodeID, TaskType, Result, Timestamp)
            VALUES (?, ?, ?, ?)
        """, node_id, task_type, str(result), timestamp)
        conn.commit()
        conn.close()
        print(f"💾 Resultado guardado en SQL para nodo {node_id}")
    except Exception as e:
        print("❌ ERROR guardando resultado en SQL:", e)
