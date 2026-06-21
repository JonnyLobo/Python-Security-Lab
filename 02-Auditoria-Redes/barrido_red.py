import socket

# 1. Definimos la red base (Tu vecindario VMware NAT)
red_base = "192.168.118."
puerto_tactico = 22

# 2. Definimos las casas que vamos a visitar (Rango de IPs)
# En VMware, el host físico suele ser el .1, el Gateway el .2, y las VMs desde el .128
rango_ips = list(range(1, 5)) + list(range(130, 135))

print(f"[*] Iniciando Reconocimiento de Red en la subred: {red_base}0/24")
print(f"[*] Buscando activos con el puerto {puerto_tactico} expuesto...\n")
print("-" * 50)

for terminacion in rango_ips:
    ip_objetivo = f"{red_base}{terminacion}"
    
    # Construimos el motor de conexión para cada IP
    motor_conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # TIEMPO DE RESPUESTA AGRESIVO: Si no responde en 0.1 segundos, pasamos a la siguiente IP.
    # En una red local, los milisegundos son suficientes. Esto evita que el script se cuelgue.
    motor_conexion.settimeout(0.1)
    
    # Intentamos la conexión
    codigo_respuesta = motor_conexion.connect_ex((ip_objetivo, puerto_tactico))
    
    if codigo_respuesta == 0:
        print(f"[+] ACTIVO ENCONTRADO -> {ip_objetivo} (Puerto {puerto_tactico} ABIERTO)")
        
    motor_conexion.close()

print("-" * 50)
print("[*] Barrido de red finalizado.")