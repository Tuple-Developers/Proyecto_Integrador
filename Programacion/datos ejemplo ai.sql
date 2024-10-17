-- Insertar ejemplos en la tabla USUARIO
insert into
  usuario (email, cuil, nombre, apellido, password, saldo)
values
  (
    'juan.perez@example.com',
    '20-12345678-9',
    'Juan',
    'Perez',
    'password123',
    1000000
  ),
  (
    'maria.gomez@example.com',
    '27-87654321-0',
    'Maria',
    'Gomez',
    'password456',
    1000000
  ),
  (
    'carlos.lopez@example.com',
    '23-11223344-5',
    'Carlos',
    'Lopez',
    'password789',
    1000000
  ),
  (
    'ana.martinez@example.com',
    '24-55667788-1',
    'Ana',
    'Martinez',
    'password101',
    1000000
  ),
  (
    'luis.sanchez@example.com',
    '21-99887766-2',
    'Luis',
    'Sanchez',
    'password202',
    1000000
  );

-- Insertar ejemplos en la tabla ACTIVO
insert into
  activo (nombre, precio_compra, precio_venta)
values
  ('Acciones ABC', 100.00, 110.00),
  ('Bonos XYZ', 200.00, 210.00),
  ('Fondo Mutuo DEF', 150.00, 160.00),
  ('ETF GHI', 300.00, 310.00),
  ('Oro', 1800.00, 1850.00),
  ('Plata', 25.00, 27.00),
  ('Criptomoneda BTC', 45000.00, 46000.00),
  ('Criptomoneda ETH', 3000.00, 3100.00),
  ('Acciones JKL', 50.00, 55.00),
  ('Bonos MNO', 1000.00, 1050.00);

-- Insertar ejemplos en la tabla TRANSACCION
insert into
  transaccion (
    usuario_email,
    activo_id,
    tipo,
    cantidad,
    precio,
    comision,
    fecha
  )
values
  (
    'juan.perez@example.com',
    1,
    'compra',
    10,
    100.00,
    1.00,
    '2023-10-01 10:00:00'
  ),
  (
    'maria.gomez@example.com',
    2,
    'venta',
    5,
    200.00,
    2.00,
    '2023-10-02 11:00:00'
  ),
  (
    'carlos.lopez@example.com',
    3,
    'compra',
    8,
    150.00,
    1.50,
    '2023-10-03 12:00:00'
  ),
  (
    'ana.martinez@example.com',
    4,
    'venta',
    3,
    300.00,
    3.00,
    '2023-10-04 13:00:00'
  ),
  (
    'luis.sanchez@example.com',
    5,
    'compra',
    2,
    1800.00,
    18.00,
    '2023-10-05 14:00:00'
  ),
  (
    'juan.perez@example.com',
    6,
    'venta',
    20,
    25.00,
    0.25,
    '2023-10-06 15:00:00'
  ),
  (
    'maria.gomez@example.com',
    7,
    'compra',
    1,
    45000.00,
    450.00,
    '2023-10-07 16:00:00'
  ),
  (
    'carlos.lopez@example.com',
    8,
    'venta',
    4,
    3000.00,
    30.00,
    '2023-10-08 17:00:00'
  ),
  (
    'ana.martinez@example.com',
    9,
    'compra',
    15,
    50.00,
    0.50,
    '2023-10-09 18:00:00'
  ),
  (
    'luis.sanchez@example.com',
    10,
    'venta',
    7,
    1000.00,
    10.00,
    '2023-10-10 19:00:00'
  ),
  (
    'juan.perez@example.com',
    1,
    'venta',
    5,
    110.00,
    1.10,
    '2023-10-11 10:00:00'
  ),
  (
    'maria.gomez@example.com',
    2,
    'compra',
    10,
    210.00,
    2.10,
    '2023-10-12 11:00:00'
  ),
  (
    'carlos.lopez@example.com',
    3,
    'venta',
    4,
    160.00,
    1.60,
    '2023-10-13 12:00:00'
  ),
  (
    'ana.martinez@example.com',
    4,
    'compra',
    6,
    310.00,
    3.10,
    '2023-10-14 13:00:00'
  ),
  (
    'luis.sanchez@example.com',
    5,
    'venta',
    1,
    1850.00,
    18.50,
    '2023-10-15 14:00:00'
  ),
  (
    'juan.perez@example.com',
    6,
    'compra',
    25,
    27.00,
    0.27,
    '2023-10-16 15:00:00'
  ),
  (
    'maria.gomez@example.com',
    7,
    'venta',
    2,
    46000.00,
    460.00,
    '2023-10-17 16:00:00'
  ),
  (
    'carlos.lopez@example.com',
    8,
    'compra',
    3,
    3100.00,
    31.00,
    '2023-10-18 17:00:00'
  ),
  (
    'ana.martinez@example.com',
    9,
    'venta',
    10,
    55.00,
    0.55,
    '2023-10-19 18:00:00'
  ),
  (
    'luis.sanchez@example.com',
    10,
    'compra',
    5,
    1050.00,
    10.50,
    '2023-10-20 19:00:00'
  );