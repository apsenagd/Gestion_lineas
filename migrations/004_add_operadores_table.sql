-- Crear tabla de operadores
CREATE TABLE IF NOT EXISTS operadores (
    id_operador INT AUTO_INCREMENT PRIMARY KEY,
    nombre_operador VARCHAR(100) NOT NULL UNIQUE,
    descripcion VARCHAR(255),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar operadores iniciales
INSERT INTO operadores (nombre_operador, descripcion) VALUES
('Movistar', 'Operador Movistar'),
('Claro', 'Operador Claro'),
('WOM', 'Operador WOM'),
('Entel', 'Operador Entel')
ON DUPLICATE KEY UPDATE nombre_operador = VALUES(nombre_operador);

-- Agregar columna id_operador a tabla lineas si no existe
ALTER TABLE lineas ADD COLUMN id_operador INT DEFAULT NULL AFTER id_plan;

-- Crear índice para id_operador
CREATE INDEX IF NOT EXISTS idx_lineas_id_operador ON lineas(id_operador);

-- Agregar relación de clave foránea (opcional, si deseas integridad referencial)
ALTER TABLE lineas ADD CONSTRAINT fk_lineas_operador 
FOREIGN KEY (id_operador) REFERENCES operadores(id_operador) 
ON DELETE SET NULL;
