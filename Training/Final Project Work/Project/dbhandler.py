#===db.py====
 
import mysql.connector
from logger import Logger

class DatabaseConnectionError (Exception):
    pass

class DatabaseConnection:
    def __init__(self):
        self.connection = None
        self.logger = Logger(self.__class__.__name__)
 
    def get_connection(self):
        if self.connection is None or not self.connection.is_connected():
            try:
                self.connection = mysql.connector.connect(
                    host="localhost",
                    database="student_db",
                    user="root",
                    password="kol@mind1",
                )
                self.logger.write_log("Database connection established", level="info")
            except Exception as e:
                self.connection = None
                self.logger.write_log(f"Database connection error: {e}", level="error")
                raise DatabaseConnectionError("Error connecting to the database")
            
                       
        return self.connection

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.logger.write_log("Closing database connection", level="info")
            self.connection.close()