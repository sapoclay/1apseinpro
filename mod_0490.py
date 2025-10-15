import psutil
import time
import os
import platform
import subprocess
from shutil import which


def snapshot_recursos(intervalo=1):
    """Devuelve un diccionario con los porcentajes de CPU y memoria."""
    if intervalo is None:
        cpu = psutil.cpu_percent(interval=None)
    else:
        cpu = psutil.cpu_percent(interval=intervalo)
    return {"cpu": cpu, "memoria": psutil.virtual_memory().percent}


def estados_servicios(servicios=None):
    """Obtiene el estado de una lista de servicios usando systemctl/service."""
    servicios = servicios or ["ssh", "nginx", "mysql", "docker"]
    resultados = []
    so = platform.system()
    if so != "Linux":
        raise RuntimeError("Monitorización real de servicios solo implementada para Linux.")
    if which("systemctl"):
        for servicio in servicios:
            try:
                result = subprocess.run(["systemctl", "is-active", servicio], capture_output=True, text=True)
                estado = result.stdout.strip() or result.stderr.strip() or "desconocido"
                resultados.append({"servicio": servicio, "estado": estado})
            except Exception as exc:
                resultados.append({"servicio": servicio, "estado": f"error: {exc}"})
    elif which("service"):
        for servicio in servicios:
            try:
                result = subprocess.run(["service", servicio, "status"], capture_output=True, text=True)
                texto = (result.stdout + result.stderr).lower()
                if "running" in texto:
                    estado = "active"
                elif "stopped" in texto or "inactive" in texto:
                    estado = "inactive"
                else:
                    estado = "desconocido"
                resultados.append({"servicio": servicio, "estado": estado})
            except Exception as exc:
                resultados.append({"servicio": servicio, "estado": f"error: {exc}"})
    else:
        raise FileNotFoundError("No se encontró systemctl ni service para comprobar servicios.")
    return resultados


def crear_log_centralizado(ruta):
    os.makedirs(ruta, exist_ok=True)
    archivo = os.path.join(ruta, "central_log.txt")
    with open(archivo, "w", encoding="utf-8") as f:
        f.write("Registro centralizado de servicios (simulado)\n")
        f.write("===============================\n")
        f.write("Todos los eventos y alertas se centralizan aquí.\n")
    return archivo

# ---------------------------
# 1. Monitorización de CPU y memoria
# ---------------------------
def monitor_recursos():
    print("\n--- Monitorización de recursos (Ctrl+C para salir) ---")
    try:
        while True:
            datos = snapshot_recursos(intervalo=1)
            cpu = datos["cpu"]
            mem = datos["memoria"]
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
    print("\n--- Monitorización de servicios ---")
    try:
        estados = estados_servicios()
        for info in estados:
            estado = info["estado"]
            if estado == "active":
                estado_texto = "\033[1;32mactivo\033[0m"
            elif estado == "inactive":
                estado_texto = "\033[1;31minactivo\033[0m"
            else:
                estado_texto = estado
            print(f"Servicio {info['servicio']}: {estado_texto}")
    except RuntimeError as exc:
        print(exc)
    except FileNotFoundError as exc:
        print(exc)
    except Exception as exc:
        print(f"[ERROR] No se pudo obtener el estado de los servicios: {exc}")

# ---------------------------
# 3. Creación de logs centralizados simulada
# ---------------------------
def gestion_logs():
    print("\n--- Gestión de logs simulada ---")
    ruta = input("Ruta donde guardar log centralizado: ").strip()
    try:
        archivo = crear_log_centralizado(ruta)
        print(f"[OK] Log centralizado creado en {archivo}")
    except PermissionError:
        print(f"[ERROR] No tienes permisos para crear la carpeta '{ruta}'. Elige una ruta dentro de tu carpeta de usuario o del proyecto.")
    except Exception as e:
        print(f"[ERROR] No se pudo crear el log: {e}")

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
