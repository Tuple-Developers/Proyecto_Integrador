import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG


class DatabaseConnection:
    @staticmethod
    def get_connection():
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            return connection
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
