import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="As@111521",  # Change to your MySQL password
        database="task_db"
    )

# Create database & table if not exist
conn = get_db_connection()
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS task_db")
cursor.execute("USE task_db")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
''')
conn.commit()
conn.close()
