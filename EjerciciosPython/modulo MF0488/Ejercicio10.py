"""Dashboard interactivo para visualizar estadísticas de incidentes."""

import json
from collections import Counter
from datetime import datetime
from typing import Dict, List


def cargar_incidentes(archivo: str = "incidentes.json") -> List[Dict[str, str]]:
    """Carga los incidentes desde el archivo JSON.
    
    Args:
        archivo: Ruta al archivo de incidentes.
        
    Returns:
        Lista de incidentes.
    """
    
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo {archivo}")
        return []
    except json.JSONDecodeError:
        print(f"[ERROR] El archivo {archivo} no es un JSON válido")
        return []


def calcular_estadisticas(incidentes: List[Dict[str, str]]) -> Dict:
    """Calcula estadísticas agregadas de los incidentes.
    
    Args:
        incidentes: Lista de incidentes.
        
    Returns:
        Diccionario con las estadísticas calculadas.
    """
    
    if not incidentes:
        return {}
    
    total = len(incidentes)
    
    # Por severidad
    por_severidad = Counter(inc.get("severidad", "DESCONOCIDA") for inc in incidentes)
    
    # Por tipo
    por_tipo = Counter(inc.get("tipo", "Desconocido") for inc in incidentes)
    
    # Por estado
    por_estado = Counter(inc.get("estado", "DESCONOCIDO") for inc in incidentes)
    
    # Calcular porcentajes de severidad
    porcentajes_severidad = {
        sev: (count / total * 100) for sev, count in por_severidad.items()
    }
    
    return {
        "total": total,
        "por_severidad": dict(por_severidad),
        "porcentajes_severidad": porcentajes_severidad,
        "por_tipo": dict(por_tipo),
        "por_estado": dict(por_estado)
    }


def mostrar_barra(porcentaje: float, longitud: int = 30, caracter: str = "█") -> str:
    """Genera una barra de progreso visual.
    
    Args:
        porcentaje: Porcentaje a representar (0-100).
        longitud: Longitud de la barra en caracteres.
        caracter: Carácter para dibujar la barra.
        
    Returns:
        String con la barra visual.
    """
    
    relleno = int((porcentaje / 100) * longitud)
    vacio = longitud - relleno
    return f"[{caracter * relleno}{' ' * vacio}]"


