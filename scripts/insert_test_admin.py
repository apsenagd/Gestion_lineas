#!/usr/bin/env python3
import mysql.connector
from werkzeug.security import generate_password_hash

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Mysql2026*',
    'database': 'gestion_lineas',
}
USERNAME = 'testadmin'
EMAIL = 'testadmin@local'
NOMBRE = 'Test Admin'
PASSWORD = 'TestPass123!'

try:
    db = mysql.connector.connect(**DB_CONFIG)
    cur = db.cursor()
    pw = generate_password_hash(PASSWORD, method='pbkdf2:sha256')
    cur.execute("INSERT INTO admins (username,password_hash,email,nombre,activo) VALUES (%s,%s,%s,%s,1)", (USERNAME, pw, EMAIL, NOMBRE))
    db.commit()
    print('Inserted id', cur.lastrowid)
    cur.close()
    db.close()
except Exception as e:
    print('Error inserting admin:', e)
