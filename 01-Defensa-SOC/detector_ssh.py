import time
import re  # 1. Importamos la librería nativa de Expresiones Regulares de Python

archivo_log = "auth_simulado.log"
firma_ataque = "Failed password"

# 2. Definimos la fórmula arquitectónica de una IPv4
# \d significa "dígito". {1,3} significa "de 1 a 3 repeticiones". \. es el punto literal.
patron_ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

print(f"[*] Iniciando motor de extracción táctica en: {archivo_log}")
print("[*] Aislando direcciones IP hostiles...\n")
print("-" * 50)

try:
    with open(archivo_log, 'r') as log:
        for linea in log:
            if firma_ataque in linea:
                # 3. Le ordenamos al motor RegEx que busque el patrón matemático en la línea actual
                coincidencias = re.findall(patron_ip, linea)
                
                # Si el motor encontró al menos una IP, la extraemos y la mostramos
                if coincidencias:
                    ip_enemiga = coincidencias[0] # Tomamos el primer resultado encontrado
                    print(f"[ACCIÓN REQUERIDA] Bloquear IP en Firewall: {ip_enemiga}")
                    
                    time.sleep(0.5)

except FileNotFoundError:
    print(f"[ERROR] No se encontró el archivo de logs: {archivo_log}")

print("-" * 50)
print("[*] Análisis y extracción completados.")