import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mysql2026*',
    database='gestion_lineas'
)

cur = db.cursor(dictionary=True)
cur.execute('SELECT id_estado, nombre_estado FROM estados_linea ORDER BY id_estado')
rows = cur.fetchall()
print("\n=== TODOS LOS ESTADOS ===")
for r in rows:
    print(f"  ID {r['id_estado']}: {r['nombre_estado']}")

cur.close()
db.close()
