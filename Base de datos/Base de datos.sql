CREATE TABLE USUARIO (
    email VARCHAR(100) PRIMARY KEY,
    cuil VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(40) NOT NULL,
    apellido VARCHAR(40) NOT NULL,
    password VARCHAR(255) NOT NULL,
    saldo DECIMAL(15, 2) NOT NULL DEFAULT 1000000
);

CREATE TABLE PORTAFOLIO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_email VARCHAR(100) UNIQUE NOT NULL,
    total_invertido DECIMAL(15, 2) NOT NULL DEFAULT 0,
    rendimiento_total DECIMAL(15, 2) NOT NULL DEFAULT 0,
    FOREIGN KEY (usuario_email) REFERENCES USUARIO(email)
);

CREATE TABLE ACTIVO (
    id INT PRIMARY KEY auto_increment,
    nombre VARCHAR(100) NOT NULL,
    simbolo VARCHAR(10) NOT NULL,
    descripcion TEXT,
    precio_compra DECIMAL(12,2) NOT NULL,
    precio_venta DECIMAL(12,2) NOT NULL,
    volumen_disponible INTEGER NOT NULL,
    ultima_actualizacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT true
);

CREATE TABLE PORTAFOLIO_ACTIVO (
    portafolio_id INT NOT NULL,
    activo_id INT NOT NULL,
    cantidad INT NOT NULL,
    PRIMARY KEY (portafolio_id, activo_id),
    FOREIGN KEY (portafolio_id) REFERENCES PORTAFOLIO(id),
    FOREIGN KEY (activo_id) REFERENCES ACTIVO(id)
);

-- Cuidado al crear, tipo solo puede ser compra o venta
CREATE TABLE TRANSACCION (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_email  VARCHAR(100) NOT NULL,
    activo_id INT NOT NULL,
    tipo ENUM('compra', 'venta') NOT NULL,
    cantidad INT NOT NULL,
    precio DECIMAL(15, 2) NOT NULL,
    comision DECIMAL(15, 2) NOT NULL,
    fecha DATETIME NOT NULL,
    FOREIGN KEY (usuario_email) REFERENCES USUARIO(email),
    FOREIGN KEY (activo_id) REFERENCES ACTIVO(id)
);

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
    '23-23456789-1',
    'Carlos',
    'Lopez',
    'password789',
    1000000
),
(
    'ana.martinez@example.com',
    '24-34567890-2',
    'Ana',
    'Martinez',
    'password012',
    1000000
),
(
    'luis.sanchez@example.com',
    '25-45678901-3',
    'Luis',
    'Sanchez',
    'password345',
    1000000
),
(
    'laura.diaz@example.com',
    '26-56789012-4',
    'Laura',
    'Diaz',
    'password678',
    1000000
),
(
    'jose.fernandez@example.com',
    '27-67890123-5',
    'Jose',
    'Fernandez',
    'password901',
    1000000
),
(
    'marta.garcia@example.com',
    '28-78901234-6',
    'Marta',
    'Garcia',
    'password234',
    1000000
),
(
    'pedro.ramirez@example.com',
    '29-89012345-7',
    'Pedro',
    'Ramirez',
    'password567',
    1000000
),
(
    'sofia.torres@example.com',
    '30-90123456-8',
    'Sofia',
    'Torres',
    'password890',
    1000000
);

insert into
portafolio (usuario_email, total_invertido, rendimiento_total)
values
('juan.perez@example.com', 500000, 50000),
('maria.gomez@example.com', 300000, 30000),
('carlos.lopez@example.com', 200000, 20000),
('ana.martinez@example.com', 400000, 40000),
('luis.sanchez@example.com', 100000, 10000),
('laura.diaz@example.com', 600000, 60000),
('jose.fernandez@example.com', 700000, 70000),
('marta.garcia@example.com', 800000, 80000),
('pedro.ramirez@example.com', 900000, 90000),
('sofia.torres@example.com', 1000000, 100000);
insert into
activo (
    nombre,
    simbolo,
    descripcion,
    precio_compra,
    precio_venta,
    volumen_disponible
)
values
('Grupo Financiero Galicia', 'GGAL', 'Banco líder en Argentina', 5800, 5900, 2880),
('Ternium Argentina', 'TXAR', 'Productor de acero', 790, 800, 1020),
('Pampa Energía', 'PAMP', 'Empresa de energía', 3020, 3100, 1990),
('Telecom Argentina', 'TECO2', 'Proveedor de telecomunicaciones', 1820, 1920, 419),
('Aluar', 'ALUA', 'Productor de aluminio', 843, 849, 810),
('BBVA Banco Francés', 'BBAR', 'Banco comercial', 4650, 4715, 222),
('Banco Macro', 'BMA', 'Banco comercial', 8650, 8850, 318),
('Edenor', 'EDN', 'Distribuidor de electricidad', 1340, 1375, 4722),
('Mirgor', 'MIRG', 'Fabricante de productos electrónicos', 20425, 21800, 5740),
('Central Puerto', 'CEPU', 'Generador de energía eléctrica', 1205, 1250, 1270);

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
    1500.00,
    15.00,
    '2023-10-01 10:00:00'
),
(
    'maria.gomez@example.com',
    2,
    'venta',
    5,
    1250.00,
    12.50,
    '2023-10-02 11:00:00'
),
(
    'carlos.lopez@example.com',
    3,
    'compra',
    2,
    6600.00,
    66.00,
    '2023-10-03 12:00:00'
),
(
    'ana.martinez@example.com',
    4,
    'venta',
    3,
    2100.00,
    21.00,
    '2023-10-04 13:00:00'
),
(
    'luis.sanchez@example.com',
    5,
    'compra',
    1,
    2800.00,
    28.00,
    '2023-10-05 14:00:00'
),
(
    'laura.diaz@example.com',
    6,
    'venta',
    4,
    1400.00,
    14.00,
    '2023-10-06 15:00:00'
),
(
    'jose.fernandez@example.com',
    7,
    'compra',
    6,
    1200.00,
    12.00,
    '2023-10-07 16:00:00'
),
(
    'marta.garcia@example.com',
    8,
    'venta',
    7,
    3500.00,
    35.00,
    '2023-10-08 17:00:00'
),
(
    'pedro.ramirez@example.com',
    9,
    'compra',
    8,
    4800.00,
    48.00,
    '2023-10-09 18:00:00'
),
(
    'sofia.torres@example.com',
    10,
    'venta',
    9,
    450.00,
    4.50,
    '2023-10-10 19:00:00'
);

insert into
portafolio_activo (portafolio_id, activo_id, cantidad)
values
(1, 1, 10),
(2, 2, 5),
(3, 3, 2),
(4, 4, 3),
(5, 5, 1),
(6, 6, 4),
(7, 7, 6),
(8, 8, 7),
(9, 9, 8),
(10, 10, 9);