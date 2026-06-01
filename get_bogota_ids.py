#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mysql2026*",
        database="gestion_lineas"
    )
    cur = db.cursor(dictionary=True)
    
    # Get Bogotá city ID
    print("=== CIUDADES ===")
    cur.execute("SELECT id_ciudad, nombre_ciudad FROM ciudades WHERE LOWER(nombre_ciudad) LIKE '%bogot%'")
    for row in cur.fetchall():
        print(f"ID: {row['id_ciudad']}, Ciudad: {row['nombre_ciudad']}")
    
    # Get Bogotá regional ID  
    print("\n=== REGIONALES ===")
    cur.execute("SELECT id_regional, nombre_regional FROM regionales WHERE LOWER(nombre_regional) LIKE '%bogot%'")
    for row in cur.fetchall():
        print(f"ID: {row['id_regional']}, Regional: {row['nombre_regional']}")
        
    cur.close()
    db.close()
except Error as e:
    print(f"Error: {e}")
