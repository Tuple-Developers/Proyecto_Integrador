from db.database import DatabaseConnection
from models.transaccion import Transaccion
from decimal import Decimal


class TransaccionDAO:
    @staticmethod
    def realizar_transaccion(transaccion):
        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()

            # Iniciar transacción
            connection.start_transaction()

            # Verificar el ID del activo
            print(f"ID del activo: {transaccion.activo_id}")

            # Registrar la transacción
            sql_transaccion = """
                INSERT INTO TRANSACCION 
                (usuario_email, activo_id, tipo, cantidad, precio, comision, fecha)
                VALUES (%s, %s, %s, %s, %s, %s, NOW())
            """
            values_transaccion = (
                transaccion.usuario_email,
                transaccion.activo_id,
                transaccion.tipo,
                transaccion.cantidad,
                transaccion.precio,
                transaccion.comision,
            )
            cursor.execute(sql_transaccion, values_transaccion)

            # Actualizar saldo del usuario
            monto_total = (
                transaccion.precio * transaccion.cantidad + transaccion.comision
            )
            if transaccion.tipo == "compra":
                sql_saldo = "UPDATE USUARIO SET saldo = saldo - %s WHERE email = %s"
            else:
                sql_saldo = "UPDATE USUARIO SET saldo = saldo + %s WHERE email = %s"

            cursor.execute(sql_saldo, (monto_total, transaccion.usuario_email))

            # Actualizar portafolio_activo
            if transaccion.tipo == "compra":
                sql_portafolio = """
                    INSERT INTO PORTAFOLIO_ACTIVO (portafolio_id, activo_id, cantidad)
                    VALUES ((SELECT id FROM PORTAFOLIO WHERE usuario_email = %s), %s, %s)
                    ON DUPLICATE KEY UPDATE cantidad = cantidad + %s
                """
                cursor.execute(
                    sql_portafolio,
                    (
                        transaccion.usuario_email,
                        transaccion.activo_id,
                        transaccion.cantidad,
                        transaccion.cantidad,
                    ),
                )
            else:
                sql_portafolio = """
                    UPDATE PORTAFOLIO_ACTIVO 
                    SET cantidad = cantidad - %s
                    WHERE portafolio_id = (SELECT id FROM PORTAFOLIO WHERE usuario_email = %s)
                    AND activo_id = %s
                """
                cursor.execute(
                    sql_portafolio,
                    (
                        transaccion.cantidad,
                        transaccion.usuario_email,
                        transaccion.activo_id,
                    ),
                )

            connection.commit()
            return True

        except Exception as e:
            if connection:
                connection.rollback()
            print(f"Error en la transacción: {e}")
            return False
        finally:
            if connection:
                cursor.close()
                connection.close()
