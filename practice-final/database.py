import mysql.connector
import os

def create_connection():
    return mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user='root',
            password=os.environ.get("DB_PASSWD")
        )

createDBQuery = """
CREATE DATABASE IF NOT EXISTS testg1;
USE testg1;
CREATE TABLE IF NOT EXISTS engs (Name VARCHAR(20), LastName VARCHAR(20), Role VARCHAR(20));
"""

insertEngQuery = "INSERT INTO engs (Name, LastName, Role) VALUES (%s, %s, %s)"

class Database:
    def __init__(self):
        self.db = create_connection()
        self.cursor = self.db.cursor()
        self.cursor.execute(createDBQuery)
        self.cursor.close()
        self.db.close()

        self.db = create_connection()
        self.cursor = self.db.cursor()
        self.cursor.execute("USE testg1;")
    
    def get_engs(self):
        self.cursor.execute("SELECT * FROM engs")
        return self.cursor.fetchall()
    
    def add_eng(self, insert_values):
        self.cursor.execute(insertEngQuery, insert_values)
        self.db.commit()

