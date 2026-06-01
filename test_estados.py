import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mysql2026*',
    database='gestion_lineas'
)

cur = db.cursor(dictionary=True)
cur.execute("SELECT id_estado, nombre_estado FROM estados_linea WHERE LOWER(nombre_estado) IN ('activa', 'cesionada')")
rows = cur.fetchall()
print("Estados encontrados:")
for r in rows:
    print(f"  ID: {r['id_estado']}, Nombre: {r['nombre_estado']}")

cur.close()
db.close()
