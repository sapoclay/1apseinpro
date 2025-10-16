"""Analizador de logs de acceso para detectar patrones de ataque (fuerza bruta, escaneos)."""

import re
from collections import Counter, defaultdict
from datetime import datetime
from typing import Dict, List, Tuple


def parsear_log_apache(linea: str) -> Dict[str, str]:
    """Extrae información relevante de una línea de log Apache/Nginx.
    
    Args:
        linea: Línea del archivo de log.
        
    Returns:
        Diccionario con IP, fecha, método, ruta y código de estado.
    """
    
    # Patrón para logs Apache/Nginx: IP - - [fecha] "MÉTODO /ruta HTTP/1.1" código tamaño
    patron = r'(\S+) - - \[(.*?)\] "(\S+) (\S+) \S+" (\d+)'
    match = re.match(patron, linea)
    
    if match:
        return {
            "ip": match.group(1),
            "fecha": match.group(2),
            "metodo": match.group(3),
            "ruta": match.group(4),
            "codigo": match.group(5)
        }
    return {}


def detectar_fuerza_bruta(logs: List[Dict[str, str]], umbral: int = 10) -> Dict[str, int]:
    """Detecta intentos de fuerza bruta basándose en códigos 401/403.
    
    Args:
        logs: Lista de entradas de log parseadas.
        umbral: Número de fallos para considerar ataque.
        
    Returns:
        Diccionario con IPs sospechosas y su número de intentos fallidos.
    """
    
    fallos_por_ip = defaultdict(int)
    
    for log in logs:
        if log.get("codigo") in ["401", "403"]:
            fallos_por_ip[log["ip"]] += 1
    
    return {ip: count for ip, count in fallos_por_ip.items() if count >= umbral}


def detectar_escaneos(logs: List[Dict[str, str]], umbral: int = 20) -> Dict[str, int]:
    """Detecta posibles escaneos de vulnerabilidades (muchas rutas diferentes por IP).
    
    Args:
        logs: Lista de entradas de log parseadas.
        umbral: Número de rutas únicas para considerar escaneo.
        
    Returns:
        Diccionario con IPs sospechosas y rutas únicas accedidas.
    """
    
    rutas_por_ip = defaultdict(set)
    
    for log in logs:
        if log.get("ip") and log.get("ruta"):
            rutas_por_ip[log["ip"]].add(log["ruta"])
    
    return {ip: len(rutas) for ip, rutas in rutas_por_ip.items() if len(rutas) >= umbral}


def detectar_ataques_comunes(logs: List[Dict[str, str]]) -> Dict[str, List[str]]:
    """Detecta patrones de ataques comunes en las rutas solicitadas.
    
    Args:
        logs: Lista de entradas de log parseadas.
        
    Returns:
        Diccionario agrupando IPs por tipo de ataque detectado.
    """
    
    patrones_ataque = {
        "SQL Injection": [r"union.*select", r"'.*or.*'", r"exec\(", r"--"],
        "XSS": [r"<script", r"javascript:", r"onerror="],
        "Path Traversal": [r"\.\./", r"\.\.\\"],
        "Command Injection": [r";.*ls", r"\|.*cat", r"`.*whoami"]
    }
    
    ataques_detectados = defaultdict(list)
    
    for log in logs:
        ruta = log.get("ruta", "").lower()
        ip = log.get("ip")
        
        if not ruta or not ip:
            continue
        
        for tipo_ataque, patrones in patrones_ataque.items():
            for patron in patrones:
                if re.search(patron, ruta, re.IGNORECASE):
                    if ip not in ataques_detectados[tipo_ataque]:
                        ataques_detectados[tipo_ataque].append(ip)
                    break
    
    return dict(ataques_detectados)


def analizar_logs(archivo_log: str) -> None:
    """Analiza un archivo de logs y genera un reporte de seguridad.
    
    Args:
        archivo_log: Ruta al archivo de logs a analizar.
    """
    
    print(f"\n=== ANALIZANDO: {archivo_log} ===\n")
    
    logs = []
    
    try:
        with open(archivo_log, "r", encoding="utf-8", errors="ignore") as f:
            for linea in f:
                entrada = parsear_log_apache(linea.strip())
                if entrada:
                    logs.append(entrada)
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo: {archivo_log}")
        return
    
    if not logs:
        print("[ERROR] No se pudieron parsear entradas del log.")
        return
    
    print(f"Total de entradas parseadas: {len(logs)}")
    print("-" * 60)
    
    # Detectar fuerza bruta
    print("\n🔐 DETECCIÓN DE FUERZA BRUTA:")
    fuerza_bruta = detectar_fuerza_bruta(logs)
    if fuerza_bruta:
        for ip, intentos in sorted(fuerza_bruta.items(), key=lambda x: x[1], reverse=True):
            print(f"  ⚠️  {ip}: {intentos} intentos fallidos")
    else:
        print("  ✓ No se detectaron patrones de fuerza bruta.")
    
    # Detectar escaneos
    print("\n🔍 DETECCIÓN DE ESCANEOS:")
    escaneos = detectar_escaneos(logs)
    if escaneos:
        for ip, rutas in sorted(escaneos.items(), key=lambda x: x[1], reverse=True):
            print(f"  ⚠️  {ip}: {rutas} rutas únicas accedidas")
    else:
        print("  ✓ No se detectaron patrones de escaneo.")
    
    # Detectar ataques comunes
    print("\n🚨 DETECCIÓN DE ATAQUES ESPECÍFICOS:")
    ataques = detectar_ataques_comunes(logs)
    if ataques:
        for tipo, ips in ataques.items():
            print(f"  🔴 {tipo}:")
            for ip in ips:
                print(f"      - {ip}")
    else:
        print("  ✓ No se detectaron patrones de ataque conocidos.")
    
    # Top IPs
    print("\n📊 TOP 10 IPs MÁS ACTIVAS:")
    contador_ips = Counter(log["ip"] for log in logs)
    for ip, count in contador_ips.most_common(10):
        print(f"  {ip}: {count} solicitudes")


if __name__ == "__main__":
    print("=== ANALIZADOR DE LOGS DE SEGURIDAD ===\n")
    
    archivo = input("Introduce la ruta del archivo de log (ej. access.log): ").strip()
    
    if archivo:
        analizar_logs(archivo)
    else:
        print("[ERROR] No se especificó ningún archivo.")
