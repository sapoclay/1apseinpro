"""Análisis de tráfico de red capturado para detectar anomalías."""

import json
from collections import Counter, defaultdict
from typing import Dict, List, Tuple


def parsear_captura_simplificada(archivo: str) -> List[Dict[str, str]]:
    """Lee un archivo de captura de red en formato texto simplificado.
    
    Formato esperado por línea: timestamp,src_ip,dst_ip,protocol,dst_port,bytes
    Ejemplo: 2025-10-16 10:30:45,192.168.1.100,8.8.8.8,TCP,443,1024
    
    Args:
        archivo: Ruta al archivo de captura.
        
    Returns:
        Lista de diccionarios con los paquetes parseados.
    """
    
    paquetes = []
    
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea or linea.startswith("#"):
                    continue
                
                partes = linea.split(",")
                if len(partes) >= 6:
                    try:
                        paquetes.append({
                            "timestamp": partes[0],
                            "src_ip": partes[1],
                            "dst_ip": partes[2],
                            "protocol": partes[3],
                            "dst_port": partes[4],
                            "bytes": int(partes[5])
                        })
                    except ValueError:
                        continue
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo: {archivo}")
    except Exception as e:
        print(f"[ERROR] Error al parsear el archivo: {e}")
    
    return paquetes


def detectar_escaneo_puertos(paquetes: List[Dict[str, str]]) -> Dict[str, List[str]]:
    """Detecta posibles escaneos de puertos (muchos puertos desde una IP).
    
    Args:
        paquetes: Lista de paquetes de red.
        
    Returns:
        Diccionario con IPs origen sospechosas y los puertos escaneados.
    """
    
    puertos_por_ip = defaultdict(set)
    
    for pkt in paquetes:
        puertos_por_ip[pkt["src_ip"]].add(pkt["dst_port"])
    
    # Considerar sospechoso si se contactan más de 20 puertos diferentes
    sospechosos = {
        ip: list(puertos) 
        for ip, puertos in puertos_por_ip.items() 
        if len(puertos) > 20
    }
    
    return sospechosos


def detectar_volumenes_anomalos(paquetes: List[Dict[str, str]], 
                                umbral_mb: float = 100.0) -> Dict[str, float]:
    """Detecta IPs con volúmenes de tráfico anormalmente altos.
    
    Args:
        paquetes: Lista de paquetes de red.
        umbral_mb: Umbral en MB para considerar anómalo.
        
    Returns:
        Diccionario con IPs y su volumen de tráfico en MB.
    """
    from collections import defaultdict
    
    bytes_por_ip = defaultdict(int)
    
    for pkt in paquetes:
        bytes_por_ip[pkt["src_ip"]] += int(pkt["bytes"])
    
    # Convertir a MB
    mb_por_ip = {ip: bytes_val / (1024 * 1024) for ip, bytes_val in bytes_por_ip.items()}
    
    anomalos = {ip: mb for ip, mb in mb_por_ip.items() if mb > umbral_mb}
    
    return anomalos


def detectar_conexiones_sospechosas(paquetes: List[Dict[str, str]]) -> Dict[str, List[str]]:
    """Detecta conexiones a puertos comúnmente usados por malware.
    
    Args:
        paquetes: Lista de paquetes de red.
        
    Returns:
        Diccionario con IPs que contactaron puertos sospechosos.
    """
    
    # Puertos comunes de malware, C&C, backdoors
    puertos_sospechosos = {
        "4444": "Metasploit default",
        "5555": "Backdoor común",
        "6666": "IRC/Botnet",
        "6667": "IRC",
        "8080": "Proxy/C&C alternativo",
        "31337": "BackOrifice",
        "12345": "NetBus"
    }
    
    conexiones = defaultdict(list)
    
    for pkt in paquetes:
        puerto = pkt["dst_port"]
        if puerto in puertos_sospechosos:
            conexiones[pkt["src_ip"]].append(
                f"{pkt['dst_ip']}:{puerto} ({puertos_sospechosos[puerto]})"
            )
    
    return dict(conexiones)


def analizar_protocolos(paquetes: List[Dict[str, str]]) -> Dict[str, int]:
    """Analiza la distribución de protocolos en el tráfico.
    
    Args:
        paquetes: Lista de paquetes de red.
        
    Returns:
        Diccionario con el conteo de cada protocolo.
    """
    
    protocolos = Counter(pkt["protocol"] for pkt in paquetes)
    return dict(protocolos)


