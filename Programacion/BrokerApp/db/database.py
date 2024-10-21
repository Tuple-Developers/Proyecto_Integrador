importar mysql.connector
Error al importar desde mysql.connector
desde configuración importar DB_CONFIG


clase DatabaseConnection:
    @metodostatico
    definición obtener_conexión():
        intentar:
            conexión = mysql.connector.connect(**DB_CONFIG)
            conexión de retorno
        excepto Error como e:
            print(f"Error al conectar a la base de datos: {e}")
            devolver Ninguno
