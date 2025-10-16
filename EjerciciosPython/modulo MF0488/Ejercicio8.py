"""Simulador de respuesta a incidentes siguiendo el framework NIST."""

import json
from datetime import datetime
from typing import Dict, List


class IncidentResponse:
    """Gestor de respuesta a incidentes siguiendo las fases del NIST."""
    
    FASES = [
        "1. Preparación",
        "2. Detección y Análisis",
        "3. Contención, Erradicación y Recuperación",
        "4. Post-Incidente"
    ]
    
    def __init__(self):
        """Inicializa el gestor de respuesta a incidentes."""
        self.incidente = {}
        self.acciones = []
    
    def fase_preparacion(self) -> None:
        """Fase 1: Preparación - Establecer capacidades de respuesta."""
        print("\n" + "=" * 70)
        print("FASE 1: PREPARACIÓN")
        print("=" * 70)
        print("\nVerificando preparación del equipo de respuesta...\n")
        
        checklist = [
            "✓ Equipo de respuesta identificado y contactado",
            "✓ Herramientas de análisis forense disponibles",
            "✓ Procedimientos de escalado definidos",
            "✓ Sistemas de respaldo verificados",
            "✓ Canales de comunicación establecidos"
        ]
        
        for item in checklist:
            print(f"  {item}")
        
        self.acciones.append({
            "fase": "Preparación",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "accion": "Verificación de preparación completada"
        })
    
    def fase_deteccion_analisis(self) -> None:
        """Fase 2: Detección y Análisis - Identificar y evaluar el incidente."""
        print("\n" + "=" * 70)
        print("FASE 2: DETECCIÓN Y ANÁLISIS")
        print("=" * 70)
        
        print("\n--- Información del Incidente ---")
        self.incidente["id"] = datetime.now().strftime("%Y%m%d%H%M%S")
        self.incidente["tipo"] = input("Tipo de incidente: ")
        self.incidente["severidad"] = input("Severidad (BAJA/MEDIA/ALTA/CRÍTICA): ").upper()
        self.incidente["descripcion"] = input("Descripción breve: ")
        self.incidente["sistemas_afectados"] = input("Sistemas afectados: ")
        
        print("\n--- Análisis Inicial ---")
        print("¿Indicadores de compromiso detectados?")
        ioc = input("IPs sospechosas, hashes, dominios (separados por comas): ")
        self.incidente["ioc"] = [x.strip() for x in ioc.split(",")] if ioc else []
        
        alcance = input("¿Cuántos sistemas están afectados? ")
        self.incidente["alcance"] = alcance
        
        vectores = input("Vector de ataque identificado: ")
        self.incidente["vector"] = vectores
        
        self.acciones.append({
            "fase": "Detección y Análisis",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "accion": f"Incidente #{self.incidente['id']} analizado y clasificado"
        })
    
    def fase_contencion_erradicacion(self) -> None:
        """Fase 3: Contención, Erradicación y Recuperación."""
        print("\n" + "=" * 70)
        print("FASE 3: CONTENCIÓN, ERRADICACIÓN Y RECUPERACIÓN")
        print("=" * 70)
        
        print("\n--- 3.1 CONTENCIÓN ---")
        print("Acciones de contención inmediata:")
        print("  1. Aislar sistemas afectados")
        print("  2. Bloquear IPs/dominios maliciosos")
        print("  3. Deshabilitar cuentas comprometidas")
        print("  4. Cambiar contraseñas críticas")
        
        contencion = input("\n¿Qué acciones de contención se tomaron? ")
        self.incidente["contencion"] = contencion
        
        self.acciones.append({
            "fase": "Contención",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "accion": contencion
        })
        
        print("\n--- 3.2 ERRADICACIÓN ---")
        print("Eliminación de la amenaza:")
        print("  1. Eliminar malware/backdoors")
        print("  2. Cerrar vulnerabilidades explotadas")
        print("  3. Aplicar parches de seguridad")
        
        erradicacion = input("\n¿Cómo se erradicó la amenaza? ")
        self.incidente["erradicacion"] = erradicacion
        
        self.acciones.append({
            "fase": "Erradicación",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "accion": erradicacion
        })
        
        print("\n--- 3.3 RECUPERACIÓN ---")
        print("Restauración de operaciones normales:")
        print("  1. Restaurar desde respaldos limpios")
        print("  2. Verificar integridad de sistemas")
        print("  3. Monitoreo reforzado")
        
        recuperacion = input("\n¿Cómo se recuperaron los sistemas? ")
        self.incidente["recuperacion"] = recuperacion
        
        self.acciones.append({
            "fase": "Recuperación",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "accion": recuperacion
        })
    
    def fase_post_incidente(self) -> None:
        """Fase 4: Actividades Post-Incidente - Lecciones aprendidas."""
        print("\n" + "=" * 70)
        print("FASE 4: POST-INCIDENTE")
        print("=" * 70)
        
        print("\n--- Análisis de Lecciones Aprendidas ---")
        
        causa_raiz = input("\n¿Cuál fue la causa raíz del incidente? ")
        self.incidente["causa_raiz"] = causa_raiz
        
        prevencion = input("¿Cómo se puede prevenir en el futuro? ")
        self.incidente["prevencion"] = prevencion
        
        mejoras = input("¿Qué mejoras se implementarán? ")
        self.incidente["mejoras"] = mejoras
        
        tiempo_resolucion = input("Tiempo total de resolución (ej. 2 horas): ")
        self.incidente["tiempo_resolucion"] = tiempo_resolucion
        
        self.acciones.append({
            "fase": "Post-Incidente",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "accion": "Análisis post-incidente completado"
        })
    
    def generar_informe(self) -> None:
        """Genera un informe completo de la respuesta al incidente."""
        print("\n" + "=" * 70)
        print("INFORME DE RESPUESTA A INCIDENTE")
        print("=" * 70)
        
        self.incidente["fecha_cierre"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.incidente["acciones_realizadas"] = self.acciones
        
        nombre_archivo = f"informe_incidente_{self.incidente['id']}.json"
        
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(self.incidente, f, indent=4, ensure_ascii=False)
        
        print(f"\n✓ Informe guardado en: {nombre_archivo}")
        
        # Mostrar resumen
        print("\n--- RESUMEN ---")
        print(f"ID: {self.incidente.get('id')}")
        print(f"Tipo: {self.incidente.get('tipo')}")
        print(f"Severidad: {self.incidente.get('severidad')}")
        print(f"Tiempo de resolución: {self.incidente.get('tiempo_resolucion')}")
        print(f"Total de acciones registradas: {len(self.acciones)}")
    
    def ejecutar_respuesta(self) -> None:
        """Ejecuta el proceso completo de respuesta a incidentes."""
        print("\n" + "=" * 70)
        print("SIMULADOR DE RESPUESTA A INCIDENTES - FRAMEWORK NIST")
        print("=" * 70)
        
        for fase in self.FASES:
            print(f"\n{fase}")
        
        input("\nPresiona Enter para comenzar el proceso...")
        
        self.fase_preparacion()
        input("\nPresiona Enter para continuar a la siguiente fase...")
        
        self.fase_deteccion_analisis()
        input("\nPresiona Enter para continuar a la siguiente fase...")
        
        self.fase_contencion_erradicacion()
        input("\nPresiona Enter para continuar a la siguiente fase...")
        
        self.fase_post_incidente()
        
        self.generar_informe()


if __name__ == "__main__":
    gestor = IncidentResponse()
    gestor.ejecutar_respuesta()
