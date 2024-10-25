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