-- Crear tabla de configuraciones
CREATE TABLE IF NOT EXISTS config (
    id INT AUTO_INCREMENT PRIMARY KEY,
    clave VARCHAR(255) UNIQUE NOT NULL,
    valor TEXT
);

-- Insertar configuraciones SMTP por defecto (vacías)
INSERT INTO config (clave, valor) VALUES
('SMTP_HOST', ''),
('SMTP_PORT', '587'),
('SMTP_USER', ''),
('SMTP_PASS', ''),
('SMTP_FROM', ''),
('SMTP_TLS', '1')
ON DUPLICATE KEY UPDATE valor = VALUES(valor);