"""Analizador de hashes de archivos para detección de malware conocido."""

import hashlib
from pathlib import Path
from typing import Any, Dict, Optional


# Base de datos simple de hashes maliciosos conocidos (ejemplos educativos)
HASHES_MALICIOSOS = {
    "44d88612fea8a8f36de82e1278abb02f": "EICAR Test File (no malicioso, solo prueba)",
    "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f": "Ejemplo de malware",
}


def calcular_hash_md5(ruta_archivo: Path) -> Optional[str]:
    """Calcula el hash MD5 de un archivo.
    
    Args:
        ruta_archivo: Ruta al archivo a analizar.
        
    Returns:
        Hash MD5 en formato hexadecimal, o None si hay error.
    """
    
    try:
        md5_hash = hashlib.md5()
        with open(ruta_archivo, "rb") as f:
            # Leer el archivo en bloques para archivos grandes
            for bloque in iter(lambda: f.read(4096), b""):
                md5_hash.update(bloque)
        return md5_hash.hexdigest()
    except Exception as e:
        print(f"[ERROR] No se pudo calcular el hash: {e}")
        return None


def calcular_hash_sha256(ruta_archivo: Path) -> Optional[str]:
    """Calcula el hash SHA256 de un archivo.
    
    Args:
        ruta_archivo: Ruta al archivo a analizar.
        
    Returns:
        Hash SHA256 en formato hexadecimal, o None si hay error.
    """
    
    try:
        sha256_hash = hashlib.sha256()
        with open(ruta_archivo, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                sha256_hash.update(bloque)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"[ERROR] No se pudo calcular el hash: {e}")
        return None


def verificar_malware(hash_md5: str, hash_sha256: str) -> Dict[str, Any]:
    """Verifica si los hashes corresponden a malware conocido.
    
    Args:
        hash_md5: Hash MD5 del archivo.
        hash_sha256: Hash SHA256 del archivo.
        
    Returns:
        Diccionario con el resultado de la verificación.
    """
    
    resultado = {
        "es_malicioso": False,
        "descripcion": "Archivo no identificado en la base de datos",
        "hash_encontrado": None
    }
    
    if hash_md5 in HASHES_MALICIOSOS:
        resultado["es_malicioso"] = True
        resultado["descripcion"] = HASHES_MALICIOSOS[hash_md5]
        resultado["hash_encontrado"] = f"MD5: {hash_md5}"
    elif hash_sha256 in HASHES_MALICIOSOS:
        resultado["es_malicioso"] = True
        resultado["descripcion"] = HASHES_MALICIOSOS[hash_sha256]
        resultado["hash_encontrado"] = f"SHA256: {hash_sha256}"
    
    return resultado


if __name__ == "__main__":
    print("=== ANALIZADOR DE ARCHIVOS - DETECTOR DE MALWARE ===\n")
    
    ruta_input = input("Introduce la ruta del archivo a analizar: ").strip()
    ruta_archivo = Path(ruta_input)
    
    if not ruta_archivo.exists():
        print(f"[ERROR] El archivo '{ruta_archivo}' no existe.")
    elif not ruta_archivo.is_file():
        print(f"[ERROR] '{ruta_archivo}' no es un archivo válido.")
    else:
        print(f"\nAnalizando: {ruta_archivo.name}")
        print("-" * 50)
        
        # Calcular hashes
        hash_md5 = calcular_hash_md5(ruta_archivo)
        hash_sha256 = calcular_hash_sha256(ruta_archivo)
        
        if hash_md5 and hash_sha256:
            print(f"MD5:    {hash_md5}")
            print(f"SHA256: {hash_sha256}")
            
            # Verificar si es malware conocido
            resultado = verificar_malware(hash_md5, hash_sha256)
            
            print("\n--- RESULTADO DEL ANÁLISIS ---")
            if resultado["es_malicioso"]:
                print("⚠️  ¡ARCHIVO MALICIOSO DETECTADO!")
                print(f"Descripción: {resultado['descripcion']}")
                print(f"Hash: {resultado['hash_encontrado']}")
            else:
                print("✓ No se detectaron amenazas conocidas.")
                print(f"Nota: {resultado['descripcion']}")
