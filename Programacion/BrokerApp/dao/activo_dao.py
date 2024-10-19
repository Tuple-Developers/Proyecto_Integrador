from db.database import DatabaseConnection


class ActivoDAO:
    @staticmethod
    def listar_activos():
        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor(dictionary=True)

            sql = "SELECT * FROM ACTIVO WHERE activo = TRUE"
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar activos: {e}")
            return None
        finally:
            if connection:
                connection.close()
