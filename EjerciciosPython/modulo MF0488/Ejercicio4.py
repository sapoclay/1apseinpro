"""Monitor de cambios en archivos críticos del sistema para detectar modificaciones sospechosas."""

import hashlib
import json
import time
from pathlib import Path
from typing import Dict, List, Optional


def calcular_hash(archivo: Path) -> Optional[str]:
    """Calcula el hash SHA256 de un archivo."""
    
    try:
        sha256 = hashlib.sha256()
        with open(archivo, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                sha256.update(bloque)
        return sha256.hexdigest()
    except Exception:
        return None


def crear_baseline(archivos: List[str], baseline_file: str = "baseline.json") -> None:
    """Crea una línea base con los hashes de los archivos críticos.
    
    Args:
        archivos: Lista de rutas de archivos a monitorizar.
        baseline_file: Archivo donde guardar la línea base.
    """
    
    baseline = {}
    
    print("\n=== CREANDO LÍNEA BASE ===\n")
    
    for ruta in archivos:
        archivo = Path(ruta)
        if archivo.exists() and archivo.is_file():
            hash_actual = calcular_hash(archivo)
            if hash_actual:
                baseline[str(archivo)] = {
                    "hash": hash_actual,
                    "fecha": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                print(f"✓ {archivo.name}")
        else:
            print(f"⚠ {ruta} - No encontrado")
    
    with open(baseline_file, "w", encoding="utf-8") as f:
        json.dump(baseline, f, indent=4, ensure_ascii=False)
    
    print(f"\n✓ Línea base guardada en {baseline_file}")


def verificar_integridad(baseline_file: str = "baseline.json") -> None:
    """Verifica la integridad de los archivos comparándolos con la línea base.
    
    Args:
        baseline_file: Archivo con la línea base de referencia.
    """
    
    try:
        with open(baseline_file, "r", encoding="utf-8") as f:
            baseline = json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo de línea base: {baseline_file}")
        return
    
    print("\n=== VERIFICACIÓN DE INTEGRIDAD ===\n")
    
    cambios_detectados = False
    
    for ruta, info in baseline.items():
        archivo = Path(ruta)
        
        if not archivo.exists():
            print(f"⚠️  ARCHIVO ELIMINADO: {archivo.name}")
            cambios_detectados = True
            continue
        
        hash_actual = calcular_hash(archivo)
        
        if hash_actual and hash_actual != info["hash"]:
            print(f"🔴 MODIFICADO: {archivo.name}")
            print(f"   Hash original: {info['hash'][:16]}...")
            print(f"   Hash actual:   {hash_actual[:16]}...")
            cambios_detectados = True
        elif hash_actual:
            print(f"✓ {archivo.name} - Sin cambios")
        else:
            print(f"⚠️  ERROR al leer: {archivo.name}")
            cambios_detectados = True
    
    if not cambios_detectados:
        print("\n✓ Todos los archivos mantienen su integridad.")
    else:
        print("\n⚠️  Se detectaron cambios en archivos críticos.")


if __name__ == "__main__":
    print("=== MONITOR DE INTEGRIDAD DE ARCHIVOS ===")
    print("\n1. Crear línea base")
    print("2. Verificar integridad")
    print("3. Salir")
    
    opcion = input("\nSelecciona una opción: ").strip()
    
    if opcion == "1":
        print("\nIntroduce las rutas de los archivos a monitorizar (una por línea).")
        print("Deja una línea vacía para finalizar.")
        print("Ejemplo: /etc/passwd, ~/.bashrc, config.ini")
        
        archivos = []
        while True:
            ruta = input().strip()
            if not ruta:
                break
            archivos.append(ruta)
        
        if archivos:
            crear_baseline(archivos)
        else:
            print("[ERROR] No se especificaron archivos.")
    
    elif opcion == "2":
        verificar_integridad()
    
    elif opcion == "3":
        print("Saliendo...")
    
    else:
        print("[ERROR] Opción no válida.")
