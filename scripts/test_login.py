#!/usr/bin/env python3
"""
scripts/test_login.py
Verifica username/email + password contra la tabla `admins` usando la misma lógica que la app.

Uso:
  python scripts/test_login.py <username_or_email> <password>

Devuelve código 0 si la contraseña coincide, 1 en caso contrario.
"""
import sys
import base64
import hashlib
import mysql.connector
from werkzeug.security import check_password_hash

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Mysql2026*',
    'database': 'gestion_lineas',
    'charset': 'utf8mb4',
    'use_unicode': True,
}


def manual_scrypt_verify(pwd, ph):
    try:
        # ph like: scrypt:32768:8:1$BASE64SALT$HEXHASH
        rest = ph[len('scrypt:'):]
        parts = rest.split('$')
        if len(parts) != 3:
            return False
        params = parts[0]
        salt_b64 = parts[1]
        hash_hex = parts[2]
        n_str, r_str, p_str = params.split(':')
        salt = base64.b64decode(salt_b64)
        dklen = len(hash_hex) // 2
        dk = hashlib.scrypt(pwd.encode('utf-8'), salt=salt, n=int(n_str), r=int(r_str), p=int(p_str), dklen=dklen)
        return dk.hex() == hash_hex
    except Exception:
        return False


def verify_password(pwd, ph):
    if not ph:
        return False
    if ph.startswith('scrypt:'):
        # try passlib if available
        try:
            from passlib.hash import scrypt as passlib_scrypt
            try:
                return passlib_scrypt.verify(pwd, ph)
            except Exception:
                return manual_scrypt_verify(pwd, ph)
        except Exception:
            return manual_scrypt_verify(pwd, ph)
    else:
        # fallback to werkzeug (pbkdf2, sha1, etc.)
        try:
            return check_password_hash(ph, pwd)
        except Exception:
            return False


def main():
    if len(sys.argv) < 3:
        print('Uso: python scripts/test_login.py <username_or_email> <password>')
        sys.exit(2)
    ident = sys.argv[1]
    pwd = sys.argv[2]
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cur = conn.cursor(dictionary=True)
        cur.execute('SELECT id_admin, username, email, nombre, activo, password_hash FROM admins WHERE username = %s OR email = %s LIMIT 1', (ident, ident))
        row = cur.fetchone()
        cur.close()
        conn.close()
    except Exception as e:
        print('Error conectando a la BD:', e)
        sys.exit(3)

    if not row:
        print('No se encontró usuario/email:', ident)
        sys.exit(1)

    print('Encontrado:', row.get('id_admin'), row.get('username'), 'activo=', row.get('activo'))
    ph = row.get('password_hash') or ''
    print('password_hash sample:', (ph[:60] + ('...' if len(ph)>60 else '')))
    ok = verify_password(pwd, ph)
    if ok:
        print('VERIFICACIÓN: OK')
        sys.exit(0)
    else:
        print('VERIFICACIÓN: FALLÓ')
        sys.exit(1)


if __name__ == '__main__':
    main()
