"""Sistema de registro y clasificación de incidentes de seguridad."""

import json
from datetime import datetime
from typing import Dict, List


def registrar_incidente() -> Dict[str, str]:
    """Solicita los datos de un incidente y devuelve un diccionario con la información."""
    
    print("\n=== REGISTRO DE INCIDENTE ===\n")
    
    incidente = {
        "id": datetime.now().strftime("%Y%m%d%H%M%S"),
        "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tipo": input("Tipo de incidente (ej. Malware, Phishing, Acceso no autorizado, DDoS): "),
        "severidad": input("Severidad (BAJA, MEDIA, ALTA, CRÍTICA): ").upper(),
        "descripcion": input("Descripción del incidente: "),
        "sistema_afectado": input("Sistema/s afectado/s: "),
        "reportado_por": input("Reportado por: "),
        "estado": "ABIERTO"
    }
    
    return incidente


def guardar_incidente(incidente: Dict[str, str], archivo: str = "incidentes.json") -> None:
    """Guarda el incidente en un archivo JSON."""
    
    try:
        # Intentar cargar incidentes existentes
        with open(archivo, "r", encoding="utf-8") as f:
            incidentes = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        incidentes = []
    
    incidentes.append(incidente)
    
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(incidentes, f, indent=4, ensure_ascii=False)
    
    print(f"\n✓ Incidente #{incidente['id']} registrado correctamente.")


def listar_incidentes(archivo: str = "incidentes.json") -> None:
    """Lista todos los incidentes registrados."""
    
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            incidentes = json.load(f)
        
        if not incidentes:
            print("\nNo hay incidentes registrados.")
            return
        
        print("\n=== INCIDENTES REGISTRADOS ===\n")
        for inc in incidentes:
            print(f"ID: {inc['id']}")
            print(f"Fecha: {inc['fecha_hora']}")
            print(f"Tipo: {inc['tipo']}")
            print(f"Severidad: {inc['severidad']}")
            print(f"Estado: {inc['estado']}")
            print(f"Descripción: {inc['descripcion']}")
            print("-" * 50)
    
    except FileNotFoundError:
        print("\nNo hay incidentes registrados.")


if __name__ == "__main__":
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE INCIDENTES ===")
        print("1. Registrar nuevo incidente")
        print("2. Listar incidentes")
        print("3. Salir")
        
        opcion = input("\nSelecciona una opción: ").strip()
        
        if opcion == "1":
            incidente = registrar_incidente()
            guardar_incidente(incidente)
        elif opcion == "2":
            listar_incidentes()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("[ERROR] Opción no válida.")
