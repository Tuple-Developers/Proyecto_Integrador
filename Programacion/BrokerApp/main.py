from dao.usuario_dao import UsuarioDAO
from dao.activo_dao import ActivoDAO
from dao.portafolio_dao import PortafolioDAO
from dao.transaccion_dao import TransaccionDAO
from models.usuario import Usuario
from models.transaccion import Transaccion
from decimal import Decimal


def mostrar_menu_principal():
    print("\n=== ISPC Investment Platform ===")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    return input("Seleccione una opción: ")


def mostrar_menu_usuario():
    print("\n=== Menú Usuario ===")
    print("1. Ver datos de la cuenta")
    print("2. Ver portafolio")
    print("3. Comprar acciones")
    print("4. Vender acciones")
    print("5. Ver historial de transacciones")
    print("6. Cerrar sesión")
    return input("Seleccione una opción: ")


def registrar_usuario():
    print("\n=== Registro de Usuario ===")
    email = input("Email: ")
    cuil = input("CUIL: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    password = input("Contraseña: ")

    usuario = Usuario(email, cuil, nombre, apellido, password, 1000000)
    if UsuarioDAO.registrar(usuario):
        print("Usuario registrado exitosamente")
    else:
        print("Error al registrar usuario")


def iniciar_sesion():
    print("\n=== Inicio de Sesión ===")
    email = input("Email: ")
    password = input("Contraseña: ")

    usuario = UsuarioDAO.login(email, password)
    if usuario:
        print(f"\nBienvenido {usuario.nombre}!")
        return usuario
    else:
        print("Credenciales inválidas")
        return None


def mostrar_datos_cuenta(usuario):
    print("\n=== Datos de la Cuenta ===")
    print(f"Nombre: {usuario.nombre} {usuario.apellido}")
    print(f"Email: {usuario.email}")
    print(f"Saldo disponible: ${usuario.saldo:,.2f}")


def mostrar_portafolio(usuario):
    portafolio = PortafolioDAO.obtener_portafolio(usuario.email)
    if portafolio:
        print("\n=== Portafolio de Inversiones ===")
        rendimiento_total = 0
        for activo in portafolio:
            if activo["cantidad"] and activo["cantidad"] > 0:
                print(f"\nID: {activo['id_activo']}")
                print(f"\nActivo: {activo['nombre']} ({activo['simbolo']})")
                print(f"Cantidad: {activo['cantidad']}")
                print(f"Precio de compra: ${activo['precio_compra']:,.2f}")
                print(f"Precio de venta actual: ${activo['precio_venta']:,.2f}")
                rendimiento_acciones = (activo["precio_venta"] * activo["cantidad"]) - (
                    activo["precio_compra"] * activo["cantidad"]
                )
                print(f"Rendimiento: ${rendimiento_acciones:,.2f}")
                rendimiento_total += rendimiento_acciones
        print(f"\n\nRendimiento total: {rendimiento_total}")
    else:
        print("No se encontraron activos en el portafolio")


def comprar_acciones(usuario):
    activos = ActivoDAO.listar_activos()
    if not activos:
        print("No hay activos disponibles para comprar")
        return

    print("\n=== Activos Disponibles (Comisión 1,5%) ===")
    for activo in activos:
        print(f"\nID: {activo['id']}")
        print(f"Nombre: {activo['nombre']} ({activo['simbolo']})")
        print(f"Precio de compra: ${activo['precio_compra']:,.2f}")
        # CORRECCION MOSTRAR VOLUMEN PROFE IVANA
        print(f"Volumen disponible: {activo['volumen_disponible']}")

    try:
        activo_id = int(input("\nIngrese el ID del activo a comprar: "))
        cantidad = int(input("Ingrese la cantidad de acciones: "))

        activo_seleccionado = next((a for a in activos if a["id"] == activo_id), None)
        if not activo_seleccionado:
            print("Activo no encontrado")
            return

        # CORRECCION VOLUMEN DE ACCIONES PROFE IVANA
        if cantidad > activo_seleccionado["volumen_disponible"]:
            print("No hay suficiente volumen disponible")
            return

        precio_total = activo_seleccionado["precio_compra"] * cantidad
        comision = precio_total * Decimal("0.015")  # 1.5% de comisión
        total_con_comision = precio_total + comision

        if total_con_comision > usuario.saldo:
            print("Saldo insuficiente")
            return

        transaccion = Transaccion(
            usuario.email,
            activo_id,
            "compra",
            cantidad,
            activo_seleccionado["precio_compra"],
            comision,
        )

        if TransaccionDAO.realizar_transaccion(transaccion):
            print("Compra realizada exitosamente")
            usuario.saldo -= total_con_comision
        else:
            print("Error al realizar la compra")

    except ValueError:
        print("Por favor ingrese valores numéricos válidos")


def vender_acciones(usuario):
    portafolio = PortafolioDAO.obtener_portafolio(usuario.email)
    if not portafolio:
        print("No tiene activos para vender")
        return

    print("\n=== Sus Activos (Comisión 1,5%) ===")
    activos_disponibles = {}
    for activo in portafolio:
        if activo["cantidad"] and activo["cantidad"] > 0:
            activos_disponibles[activo["id_activo"]] = activo
            print(f"\nID: {activo['id_activo']}")
            print(f"Nombre: {activo['nombre']} ({activo['simbolo']})")
            print(f"Cantidad disponible: {activo['cantidad']}")
            print(f"Precio de venta: ${activo['precio_venta']:,.2f}")

    if not activos_disponibles:
        print("No tiene activos para vender")
        return

    try:
        activo_id = int(input("\nIngrese el ID del activo a vender: "))
        if activo_id not in activos_disponibles:
            print("Activo no encontrado en su portafolio")
            return

        activo = activos_disponibles[activo_id]
        cantidad = int(
            input(
                f"Ingrese la cantidad de acciones a vender (máx. {activo['cantidad']}): "
            )
        )

        if cantidad > activo["cantidad"]:
            print("No tiene suficientes acciones")
            return

        precio_total = activo["precio_venta"] * cantidad
        comision = precio_total * Decimal("0.015")  # 1.5% de comisión
        total_con_comision = precio_total - comision

        transaccion = Transaccion(
            usuario.email,
            activo_id,
            "venta",
            cantidad,
            activo["precio_venta"],
            comision,
        )

        if TransaccionDAO.realizar_transaccion(transaccion):
            print("Venta realizada exitosamente")
            usuario.saldo += total_con_comision
        else:
            print("Error al realizar la venta")

    except ValueError:
        print("Por favor ingrese valores numéricos válidos")


def mostrar_historial_transacciones(usuario):
    historial = TransaccionDAO.obtener_historial(usuario.email)
    if historial:
        print("\n=== Historial de Transacciones ===")
        for transaccion in historial:
            print(f"\nFecha: {transaccion['fecha']}")
            print(f"Activo: {transaccion['activo_nombre']} ({transaccion['simbolo']})")
            print(f"Tipo: {transaccion['tipo'].upper()}")
            print(f"Cantidad: {transaccion['cantidad']}")
            print(f"Precio unitario: ${transaccion['precio']:,.2f}")
            print(f"Comisión: ${transaccion['comision']:,.2f}")
            monto_total = transaccion["precio"] * transaccion["cantidad"]
            if transaccion["tipo"] == "compra":
                monto_total += transaccion["comision"]
                print(f"Monto total pagado: ${monto_total:,.2f}")
            else:
                monto_total -= transaccion["comision"]
                print(f"Monto total recibido: ${monto_total:,.2f}")
    else:
        print("No se encontraron transacciones")


def main():
    usuario_actual = None

    while True:
        if not usuario_actual:
            opcion = mostrar_menu_principal()
            if opcion == "1":
                registrar_usuario()
            elif opcion == "2":
                usuario_actual = iniciar_sesion()
            elif opcion == "3":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida")
        else:
            opcion = mostrar_menu_usuario()
            if opcion == "1":
                mostrar_datos_cuenta(usuario_actual)
            elif opcion == "2":
                mostrar_portafolio(usuario_actual)
            elif opcion == "3":
                comprar_acciones(usuario_actual)
            elif opcion == "4":
                vender_acciones(usuario_actual)
            elif opcion == "5":
                mostrar_historial_transacciones(usuario_actual)
            elif opcion == "6":
                usuario_actual = None
                print("Sesión cerrada")
            else:
                print("Opción inválida")


if __name__ == "__main__":
    main()
