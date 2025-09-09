
import sys
import os
import mod_0486
import mod_0487
import mod_0488
import mod_0489
import mod_0490

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    while True:
        print("\n\033[1;33m=== APLICACIÓN SEGURIDAD INFORMÁTICA ===\033[0m")
        print("1. 0486 - Seguridad en equipos informáticos")
        print("2. 0487 - Auditoría de seguridad informática")
        print("3. 0488 - Gestión de incidentes de seguridad informática")
        print("4. 0489 - Sistemas seguros de acceso y transmisión de datos")
        print("5. 0490 - Gestión de servicios en el sistema informático")
        print("6. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            mod_0486.menu()
        elif opcion == "2":
            limpiar_pantalla()
            mod_0487.menu()
        elif opcion == "3":
            limpiar_pantalla()
            mod_0488.menu()
        elif opcion == "4":
            limpiar_pantalla()
            mod_0489.menu()
        elif opcion == "5":
            limpiar_pantalla()
            mod_0490.menu()
        elif opcion == "6":
            print("Saliendo de la aplicación...")
            sys.exit(0)
        else:
            print("[ERROR] Opción no válida.")

if __name__ == "__main__":
    menu_principal()
