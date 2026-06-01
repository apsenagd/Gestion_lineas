-- Recomendaciones de índices sugeridas por Copilot
CREATE INDEX idx_lineas_numero ON lineas(numero_linea);
CREATE INDEX idx_lineas_usuario ON lineas(id_usuario);
CREATE INDEX idx_lineas_estado ON lineas(id_estado);
CREATE INDEX idx_lineas_plan ON lineas(id_plan);
CREATE INDEX idx_lineas_ciudad ON lineas(id_ciudad);
CREATE INDEX idx_usuarios_nombre ON usuarios(nombre);
CREATE INDEX idx_ciudades_nombre ON ciudades(nombre_ciudad);
CREATE INDEX idx_planes_nombre ON planes(nombre_plan);
CREATE INDEX idx_tipos_nombre ON tipos_sim(nombre_tipo);
CREATE INDEX idx_estados_nombre ON estados_linea(nombre_estado);