def mostrar_dashboard(incidentes: List[Dict[str, str]]) -> None:
    """Muestra un dashboard interactivo con las estadísticas.
    
    Args:
        incidentes: Lista de incidentes a visualizar.
    """
    
    if not incidentes:
        print("\n[INFO] No hay incidentes para mostrar.")
        return
    
    stats = calcular_estadisticas(incidentes)
    
    # Header
    print("\n" + "=" * 80)
    print(" " * 20 + "📊 DASHBOARD DE INCIDENTES DE SEGURIDAD")
    print("=" * 80)
    print(f"\nÚltima actualización: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 80)
    
    # Total de incidentes
    print(f"\n{'TOTAL DE INCIDENTES':^80}")
    print(f"{'=' * 80}")
    print(f"\n{stats['total']:^80}")
    print()
    
    # Por severidad
    print(f"\n{'INCIDENTES POR SEVERIDAD':^80}")
    print("=" * 80)
    
    orden_severidad = ["CRÍTICA", "ALTA", "MEDIA", "BAJA", "DESCONOCIDA"]
    colores = {
        "CRÍTICA": "🔴",
        "ALTA": "🟠",
        "MEDIA": "🟡",
        "BAJA": "🟢",
        "DESCONOCIDA": "⚪"
    }
    
    for sev in orden_severidad:
        if sev in stats["por_severidad"]:
            count = stats["por_severidad"][sev]
            porcentaje = stats["porcentajes_severidad"][sev]
            emoji = colores.get(sev, "⚪")
            barra = mostrar_barra(porcentaje)
            print(f"\n{emoji} {sev:12} {barra} {count:3} ({porcentaje:5.1f}%)")
    
    # Por estado
    print(f"\n\n{'INCIDENTES POR ESTADO':^80}")
    print("=" * 80)
    
    for estado, count in sorted(stats["por_estado"].items()):
        porcentaje = (count / stats["total"]) * 100
        emoji = "🟢" if estado == "CERRADO" else "🔴" if estado == "ABIERTO" else "🟡"
        barra = mostrar_barra(porcentaje)
        print(f"\n{emoji} {estado:12} {barra} {count:3} ({porcentaje:5.1f}%)")
    
    # Por tipo
    print(f"\n\n{'TOP 5 TIPOS DE INCIDENTES':^80}")
    print("=" * 80)
    
    top_tipos = sorted(stats["por_tipo"].items(), key=lambda x: x[1], reverse=True)[:5]
    
    for i, (tipo, count) in enumerate(top_tipos, 1):
        porcentaje = (count / stats["total"]) * 100
        barra = mostrar_barra(porcentaje)
        print(f"\n{i}. {tipo:30} {barra} {count:3} ({porcentaje:5.1f}%)")
    
    # Incidentes recientes
    print(f"\n\n{'ÚLTIMOS 5 INCIDENTES':^80}")
    print("=" * 80)
    
    ultimos = sorted(incidentes, key=lambda x: x.get("id", ""), reverse=True)[:5]
    
    for inc in ultimos:
        sev = inc.get("severidad", "N/A")
        emoji = colores.get(sev, "⚪")
        print(f"\n{emoji} ID: {inc.get('id', 'N/A'):15} | {inc.get('tipo', 'N/A'):25} | {sev:8}")
        print(f"   {inc.get('descripcion', 'Sin descripción')[:70]}")
    
    print("\n" + "=" * 80 + "\n")


def menu_dashboard() -> None:
    """Menú interactivo del dashboard."""
    
    while True:
        print("\n" + "=" * 80)
        print(" " * 25 + "DASHBOARD DE INCIDENTES")
        print("=" * 80)
        print("\n1. Ver dashboard completo")
        print("2. Filtrar por severidad")
        print("3. Filtrar por estado")
        print("4. Buscar por tipo")
        print("5. Actualizar datos")
        print("6. Salir")
        
        opcion = input("\nSelecciona una opción: ").strip()
        
        if opcion == "1":
            incidentes = cargar_incidentes()
            mostrar_dashboard(incidentes)
            input("\nPresiona Enter para continuar...")
        
        elif opcion == "2":
            incidentes = cargar_incidentes()
            if incidentes:
                severidad = input("\nSeveridad (CRÍTICA/ALTA/MEDIA/BAJA): ").upper()
                filtrados = [inc for inc in incidentes if inc.get("severidad") == severidad]
                print(f"\n{len(filtrados)} incidentes con severidad {severidad}")
                mostrar_dashboard(filtrados)
                input("\nPresiona Enter para continuar...")
        
        elif opcion == "3":
            incidentes = cargar_incidentes()
            if incidentes:
                estado = input("\nEstado (ABIERTO/CERRADO/EN_PROGRESO): ").upper()
                filtrados = [inc for inc in incidentes if inc.get("estado") == estado]
                print(f"\n{len(filtrados)} incidentes en estado {estado}")
                mostrar_dashboard(filtrados)
                input("\nPresiona Enter para continuar...")
        
        elif opcion == "4":
            incidentes = cargar_incidentes()
            if incidentes:
                tipo = input("\nTipo de incidente: ").strip()
                filtrados = [inc for inc in incidentes if tipo.lower() in inc.get("tipo", "").lower()]
                print(f"\n{len(filtrados)} incidentes del tipo '{tipo}'")
                mostrar_dashboard(filtrados)
                input("\nPresiona Enter para continuar...")
        
        elif opcion == "5":
            print("\n✓ Datos actualizados.")
            incidentes = cargar_incidentes()
            print(f"Total de incidentes cargados: {len(incidentes)}")
            input("\nPresiona Enter para continuar...")
        
        elif opcion == "6":
            print("\nSaliendo del dashboard...")
            break
        
        else:
            print("[ERROR] Opción no válida.")


if __name__ == "__main__":
    menu_dashboard()
