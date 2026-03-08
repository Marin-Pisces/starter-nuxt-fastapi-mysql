import os
import mysql.connector
from contextlib import contextmanager

# -----------------------------------------------------
# DB設定の取得
# -----------------------------------------------------
def get_db_config():
    return {
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASS", "root"),
        "host": os.getenv("DB_HOST", "db"),
        "port": os.getenv("DB_PORT", "3306"),
        "database": os.getenv("DB_NAME", "init")
    }

# -----------------------------------------------------
# DB接続マネージャー (Context Manager)
# -----------------------------------------------------
@contextmanager
def get_connection():
    con = mysql.connector.connect(**get_db_config())
    cursor = con.cursor(dictionary=True)

    try:
        yield cursor, con

    except Exception as e:
        con.rollback()
        raise e

    finally:
        cursor.close()
        con.close()