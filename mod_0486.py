import os
import hashlib
import tarfile
from datetime import datetime
import platform


def analizar_eicar_core(path):
    """Devuelve el hash MD5 del archivo y si coincide con EICAR."""
    if not os.path.isfile(path):
        raise FileNotFoundError("El archivo no existe.")
    hash_eicar = "44d88612fea8a8f36de82e1278abb02f"
    md5 = file_hash(path)
    return {"md5": md5, "es_eicar": md5 == hash_eicar}


def hardening_sistema_info():
    """Genera el texto explicativo del hardening según el sistema operativo."""
    so = platform.system()
    lineas = [f"Detectado sistema operativo: {so}"]
    if so == "Linux":
        lineas.append("Servicios recomendados para deshabilitar en Linux (ejecutar manualmente):")
        lineas.extend([
            "- bluetooth: sudo systemctl disable bluetooth",
            "- cups (impresoras): sudo systemctl disable cups",
            "- avahi-daemon (descubrimiento red): sudo systemctl disable avahi-daemon",
        ])
    elif so == "Windows":
        lineas.append("Servicios recomendados para deshabilitar en Windows (ejecutar manualmente en services.msc):")
        lineas.extend([
            "- Fax",
            "- Remote Registry",
            "- Bluetooth Support Service (si no se usa)",
        ])
    else:
        lineas.append("Sistema no reconocido para hardening.")
    lineas.append("⚠️ Recuerda documentar qué servicios deshabilitas y por qué.")
    return "\n".join(lineas)


def politicas_contrasenas_info():
    """Genera el texto con la guía de políticas de contraseñas."""
    so = platform.system()
    if so == "Windows":
        lineas = [
            "Para configurar políticas de contraseñas en Windows Server:",
            "1. Abre 'secpol.msc'",
            "2. Ve a Directivas de cuenta → Directiva de contraseñas",
            "3. Configura:",
            "   - Longitud mínima: 8 caracteres",
            "   - Complejidad: habilitada",
            "   - Caducidad: 30 días",
            "   - Bloqueo tras 5 intentos fallidos",
        ]
    else:
        lineas = ["En Linux, edita el archivo /etc/login.defs o usa PAM para definir políticas."]
    lineas.append("👉 Este paso requiere configuración manual por el administrador.")
    return "\n".join(lineas)


def backup_directorio_core(origen, destino):
    """Crea un backup comprimido y devuelve la ruta generada."""
    if not os.path.isdir(origen):
        raise NotADirectoryError("El directorio de origen no existe.")
    os.makedirs(destino, exist_ok=True)
    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(destino, f"backup_{fecha}.tar.gz")
    with tarfile.open(backup_file, "w:gz") as tar:
        tar.add(origen, arcname=os.path.basename(origen))
    return backup_file

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
    try:
        resultado = analizar_eicar_core(path)
        print("MD5 calculado:", resultado["md5"])
        if resultado["es_eicar"]:
            print("[ALERTA] Archivo coincide con la firma EICAR (debe ser detectado por el antivirus).")
        else:
            print("[OK] Archivo no coincide con EICAR.")
    except FileNotFoundError as exc:
        print(f"[ERROR] {exc}")

# ---------------------------
# 2. Hardening del sistema
# ---------------------------
def hardening_sistema():
    print(hardening_sistema_info())

# ---------------------------
# 3. Políticas de contraseñas (Windows Server)
# ---------------------------
def politicas_contrasenas():
    print(politicas_contrasenas_info())

# ---------------------------
# 4. Copias de seguridad automáticas
# ---------------------------
def backup_directorio():
    origen = input("Ruta del directorio a respaldar: ").strip()
    destino = input("Ruta donde guardar el backup: ").strip()
    try:
        backup_file = backup_directorio_core(origen, destino)
        print(f"[OK] Backup creado en: {backup_file}")
        print("👉 Para automatizar, añade este script a cron (Linux) o al Programador de Tareas (Windows).")
    except NotADirectoryError as exc:
        print(f"[ERROR] {exc}")
    except Exception as exc:
        print(f"[ERROR] No se pudo crear el backup: {exc}")

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
