import socket
import time

# 1. Definimos el objetivo físico (La IP de tu Módem/Router)
objetivo = "172.16.0.1"

# 2. Puertos tácticos de infraestructura: 
# 21 (FTP), 22 (SSH), 23 (Telnet - ¡Peligroso si está abierto!), 80 (HTTP Admin), 443 (HTTPS), 8080 (Admin alternativo)
puertos_a_escanear = [21, 22, 23, 80, 443, 8080]

print(f"[*] Iniciando Auditoría de Red Física en el Gateway: {objetivo}")
print("-" * 50)

for puerto in puertos_a_escanear:
    motor_conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Tiempo de espera corto para red local
    motor_conexion.settimeout(0.5)
    
    codigo_respuesta = motor_conexion.connect_ex((objetivo, puerto))
    
    if codigo_respuesta == 0:
        print(f"[ALERTA DE SUPERFICIE] Puerto {puerto} -> ABIERTO (Servicio expuesto en el Módem)")
    else:
        print(f"[INFO] Puerto {puerto} -> Cerrado o Filtrado")
        
    motor_conexion.close()
    time.sleep(0.5)

print("-" * 50)
print("[*] Auditoría del Módem finalizada.")