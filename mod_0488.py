import re
from datetime import datetime
import os


def phishing_analisis_core(ruta):
    if not os.path.isfile(ruta):
        raise FileNotFoundError("El archivo no existe.")
    with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
        contenido = f.read()
    alertas = []
    if "http://" in contenido:
        alertas.append("Contiene enlace no seguro (HTTP).")
    if "@" in contenido:
        alertas.append("Revisa remitente sospechoso.")
    if "adjunto" in contenido.lower():
        alertas.append("Posible adjunto sospechoso.")
    return alertas


def registro_incidente_core(titulo, descripcion, archivo):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(f"{fecha} | {titulo}\n")
        f.write(f"{descripcion}\n")
        f.write("-" * 40 + "\n")
    return archivo


def analisis_forense_core(log_path):
    if not os.path.isfile(log_path):
        raise FileNotFoundError("El archivo no existe.")
    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        logs = f.read()
    fallos = re.findall(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)", logs)
    conteo = {ip: fallos.count(ip) for ip in set(fallos)}
    return conteo


def plan_respuesta_core(archivo):
    with open(archivo, "w", encoding="utf-8") as f:
        f.write("Plan de respuesta a incidentes\n")
        f.write("==============================\n")
        f.write("1. Detección\n2. Contención\n3. Erradicación\n4. Recuperación\n")
        f.write("Cada fase debe documentarse con acciones específicas.\n")
    return archivo

# ---------------------------
# 1. Caso práctico de phishing
# ---------------------------
def phishing_analisis():
    print("\n--- Caso práctico de phishing ---")
    print("Introduce un correo simulado (puede ser un .txt con ejemplo de phishing):")
    ruta = input("Ruta del archivo: ").strip()
    try:
        alertas = phishing_analisis_core(ruta)
        if alertas:
            print("[ALERTA] Indicadores de phishing encontrados:")
            for a in alertas:
                print(f"- {a}")
        else:
            print("[OK] No se detectaron indicadores obvios de phishing.")
    except FileNotFoundError as exc:
        print(f"[ERROR] {exc}")

# ---------------------------
# 2. Registro de incidentes
# ---------------------------
def registro_incidente():
    print("\n--- Registro de incidente ---")
    titulo = input("Título del incidente: ").strip()
    descripcion = input("Descripción breve: ").strip()
    archivo = input("Nombre del archivo de registro (ej: incidente.txt): ").strip()
    try:
        registro_incidente_core(titulo, descripcion, archivo)
        print(f"[OK] Incidente registrado en {archivo}")
    except Exception as exc:
        print(f"[ERROR] No se pudo registrar el incidente: {exc}")

# ---------------------------
# 3. Análisis forense básico
# ---------------------------
def analisis_forense():
    print("\n--- Análisis forense básico ---")
    log_path = input("Ruta del archivo de logs (ej: auth.log): ").strip()
    try:
        conteo = analisis_forense_core(log_path)
        if conteo:
            print("IPs con intentos de acceso fallidos:")
            for ip, cantidad in conteo.items():
                print(f"- {ip} ({cantidad} intentos)")
        else:
            print("[OK] No se detectaron intentos fallidos en los logs.")
    except FileNotFoundError as exc:
        print(f"[ERROR] {exc}")

# ---------------------------
# 4. Plan de respuesta
# ---------------------------
def plan_respuesta():
    print("\n--- Plan de respuesta ---")
    archivo = input("Nombre del archivo para el plan de respuesta (ej: plan_respuesta.txt): ").strip()
    try:
        plan_respuesta_core(archivo)
        print(f"[OK] Plan de respuesta generado en {archivo}")
    except Exception as exc:
        print(f"[ERROR] No se pudo generar el plan: {exc}")

# ---------------------------
# Menú principal del módulo 0488
# ---------------------------
def menu():
    while True:
        print("\n\033[1;33m--- 0488: Xestión de incidentes de seguridade informática ---\033[0m")
        print("1. Caso práctico de phishing")
        print("2. Registro de incidentes")
        print("3. Análisis forense básico (logs)")
        print("4. Plan de respuesta a incidentes")
        print("5. Volver al menú principal")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            phishing_analisis()
        elif opcion == "2":
            registro_incidente()
        elif opcion == "3":
            analisis_forense()
        elif opcion == "4":
            plan_respuesta()
        elif opcion == "5":
            break
        else:
            print("[ERROR] Opción no válida.")