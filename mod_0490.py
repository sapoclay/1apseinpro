import psutil
import time
import os

# ---------------------------
# 1. Monitorización de CPU y memoria
# ---------------------------
def monitor_recursos():
    print("\n--- Monitorización de recursos (Ctrl+C para salir) ---")
    try:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            mem = psutil.virtual_memory().percent
            print(f"CPU: {cpu}% | Memoria: {mem}%")
            if cpu > 80 or mem > 80:
                print("[ALERTA] Consumo alto de recursos")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nMonitorización detenida.")

# ---------------------------
# 2. Monitorización de servicios simulada
# ---------------------------
def monitor_servicios():
    import platform
    print("\n--- Monitorización de servicios ---")
    servicios = ["ssh", "nginx", "mysql", "docker"]
    so = platform.system()
    if so == "Linux":
        from shutil import which
        if which("systemctl"):
            for s in servicios:
                try:
                    import subprocess
                    result = subprocess.run(["systemctl", "is-active", s], capture_output=True, text=True)
                    estado = result.stdout.strip()
                    if estado == "active":
                        print(f"Servicio {s}: \033[1;32mactivo\033[0m")
                    elif estado == "inactive":
                        print(f"Servicio {s}: \033[1;31minactivo\033[0m")
                    else:
                        print(f"Servicio {s}: {estado}")
                except Exception as e:
                    print(f"Servicio {s}: error ({e})")
        elif which("service"):
            for s in servicios:
                try:
                    import subprocess
                    result = subprocess.run(["service", s, "status"], capture_output=True, text=True)
                    if "is running" in result.stdout or "active (running)" in result.stdout:
                        print(f"Servicio {s}: \033[1;32mactivo\033[0m")
                    else:
                        print(f"Servicio {s}: \033[1;31minactivo\033[0m")
                except Exception as e:
                    print(f"Servicio {s}: error ({e})")
        else:
            print("No se encontró systemctl ni service para comprobar servicios.")
    else:
        print("Monitorización real de servicios solo implementada para Linux.")

# ---------------------------
# 3. Creación de logs centralizados simulada
# ---------------------------
def gestion_logs():
    print("\n--- Gestión de logs simulada ---")
    ruta = input("Ruta donde guardar log centralizado: ").strip()
    try:
        os.makedirs(ruta, exist_ok=True)
        archivo = os.path.join(ruta, "central_log.txt")
        with open(archivo, "w") as f:
            f.write("Registro centralizado de servicios (simulado)\n")
            f.write("===============================\n")
            f.write("Todos los eventos y alertas se centralizan aquí.\n")
        print(f"[OK] Log centralizado creado en {archivo}")
    except PermissionError:
        print(f"[ERROR] No tienes permisos para crear la carpeta '{ruta}'. Elige una ruta dentro de tu carpeta de usuario o del proyecto.")
    except Exception as e:
        print(f"[ERROR] No se pudo crear el log: {e}")

import os

# ---------------------------
# Menú principal del módulo 0490
# ---------------------------
def menu():
    while True:
        print("\n\033[1;33m--- 0490: Xestión de servizos no sistema informático ---\033[0m")
        print("1. Monitorización de CPU y memoria")
        print("2. Monitorización de servicios simulada")
        print("3. Gestión de logs centralizados simulada")
        print("4. Volver al menú principal")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            monitor_recursos()
        elif opcion == "2":
            monitor_servicios()
        elif opcion == "3":
            gestion_logs()
        elif opcion == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("[ERROR] Opción no válida.")
