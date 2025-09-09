import os
from cryptography.fernet import Fernet

# ---------------------------
# 1. Cifrado de archivos con Fernet
# ---------------------------
def cifrado_archivo():
    ruta = input("Ruta del archivo a cifrar: ").strip()
    if not os.path.isfile(ruta):
        print("[ERROR] El archivo no existe.")
        return

    key = Fernet.generate_key()
    cipher = Fernet(key)

    with open(ruta, "rb") as f:
        data = f.read()

    token = cipher.encrypt(data)
    archivo_cifrado = ruta + ".enc"
    with open(archivo_cifrado, "wb") as f:
        f.write(token)

    print(f"[OK] Archivo cifrado guardado en {archivo_cifrado}")
    print(f"Clave para descifrado: {key.decode()} (guárdala en lugar seguro)")

# ---------------------------
# 2. Descifrado de archivos
# ---------------------------
def descifrado_archivo():
    ruta = input("Ruta del archivo cifrado: ").strip()
    if not os.path.isfile(ruta):
        print("[ERROR] El archivo no existe.")
        return
    key_input = input("Introduce la clave de descifrado: ").strip().encode()
    cipher = Fernet(key_input)

    with open(ruta, "rb") as f:
        data = f.read()

    try:
        original = cipher.decrypt(data)
    except Exception as e:
        print(f"[ERROR] No se pudo descifrar el archivo: {e}")
        return

    archivo_descifrado = ruta.replace(".enc", ".dec")
    with open(archivo_descifrado, "wb") as f:
        f.write(original)
    print(f"[OK] Archivo descifrado guardado en {archivo_descifrado}")

# ---------------------------
# 3. Generación de clave para autenticación multifactor
# ---------------------------
def generacion_mfa():
    print("\n--- Generación de clave simulada para MFA ---")
    key = Fernet.generate_key()
    print(f"Clave generada para MFA (simulada): {key.decode()}")
    print("Se puede usar para integrar con Google Authenticator u otra app TOTP.")

import os

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
