from db.database import DatabaseConnection
from models.usuario import Usuario


class UsuarioDAO:
    @staticmethod
    def registrar(usuario):
        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()

            sql = """INSERT INTO USUARIO (email, cuil, nombre, apellido, password, saldo) 
                        VALUES (%s, %s, %s, %s, %s, %s)"""
            values = (
                usuario.email,
                usuario.cuil,
                usuario.nombre,
                usuario.apellido,
                usuario.password,
                usuario.saldo,
            )

            cursor.execute(sql, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            return False
        finally:
            if connection:
                cursor.close()
                connection.close()

    @staticmethod
    def login(email, password):
        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor(dictionary=True)

            sql = "SELECT * FROM USUARIO WHERE email = %s AND password = %s"
            cursor.execute(sql, (email, password))

            user_data = cursor.fetchone()
            if user_data:
                return Usuario(**user_data)
            return None
        except Exception as e:
            print(f"Error en login: {e}")
            return None
        finally:
            if connection:
                cursor.close()
                connection.close()
