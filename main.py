
import sys
import os
import re
import subprocess
import runpy
from pathlib import Path
from typing import Optional
import mod_0486
import mod_0487
import mod_0488
import mod_0489
import mod_0490


MODULOS_DIR = Path(__file__).parent / "EjerciciosPython"

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_ejercicios_python(modulo_nombre: Optional[str] = None):
    """Muestra el menú de ejercicios Python filtrado por módulo.
    
    Args:
        modulo_nombre: Nombre del módulo a filtrar (ej: 'modulo MF0487', 'modulo MF0488').
                      Si es None, muestra todos los ejercicios.
    """
    while True:
        limpiar_pantalla()
        
        # Filtrar ejercicios según el módulo especificado
        if modulo_nombre:
            modulo_dir = MODULOS_DIR / modulo_nombre
            if modulo_dir.exists():
                modulos = sorted(
                    [ruta for ruta in modulo_dir.glob("*.py") if not ruta.name.startswith("_")],
                    key=_orden_ejercicio
                )
            else:
                modulos = []
            titulo = f"=== EJERCICIOS PYTHON - {modulo_nombre.upper()} ==="
        else:
            modulos = sorted(
                [ruta for ruta in MODULOS_DIR.rglob("*.py") if not ruta.name.startswith("_")],
                key=_orden_ejercicio
            )
            titulo = "=== EJERCICIOS PYTHON ==="

        print(f"\n{titulo}")
        if not modulos:
            print(f"No se encontraron ejercicios en {modulo_nombre if modulo_nombre else 'EjerciciosPython'}.")

        for indice, ruta in enumerate(modulos, start=1):
            nombre_relativo = ruta.relative_to(MODULOS_DIR).with_suffix("")
            print(f"{indice}. {nombre_relativo}")
        print(f"{len(modulos) + 1}. Instalar dependencias (requirements.txt)")
        print(f"{len(modulos) + 2}. Volver")

        opcion = input("Selecciona un módulo: ").strip()

        if not opcion.isdigit():
            print("[ERROR] Opción no válida.")
            continue

        indice = int(opcion)

        if indice == len(modulos) + 2:
            limpiar_pantalla()
            return

        if indice == len(modulos) + 1:
            limpiar_pantalla()
            instalar_dependencias_ejercicios(modulo_nombre)
            continue

        if 1 <= indice <= len(modulos):
            ejecutar_modulo_individual(modulos[indice - 1])
            continue

        print("[ERROR] Opción fuera de rango.")


def ejecutar_modulo_individual(ruta_modulo: Path):
    limpiar_pantalla()
    print(f"=== Ejecutando {ruta_modulo.name} ===")
    try:
        runpy.run_path(str(ruta_modulo), run_name="__main__")
    except Exception as exc:  # breve registro para depuración básica
        print(f"[ERROR] El módulo {ruta_modulo.name} produjo un error: {exc}")
    input("\nPulsa Enter para continuar...")
    limpiar_pantalla()


def instalar_dependencias_ejercicios(modulo_nombre: Optional[str] = None):
    """Instala las dependencias de los ejercicios Python.
    
    Args:
        modulo_nombre: Nombre del módulo específico. Si es None, busca en toda la carpeta.
    """
    if modulo_nombre:
        modulo_dir = MODULOS_DIR / modulo_nombre
        requirements = next(modulo_dir.glob("requirement*.txt"), None)
    else:
        requirements = next(MODULOS_DIR.rglob("requirement*.txt"), None)
    
    if not requirements or not requirements.exists():
        print(f"[ERROR] No se encontró el archivo requirements.txt en {modulo_nombre if modulo_nombre else 'EjerciciosPython'}.")
        input("Pulsa Enter para continuar...")
        return

    comando = [sys.executable, "-m", "pip", "install", "-r", str(requirements)]
    print(f"Instalando dependencias para {modulo_nombre if modulo_nombre else 'EjerciciosPython'}...\n")
    try:
        subprocess.run(comando, check=False)
    except Exception as exc:
        print(f"[ERROR] No se pudieron instalar las dependencias: {exc}")
    input("\nPulsa Enter para continuar...")


def _orden_ejercicio(ruta: Path):
    coincidencia = re.search(r"(\d+)$", ruta.stem)
    if coincidencia:
        return (0, int(coincidencia.group(1)))
    return (1, ruta.stem.lower())

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

def iniciar_aplicacion():
    limpiar_pantalla()
    if "--gui" in sys.argv:
        lanzar_gui()
        return
    if "--cli" in sys.argv:
        menu_principal()
        return

    while True:
        print("\nSelecciona el modo de ejecución:")
        print("1. Módulos IFCT0109 (CLI)")
        print("2. Módulos IFCT0109 (GUI)")
        print("3. EjerciciosPython - Módulo modulo MF0487")
        print("4. EjerciciosPython - Módulo modulo MF0488")
        print("5. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1" or opcion == "":
            menu_principal()
            break
        if opcion == "2":
            lanzar_gui()
            break
        if opcion == "3":
            menu_ejercicios_python("modulo MF0487")
            continue
        if opcion == "4":
            menu_ejercicios_python("modulo MF0488")
            continue
        if opcion == "5":
            print("Saliendo...")
            break
        print("[ERROR] Opción no válida.")


def lanzar_gui():
    try:
        from gui_app import lanzar_gui as _lanzar_gui
    except ImportError as exc:
        print(f"[ERROR] No se pudo cargar la interfaz gráfica: {exc}")
        return
    _lanzar_gui()


if __name__ == "__main__":
    iniciar_aplicacion()
