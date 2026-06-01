-- Índices para mejorar rendimiento de búsqueda y filtros en gestion_lineas

-- Índices en tabla lineas
CREATE INDEX IF NOT EXISTS idx_lineas_numero ON lineas(numero_linea);
CREATE INDEX IF NOT EXISTS idx_lineas_id_usuario ON lineas(id_usuario);
CREATE INDEX IF NOT EXISTS idx_lineas_id_jefe ON lineas(id_jefe);
CREATE INDEX IF NOT EXISTS idx_lineas_id_plan ON lineas(id_plan);
CREATE INDEX IF NOT EXISTS idx_lineas_id_tipo_sim ON lineas(id_tipo_sim);
CREATE INDEX IF NOT EXISTS idx_lineas_id_estado ON lineas(id_estado);
CREATE INDEX IF NOT EXISTS idx_lineas_id_regional ON lineas(id_regional);

-- Índices en tabla usuarios
CREATE INDEX IF NOT EXISTS idx_usuarios_nombre ON usuarios(nombre);
CREATE INDEX IF NOT EXISTS idx_usuarios_id_cargo ON usuarios(id_cargo);
CREATE INDEX IF NOT EXISTS idx_usuarios_id_ciudad ON usuarios(id_ciudad);
CREATE INDEX IF NOT EXISTS idx_usuarios_id_jefe ON usuarios(id_jefe);

-- Índices en tablas de catálogos
CREATE INDEX IF NOT EXISTS idx_cargos_nombre ON cargos(nombre_cargo);
CREATE INDEX IF NOT EXISTS idx_ciudades_nombre ON ciudades(nombre_ciudad);
CREATE INDEX IF NOT EXISTS idx_planes_nombre ON planes(nombre_plan);
CREATE INDEX IF NOT EXISTS idx_tipos_sim_nombre ON tipos_sim(nombre_tipo);
CREATE INDEX IF NOT EXISTS idx_estados_linea_nombre ON estados_linea(nombre_estado);
CREATE INDEX IF NOT EXISTS idx_jefes_nombre ON jefes(nombre_jefe);
CREATE INDEX IF NOT EXISTS idx_regionales_nombre ON regionales(nombre_regional);

-- Índice en tabla novedades_linea para búsquedas por línea
CREATE INDEX IF NOT EXISTS idx_novedades_linea_id ON novedades_linea(id_linea);
