# Proyecto Integrador: Broker Tuple-Developers

### Link Planificación del Proyecto
https://docs.google.com/spreadsheets/d/1LL8X0-WoadNC5Rn-EOkjIRzQSmQNItS-e-FEEm2XIC8/edit?usp=sharing

### Colaboradores
- Juan Ignacio Moreno(JuanIgnaciom03)
- Jorge Antonio Marchisone(jmarchisone)(ScrumMaster)
- Martin Ernesto Olmedo(Martin-Olmedo98)
- Fabián Ricardo Perisset(FabianRicardoPerisset)
- Sabrina Loza(Saloza14)
- Facundo Lozano(facundoLozano0)
  
## Contexto 

El sistema fue diseñado para permitir a los usuarios gestionar sus inversiones en 
acciones del MERVAL. Los usuarios pueden ver sus portafolios, comprar y vender 
acciones, y obtener información sobre las cotizaciones de las acciones en las que están 
interesados. 

## Objetivo 

El objetivo del sistema es facilitar a los usuarios la administración de sus inversiones en 
acciones, proporcionando funcionalidades clave como la visualización del portafolio, la 
compra y venta de acciones, y la actualización de las cotizaciones de las acciones.


## Funcionamiento (Programación)

Para correr el proyecto, ingresar en la carpeta Programacion/BrokerApp y cargar en MySQL workbench el archivo:

```bash
tuple-developers.sql
```
Luego cargar datos de ejemplo:

```bash
datos_ejemplo_ai.sql
```
Configurar datos de usuario y clave MySQL en:
```bash
config.py
```
Por último ejecutar el archivo main.py:

```bash
python main.py
```
## Funciones

- Creación de usuario
- Login de usuario
- Ver datos de cuenta
- Ver portafolio
- Comprar acciones
- Vender acciones
- Cerrar sesión

