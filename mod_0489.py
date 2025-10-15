import os
from cryptography.fernet import Fernet


def cifrar_archivo_core(ruta):
    if not os.path.isfile(ruta):
        raise FileNotFoundError("El archivo no existe.")
    key = Fernet.generate_key()
    cipher = Fernet(key)
    with open(ruta, "rb") as f:
        data = f.read()
    token = cipher.encrypt(data)
    archivo_cifrado = ruta + ".enc"
    with open(archivo_cifrado, "wb") as f:
        f.write(token)
    return {"archivo": archivo_cifrado, "clave": key.decode()}


def descifrar_archivo_core(ruta, clave):
    if not os.path.isfile(ruta):
        raise FileNotFoundError("El archivo no existe.")
    cipher = Fernet(clave.encode() if isinstance(clave, str) else clave)
    with open(ruta, "rb") as f:
        data = f.read()
    original = cipher.decrypt(data)
    archivo_descifrado = ruta.replace(".enc", ".dec")
    with open(archivo_descifrado, "wb") as f:
        f.write(original)
    return archivo_descifrado


def generar_mfa_key():
    return Fernet.generate_key().decode()

# ---------------------------
# 1. Cifrado de archivos con Fernet
# ---------------------------
def cifrado_archivo():
    ruta = input("Ruta del archivo a cifrar: ").strip()
    try:
        resultado = cifrar_archivo_core(ruta)
        print(f"[OK] Archivo cifrado guardado en {resultado['archivo']}")
        print(f"Clave para descifrado: {resultado['clave']} (guárdala en lugar seguro)")
    except FileNotFoundError as exc:
        print(f"[ERROR] {exc}")
    except Exception as exc:
        print(f"[ERROR] No se pudo cifrar el archivo: {exc}")

# ---------------------------
# 2. Descifrado de archivos
# ---------------------------
def descifrado_archivo():
    ruta = input("Ruta del archivo cifrado: ").strip()
    key_input = input("Introduce la clave de descifrado: ").strip()
    try:
        archivo_descifrado = descifrar_archivo_core(ruta, key_input)
        print(f"[OK] Archivo descifrado guardado en {archivo_descifrado}")
    except FileNotFoundError as exc:
        print(f"[ERROR] {exc}")
    except Exception as exc:
        print(f"[ERROR] No se pudo descifrar el archivo: {exc}")

# ---------------------------
# 3. Generación de clave para autenticación multifactor
# ---------------------------
def generacion_mfa():
    print("\n--- Generación de clave simulada para MFA ---")
    key = generar_mfa_key()
    print(f"Clave generada para MFA (simulada): {key}")
    print("Se puede usar para integrar con Google Authenticator u otra app TOTP.")

# ---------------------------
# Menú principal del módulo 0489
# ---------------------------
def menu():
    while True:
        print("\n\033[1;33m--- 0489: Sistemas seguros de acceso e transmisión de datos ---\033[0m")
        print("1. Cifrar archivo (Fernet AES)")
        print("2. Descifrar archivo")
        print("3. Generación de clave MFA simulada")
        print("4. Volver al menú principal")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            cifrado_archivo()
        elif opcion == "2":
            descifrado_archivo()
        elif opcion == "3":
            generacion_mfa()
        elif opcion == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("[ERROR] Opción no válida.")
