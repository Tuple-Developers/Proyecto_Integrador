from db.database import DatabaseConnection


class PortafolioDAO:
    @staticmethod
    def obtener_portafolio(email):
        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor(dictionary=True)

            sql = """
                SELECT p.*, pa.cantidad, a.id as id_activo, a.nombre, a.simbolo, a.precio_compra, a.precio_venta
                FROM PORTAFOLIO p
                LEFT JOIN PORTAFOLIO_ACTIVO pa ON p.id = pa.portafolio_id
                LEFT JOIN ACTIVO a ON pa.activo_id = a.id
                WHERE p.usuario_email = %s
            """
            cursor.execute(sql, (email,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener portafolio: {e}")
            return None
        finally:
            if connection:
                connection.close()
