#!/usr/bin/env python3
"""
scripts/test_smtp.py
Prueba envío SMTP usando la función `send_reset_email` de la app.

Uso:
  python scripts/test_smtp.py destino@example.com

El script carga las variables de entorno para SMTP (SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, SMTP_FROM).
"""
import sys
import os

if len(sys.argv) < 2:
    print('Uso: python scripts/test_smtp.py destino@example.com')
    sys.exit(2)

to = sys.argv[1]

# Import la función desde app (no ejecuta el servidor)
try:
    from app import send_reset_email
except Exception as e:
    print('Error importando send_reset_email desde app:', e)
    sys.exit(3)

reset_url = 'https://example.local/reset-test'
ok = send_reset_email(to, reset_url)
print('Envío OK' if ok else 'Envío FALLÓ')
