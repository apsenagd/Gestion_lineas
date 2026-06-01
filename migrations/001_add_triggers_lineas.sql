-- Triggers to keep fecha_modificacion updated on INSERT/UPDATE
-- Run with caution and backup the DB first.

DELIMITER $$
CREATE TRIGGER trg_lineas_before_insert
BEFORE INSERT ON lineas FOR EACH ROW
BEGIN
  SET NEW.fecha_modificacion = NOW();
END$$

CREATE TRIGGER trg_lineas_before_update
BEFORE UPDATE ON lineas FOR EACH ROW
BEGIN
  SET NEW.fecha_modificacion = NOW();
END$$
DELIMITER ;