def analizar_trafico(archivo: str) -> None:
    """Realiza un análisis completo del tráfico de red capturado.
    
    Args:
        archivo: Ruta al archivo de captura.
    """
    
    print(f"\n=== ANALIZANDO TRÁFICO DE RED: {archivo} ===\n")
    
    paquetes = parsear_captura_simplificada(archivo)
    
    if not paquetes:
        print("[ERROR] No se pudieron leer paquetes del archivo.")
        return
    
    print(f"Total de paquetes analizados: {len(paquetes)}")
    print("-" * 70)
    
    # Análisis de protocolos
    print("\n📊 DISTRIBUCIÓN DE PROTOCOLOS:")
    protocolos = analizar_protocolos(paquetes)
    for protocolo, count in sorted(protocolos.items(), key=lambda x: x[1], reverse=True):
        print(f"  {protocolo}: {count} paquetes")
    
    # Detección de escaneos
    print("\n🔍 DETECCIÓN DE ESCANEOS DE PUERTOS:")
    escaneos = detectar_escaneo_puertos(paquetes)
    if escaneos:
        for ip, puertos in escaneos.items():
            print(f"  ⚠️  {ip}: {len(puertos)} puertos diferentes contactados")
            print(f"      Puertos: {', '.join(sorted(puertos)[:10])}...")
    else:
        print("  ✓ No se detectaron escaneos de puertos.")
    
    # Detección de volúmenes anómalos
    print("\n📈 DETECCIÓN DE VOLÚMENES ANÓMALOS:")
    anomalos = detectar_volumenes_anomalos(paquetes, umbral_mb=50.0)
    if anomalos:
        for ip, mb in sorted(anomalos.items(), key=lambda x: x[1], reverse=True):
            print(f"  ⚠️  {ip}: {mb:.2f} MB transferidos")
    else:
        print("  ✓ No se detectaron volúmenes anómalos.")
    
    # Detección de conexiones sospechosas
    print("\n🚨 CONEXIONES A PUERTOS SOSPECHOSOS:")
    sospechosas = detectar_conexiones_sospechosas(paquetes)
    if sospechosas:
        for ip, conexiones in sospechosas.items():
            print(f"  🔴 {ip}:")
            for conn in conexiones:
                print(f"      → {conn}")
    else:
        print("  ✓ No se detectaron conexiones sospechosas.")
    
    # Top IPs más activas
    print("\n📊 TOP 10 IPs MÁS ACTIVAS:")
    contador_ips = Counter(pkt["src_ip"] for pkt in paquetes)
    for ip, count in contador_ips.most_common(10):
        print(f"  {ip}: {count} paquetes")


def generar_archivo_ejemplo() -> None:
    """Genera un archivo de ejemplo para pruebas."""
    
    contenido = """# Archivo de captura de tráfico de red - Formato simplificado
# timestamp,src_ip,dst_ip,protocol,dst_port,bytes
2025-10-16 10:30:45,192.168.1.100,8.8.8.8,TCP,443,1024
2025-10-16 10:30:46,192.168.1.100,8.8.8.8,TCP,443,2048
2025-10-16 10:30:47,192.168.1.101,192.168.1.1,UDP,53,512
2025-10-16 10:30:48,192.168.1.100,93.184.216.34,TCP,80,4096
2025-10-16 10:30:49,10.0.0.50,192.168.1.100,TCP,22,256
2025-10-16 10:30:50,10.0.0.50,192.168.1.100,TCP,23,256
2025-10-16 10:30:51,10.0.0.50,192.168.1.100,TCP,80,256
2025-10-16 10:30:52,10.0.0.50,192.168.1.100,TCP,443,256
2025-10-16 10:30:53,10.0.0.50,192.168.1.100,TCP,8080,256
2025-10-16 10:30:54,10.0.0.50,192.168.1.100,TCP,21,256
2025-10-16 10:30:55,10.0.0.50,192.168.1.100,TCP,445,256
2025-10-16 10:30:56,192.168.1.100,8.8.8.8,TCP,443,1024000
"""
    
    with open("captura_ejemplo.txt", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("\n✓ Archivo de ejemplo generado: captura_ejemplo.txt")


if __name__ == "__main__":
    print("=== ANALIZADOR DE TRÁFICO DE RED ===\n")
    print("1. Analizar archivo de captura")
    print("2. Generar archivo de ejemplo")
    print("3. Salir")
    
    opcion = input("\nSelecciona una opción: ").strip()
    
    if opcion == "1":
        archivo = input("\nIntroduce la ruta del archivo de captura: ").strip()
        if archivo:
            analizar_trafico(archivo)
        else:
            print("[ERROR] No se especificó ningún archivo.")
    
    elif opcion == "2":
        generar_archivo_ejemplo()
    
    elif opcion == "3":
        print("Saliendo...")
    
    else:
        print("[ERROR] Opción no válida.")
