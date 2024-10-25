--Consultas de update
UPDATE USUARIO
SET saldo = saldo + 5000
WHERE email = 'juan.perez@example.com';

UPDATE USUARIO
SET apellido = 'Rodriguez'
WHERE email = 'maria.gomez@example.com';

UPDATE USUARIO
SET password = 'newpassword123'
WHERE email = 'carlos.lopez@example.com';

UPDATE ACTIVO
SET precio_compra = precio_compra * 1.05, precio_venta = precio_venta * 1.05
WHERE simbolo = 'TXAR';

UPDATE ACTIVO
SET precio_compra = precio_compra * 0.95, precio_venta = precio_venta * 0.95
WHERE simbolo = 'BBAR';

--Muestra todas las acciones compradas de todos los usuarios, y con que precio.
SELECT u.nombre, u.apellido, p.usuario_email, pa.cantidad, a.id as id_activo, a.nombre, a.simbolo, a.precio_compra, a.precio_venta 
FROM PORTAFOLIO p
LEFT JOIN PORTAFOLIO_ACTIVO pa ON p.id = pa.portafolio_id
LEFT JOIN ACTIVO a ON pa.activo_id = a.id
INNER JOIN usuario u ON p.usuario_email = u.email

--Muestra los usuarios que mas transacciones realizan. Puede usarse para aplicar alguna campaña de marketing.
SELECT u.nombre, u.apellido, u.email, 
COUNT(t.id) AS cantidad_transacciones
FROM USUARIO u
LEFT JOIN TRANSACCION t ON u.email = t.usuario_email
GROUP BY u.email, u.nombre, u.apellido
ORDER BY cantidad_transacciones DESC;

--Mostrar la cantidad todal de transacciones que se han realizado por cada activo. Permite conocer las acciones más populares.
SELECT a.nombre, a.simbolo, 
COUNT(t.id) AS cantidad_transacciones
FROM ACTIVO a
LEFT JOIN TRANSACCION t ON a.id = t.activo_id
GROUP BY a.id, a.nombre, a.simbolo;