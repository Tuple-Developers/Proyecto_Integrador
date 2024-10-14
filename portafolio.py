class Portafolio:
    def __init__(self, db):
        self.db = db

    def obtener_datos(self, email):
        query = """
        SELECT u.saldo, p.total_invertido, p.rendimiento_total
        FROM USUARIO u
        JOIN PORTAFOLIO p ON u.email = p.usuario_email
        WHERE u.email = %s
        """
        return self.db.fetch_one(query, (email,))

    def listar_activos(self, email):
        query = """
        SELECT a.nombre, pa.cantidad, a.precio_compra, a.precio_venta,
               (a.precio_venta - a.precio_compra) * pa.cantidad as rendimiento,
                a.id
        FROM PORTAFOLIO_ACTIVO pa
        JOIN ACTIVO a ON pa.activo_id = a.id
        JOIN PORTAFOLIO p ON pa.portafolio_id = p.id
        WHERE p.usuario_email = %s
        """
        return self.db.fetch_all(query, (email,))

    def actualizar_total_invertido(self, email, monto):
        query = """
        UPDATE PORTAFOLIO
        SET total_invertido = total_invertido + %s
        WHERE usuario_email = %s
        """
        self.db.execute_query(query, (monto, email))

    def actualizar_rendimiento_total(self, email):
        query = """
        UPDATE PORTAFOLIO p
        SET rendimiento_total = (
            SELECT SUM((a.precio_venta - a.precio_compra) * pa.cantidad)
            FROM PORTAFOLIO_ACTIVO pa
            JOIN ACTIVO a ON pa.activo_id = a.id
            WHERE pa.portafolio_id = p.id
        )
        WHERE p.usuario_email = %s
        """
        self.db.execute_query(query, (email,))
