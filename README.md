# Broker de Acciones

### Colaboradores
- Juan Ignacio Moreno.
- Jorge Antonio Marchisone(jmarchisone)
- Martin Ernesto Olmedo
- Fabián Ricardo Perisset(FabianRicardoPerisset)

## Descripción

Esta aplicación simula un broker de acciones, permitiendo a los usuarios gestionar sus cuentas, comprar y vender acciones, y consultar sus transacciones. Está construida en Python y utiliza un enfoque orientado a objetos para modelar los diferentes componentes del sistema.

## Estructura del Proyecto

- `Usuario`: Clase que representa a un usuario del broker.
- `Accion`: Clase que representa una acción en el mercado.
- `Transaccion`: Clase que representa una transacción de compra o venta de acciones.
- `Broker`: Clase que gestiona usuarios, acciones y transacciones.
- `Mercado`: Clase que gestiona la lista de acciones disponibles y sus precios.

## Funcionalidades

### Usuario
- Crear un nuevo usuario con un balance inicial.
- Depositar y retirar fondos de la cuenta del usuario.
- Mostrar el balance y el portafolio del usuario.
- Comprar y vender acciones.
- Consultar el historial de transacciones.

### Accion
- Crear una nueva acción con un ticker y un precio inicial.
- Actualizar el precio de una acción.

### Transaccion
- Registrar una transacción de compra o venta.

### Broker
- Agregar usuarios y acciones al sistema.
- Gestionar la compra y venta de acciones para los usuarios.
- Consultar el historial de transacciones de los usuarios.

### Mercado
- Actualizar los precios de las acciones en tiempo real.

## Instalación

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/broker-de-acciones.git
    ```
2. Navegar al directorio del proyecto:
    ```bash
    cd broker-de-acciones
    ```
3. Instalar las dependencias necesarias (si las hubiera). Para este proyecto básico, no hay dependencias externas.

## Uso

Aquí hay un ejemplo de cómo usar las clases en un script de Python:

```python
from datetime import datetime

# Crear instancia del broker
broker = Broker()

# Agregar usuarios
broker.agregar_usuario("Alice", 10000)
broker.agregar_usuario("Bob", 5000)

# Agregar acciones
broker.agregar_accion("AAPL", 150)
broker.agregar_accion("GOOGL", 2800)

# Comprar acciones
broker.comprar_accion("Alice", "AAPL", 10)
broker.comprar_accion("Bob", "GOOGL", 2)

# Vender acciones
broker.vender_accion("Alice", "AAPL", 5)

# Mostrar información del usuario
usuario_alice = broker.usuarios["Alice"]
usuario_alice.mostrar_balance()
usuario_alice.mostrar_portafolio()

# Consultar historial de transacciones
broker.consultar_transacciones()
