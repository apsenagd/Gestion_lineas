-- Backup recommended before running.
-- Fix regional for specific linea id = 192 by setting id_regional to the city's regional

START TRANSACTION;

SELECT 'Before' AS phase;
SELECT l.id_linea, l.numero_linea, l.id_ciudad, ci.nombre_ciudad, l.id_regional, r.nombre_regional
FROM lineas l
LEFT JOIN ciudades ci ON ci.id_ciudad = l.id_ciudad
LEFT JOIN regionales r ON r.id_regional = l.id_regional
WHERE l.id_linea = 192;

-- Update regional to match the city
UPDATE lineas l
JOIN ciudades ci ON ci.id_ciudad = l.id_ciudad
SET l.id_regional = ci.id_regional,
    l.fecha_modificacion = NOW()
WHERE l.id_linea = 192;

SELECT 'After' AS phase;
SELECT l.id_linea, l.numero_linea, l.id_ciudad, ci.nombre_ciudad, l.id_regional, r.nombre_regional
FROM lineas l
LEFT JOIN ciudades ci ON ci.id_ciudad = l.id_ciudad
LEFT JOIN regionales r ON r.id_regional = l.id_regional
WHERE l.id_linea = 192;

COMMIT;
