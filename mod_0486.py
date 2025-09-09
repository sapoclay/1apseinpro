import os
import hashlib
import tarfile
from datetime import datetime
import platform
import subprocess

# ---------------------------
# 1. Análisis de malware (EICAR)
# ---------------------------
def file_hash(path):
    """Calcula el hash MD5 de un fichero"""
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def analizar_eicar():
    path = input("Ruta del archivo a analizar (ej: muestras/eicar.com): ").strip()
    if not os.path.isfile(path):
        print("[ERROR] El archivo no existe.")
        return
    hash_eicar = "44d88612fea8a8f36de82e1278abb02f"
    md5 = file_hash(path)
    print("MD5 calculado:", md5)
    if md5 == hash_eicar:
        print("[ALERTA] Archivo coincide con la firma EICAR (debe ser detectado por el antivirus).")
    else:
        print("[OK] Archivo no coincide con EICAR.")

# ---------------------------
# 2. Hardening del sistema
# ---------------------------
def hardening_sistema():
    so = platform.system()
    print(f"Detectado sistema operativo: {so}")
    if so == "Linux":
        print("Servicios recomendados para deshabilitar en Linux (ejecutar manualmente):")
        print("- bluetooth: sudo systemctl disable bluetooth")
        print("- cups (impresoras): sudo systemctl disable cups")
        print("- avahi-daemon (descubrimiento red): sudo systemctl disable avahi-daemon")
    elif so == "Windows":
        print("Servicios recomendados para deshabilitar en Windows (ejecutar manualmente en services.msc):")
        print("- Fax")
        print("- Remote Registry")
        print("- Bluetooth Support Service (si no se usa)")
    else:
        print("Sistema no reconocido para hardening.")
    print("⚠️ Recuerda documentar qué servicios deshabilitas y por qué.")

# ---------------------------
# 3. Políticas de contraseñas (Windows Server)
# ---------------------------
def politicas_contrasenas():
    so = platform.system()
    if so == "Windows":
        print("Para configurar políticas de contraseñas en Windows Server:")
        print("1. Abre 'secpol.msc'")
        print("2. Ve a Directivas de cuenta → Directiva de contraseñas")
        print("3. Configura:")
        print("   - Longitud mínima: 8 caracteres")
        print("   - Complejidad: habilitada")
        print("   - Caducidad: 30 días")
        print("   - Bloqueo tras 5 intentos fallidos")
    else:
        print("En Linux, edita el archivo /etc/login.defs o usa PAM para definir políticas.")
    print("👉 Este paso requiere configuración manual por el administrador.")

# ---------------------------
# 4. Copias de seguridad automáticas
# ---------------------------
def backup_directorio():
    origen = input("Ruta del directorio a respaldar: ").strip()
    if not os.path.isdir(origen):
        print("[ERROR] El directorio no existe.")
        return

    destino = input("Ruta donde guardar el backup: ").strip()
    os.makedirs(destino, exist_ok=True)

    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(destino, f"backup_{fecha}.tar.gz")

    with tarfile.open(backup_file, "w:gz") as tar:
        tar.add(origen, arcname=os.path.basename(origen))

    print(f"[OK] Backup creado en: {backup_file}")
    print("👉 Para automatizar, añade este script a cron (Linux) o al Programador de Tareas (Windows).")

import os

# ---------------------------
# Menú principal
# ---------------------------
def menu():
    while True:
        print("\n\033[1;33m--- Menú Seguridad en equipos informáticos ---\033[0m")
        print("1. Análisis de malware (EICAR)")
        print("2. Hardening del sistema operativo")
        print("3. Políticas de contraseñas")
        print("4. Copia de seguridad de directorio")
        print("5. Volver al menú principal")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            analizar_eicar()
        elif opcion == "2":
            hardening_sistema()
        elif opcion == "3":
            politicas_contrasenas()
        elif opcion == "4":
            backup_directorio()
        elif opcion == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Volviendo al menú principal...")
            break
        else:
            print("[ERROR] Opción no válida.")

if __name__ == "__main__":
    menu()
