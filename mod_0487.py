import os
import subprocess


def ejecutar_nmap(host):
    """Ejecuta nmap -sV sobre host y devuelve el resultado en texto."""
    try:
        result = subprocess.run(["nmap", "-sV", host], capture_output=True, text=True, check=False)
        if result.returncode == 0:
            return result.stdout
        return result.stdout + "\n" + result.stderr
    except FileNotFoundError:
        raise FileNotFoundError("nmap no está instalado o no se encuentra en PATH.")


def simulacion_auditoria_info():
    checklist = {
        "Usuarios": ["root", "admin", "test"],
        "Permisos": ["/home/usuario -> 755", "/etc/shadow -> 600"],
        "Servicios": ["ssh: activo", "ftp: deshabilitado"],
        "Parches aplicados": ["Kernel actualizado", "OpenSSH actualizado"],
    }
    lineas = ["Crea un checklist de auditoría para un servidor ficticio.", "Ejemplo de campos:"]
    for k, v in checklist.items():
        lineas.append(f"{k}: {v}")
    lineas.append("Puedes guardar esta información en un archivo .txt para documentar.")
    return "\n".join(lineas)


def prueba_contrasenas_info():
    return "\n".join([
        "⚠️ Este ejercicio requiere John the Ripper o similar.",
        "Pasos sugeridos:",
        "1. Coloca un archivo de hashes (ej: hashes.txt) con contraseñas de prueba.",
        "2. Ejecuta en terminal:",
        "   john --wordlist=diccionario.txt hashes.txt",
        "3. Documenta las contraseñas débiles encontradas.",
    ])


def generar_informe_auditoria(archivo):
    with open(archivo, "w") as f:
        f.write("Informe de auditoría\n")
        f.write("====================\n")
        f.write("Vulnerabilidades detectadas:\n- Ejemplo: Puerto 21 abierto\n")
        f.write("Nivel de criticidad:\n- Media\n")
        f.write("Recomendaciones:\n- Deshabilitar FTP si no se usa\n")

# ---------------------------
# 1. Escaneo de vulnerabilidades
# ---------------------------
def escaneo_vulnerabilidades():
    print("\n--- Escaneo de vulnerabilidades ---")
    ip = input("Introduce la IP o host a auditar (ej: 127.0.0.1): ").strip()
    print("⚠️ Recuerda tener permisos para escanear esta red/host")
    print("Opciones:")
    print("1. Escaneo con nmap (Python lanzará comando básico)")
    print("2. Escaneo con OpenVAS (requiere configuración externa)")

    opcion = input("Selecciona opción: ").strip()
    if opcion == "1":
        print(f"Escaneando {ip} con nmap...")
        try:
            salida = ejecutar_nmap(ip)
            print(salida)
        except FileNotFoundError as exc:
            print(f"[ERROR] {exc}")
    elif opcion == "2":
        print("Abre OpenVAS/GVM en tu navegador para escanear la IP y documentar resultados.")
    else:
        print("[ERROR] Opción no válida.")

# ---------------------------
# 2. Simulación de auditoría
# ---------------------------
def simulacion_auditoria():
    print("\n--- Simulación de auditoría ---")
    print(simulacion_auditoria_info())

# ---------------------------
# 3. Prueba de contraseñas débiles
# ---------------------------
def prueba_contrasenas():
    print("\n--- Prueba de contraseñas débiles ---")
    print(prueba_contrasenas_info())

# ---------------------------
# 4. Informe de auditoría
# ---------------------------
def informe_auditoria():
    print("\n--- Informe de auditoría ---")
    print("Crea un informe redactando:")
    print("- Vulnerabilidades detectadas")
    print("- Nivel de criticidad (Baja, Media, Alta)")
    print("- Recomendaciones de mitigación")
    archivo = input("Nombre del archivo de informe (ej: informe.txt): ").strip()
    try:
        generar_informe_auditoria(archivo)
        print(f"[OK] Informe creado en {archivo}")
    except Exception as exc:
        print(f"[ERROR] No se pudo crear el informe: {exc}")

import os

# ---------------------------
# Menú principal del módulo 0487
# ---------------------------
def menu():
    while True:
        print("\n\033[1;33m--- 0487: Auditoría de seguridade informática ---\033[0m")
        print("1. Escaneo de vulnerabilidades (nmap/OpenVAS)")
        print("2. Simulación de auditoría (checklist servidor ficticio)")
        print("3. Prueba de contraseñas débiles (John the Ripper)")
        print("4. Informe de auditoría")
        print("5. Volver al menú principal")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            escaneo_vulnerabilidades()
        elif opcion == "2":
            simulacion_auditoria()
        elif opcion == "3":
            prueba_contrasenas()
        elif opcion == "4":
            informe_auditoria()
        elif opcion == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("[ERROR] Opción no válida.")