#!/usr/bin/env python3
"""
scripts/create_admin.py
Inserta un admin inicial en la tabla `admins` usando contraseña hasheada (werkzeug).
Ajustar las credenciales de conexión a la BD si es necesario.

Uso:
  python scripts/create_admin.py

El script pedirá confirmación antes de insertar.
"""
import os
import sys
import mysql.connector
from werkzeug.security import generate_password_hash

# Configuración de conexión (coincide con la usada en app.py)
DB_CONFIG = {
    "host": os.environ.get('DB_HOST', 'localhost'),
    "user": os.environ.get('DB_USER', 'root'),
    "password": os.environ.get('DB_PASS', 'Mysql2026*'),
    "database": os.environ.get('DB_NAME', 'gestion_lineas'),
    "charset": 'utf8mb4',
    "use_unicode": True,
}

# Valores por defecto solicitados
DEFAULT_USERNAME = os.environ.get('ADMIN_USERNAME', 'apsenagd@megalabs.com.co')
DEFAULT_EMAIL = os.environ.get('ADMIN_EMAIL', 'apsenagd@megalabs.com.co')
DEFAULT_NOMBRE = os.environ.get('ADMIN_NOMBRE', 'Apsenagd')
# Contraseña proporcionada por el usuario en la conversación
DEFAULT_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'Gaby+seguro2026*')


def create_admin(username, email, nombre, plain_password):
    # Force pbkdf2:sha256 to avoid scrypt which may be unsupported/too memory-heavy
    pw_hash = generate_password_hash(plain_password, method='pbkdf2:sha256')
    db = None
    try:
        db = mysql.connector.connect(**DB_CONFIG)
        cur = db.cursor()
        cur.execute(
            """INSERT INTO admins (username, password_hash, email, nombre, activo)
               VALUES (%s, %s, %s, %s, 1)""",
            (username, pw_hash, email, nombre)
        )
        db.commit()
        print("Admin creado con id:", cur.lastrowid)
        cur.close()
    except mysql.connector.IntegrityError as e:
        print("Error: el usuario ya existe o violación de unicidad:", e)
        return False
    except Exception as e:
        print("Error creando admin:", e)
        return False
    finally:
        if db:
            db.close()
    return True


if __name__ == '__main__':
    print('Crear admin con los siguientes valores por defecto:')
    print('  username:', DEFAULT_USERNAME)
    print('  email:   ', DEFAULT_EMAIL)
    print('  nombre:  ', DEFAULT_NOMBRE)
    print('  password: (la contraseña se insertará como hash)')
    ans = input('Desea continuar e insertar este admin en la BD? [y/N]: ').strip().lower()
    if ans != 'y':
        print('Cancelado por el usuario.')
        sys.exit(0)
    ok = create_admin(DEFAULT_USERNAME, DEFAULT_EMAIL, DEFAULT_NOMBRE, DEFAULT_PASSWORD)
    if ok:
        print('Hecho. Por seguridad, elimine o proteja este script si no lo necesita más.')
    else:
        print('No se pudo crear el admin.')
