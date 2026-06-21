# Python Security Lab 🛡️

Entorno de laboratorio técnico enfocado en el desarrollo de herramientas personalizadas para operaciones defensivas (Blue Team) y auditoría de redes. Desarrollado nativamente en Python y ejecutado sobre un núcleo Linux (Ubuntu Server).

## 🏗️ Arquitectura del Laboratorio

El repositorio está clasificado en dos departamentos tácticos:

### 1. 01-Defensa-SOC (Monitoreo y Blue Team)
Herramientas diseñadas para la detección de intrusiones y análisis forense de registros del sistema:
* `detector_ssh.py`: Motor de monitoreo basado en expresiones regulares (RegEx) para identificar ataques de fuerza bruta en tiempo real contra el servicio SSH.
* `auth_simulado.log`: Artefacto de simulación de registros del sistema Linux (`/var/log/auth.log`) para pruebas controladas de ingesta de datos.

### 2. 02-Auditoria-Redes (Reconocimiento de Superficie)
Automatización táctica para la evaluación de exposición tanto en entornos virtualizados (NAT) como en infraestructura de red física:
* `escaner_puertos.py`: Escáner TCP automatizado para identificar servicios expuestos, configuraciones heredadas inseguras y facilitar técnicas de *Banner Grabbing*.
* `barrido_red.py`: Herramienta de descubrimiento de *hosts* (Ping Sweep) para mapear topologías de red y localizar activos vivos.

## 🛠️ Tecnologías y Entorno Operativo
* **Lenguaje:** Python 3 (Librerías Core: `re`, `socket`, `time`)
* **Entorno de Ejecución:** Ubuntu Server (CLI) aislado mediante hipervisor
* **Desarrollo y Versionado:** Visual Studio Code, Git, GitHub
* **Auditoría Complementaria:** Netcat (`nc`), Diagnóstico TCP/IP