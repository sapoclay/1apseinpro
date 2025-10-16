"""Sistema de notificaciones de incidentes por email (simulado)."""

import json
from datetime import datetime
from typing import Dict, List, Optional


def generar_email_notificacion(incidente: Dict[str, str]) -> str:
    """Genera el contenido de un email de notificación de incidente.
    
    Args:
        incidente: Diccionario con la información del incidente.
        
    Returns:
        Contenido del email en formato texto.
    """
    
    # Mapeo de severidad a prioridad y emoji
    prioridades = {
        "CRÍTICA": ("🚨 URGENTE", "INMEDIATA"),
        "ALTA": ("⚠️  ALTA", "24 horas"),
        "MEDIA": ("⚡ MEDIA", "48 horas"),
        "BAJA": ("ℹ️  BAJA", "1 semana")
    }
    
    severidad = incidente.get("severidad", "MEDIA").upper()
    emoji, tiempo_respuesta = prioridades.get(severidad, ("ℹ️", "Según procedimiento"))
    
    email = f"""
{'=' * 70}
{emoji} ALERTA DE INCIDENTE DE SEGURIDAD
{'=' * 70}

INFORMACIÓN DEL INCIDENTE:
--------------------------
ID del Incidente:    {incidente.get('id', 'N/A')}
Fecha y Hora:        {incidente.get('fecha_hora', 'N/A')}
Severidad:           {severidad}
Tipo:                {incidente.get('tipo', 'N/A')}
Estado:              {incidente.get('estado', 'ABIERTO')}

DETALLES:
---------
Sistema Afectado:    {incidente.get('sistema_afectado', 'N/A')}
Descripción:         {incidente.get('descripcion', 'N/A')}
Reportado por:       {incidente.get('reportado_por', 'N/A')}

ACCIÓN REQUERIDA:
-----------------
Tiempo de respuesta esperado: {tiempo_respuesta}

PRÓXIMOS PASOS:
---------------
1. Evaluar el alcance del incidente
2. Contener la amenaza si es necesario
3. Recopilar evidencias
4. Documentar las acciones tomadas
5. Actualizar el estado del incidente

Para más información, acceda al sistema de gestión de incidentes.

{'=' * 70}
Este es un mensaje automático del Sistema de Gestión de Incidentes.
Generado: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
{'=' * 70}
"""
    
    return email


def enviar_notificacion(incidente: Dict[str, str], 
                       destinatarios: List[str],
                       simular: bool = True) -> None:
    """Envía (o simula) una notificación por email.
    
    Args:
        incidente: Diccionario con la información del incidente.
        destinatarios: Lista de direcciones de email.
        simular: Si True, solo muestra el email sin enviarlo.
    """
    
    contenido = generar_email_notificacion(incidente)
    
    if simular:
        print("\n" + "=" * 70)
        print("MODO SIMULACIÓN - EMAIL NO ENVIADO REALMENTE")
        print("=" * 70)
        print(f"\nDe:      sistema-incidentes@empresa.com")
        print(f"Para:    {', '.join(destinatarios)}")
        print(f"Asunto:  [INCIDENTE #{incidente.get('id')}] {incidente.get('tipo')} - {incidente.get('severidad')}")
        print("\n" + contenido)
    else:
        # Aquí iría la lógica real de envío por SMTP
        print("[INFO] En producción, aquí se enviaría el email vía SMTP.")


def notificar_incidentes_criticos(archivo_incidentes: str = "incidentes.json",
                                  destinatarios: Optional[List[str]] = None) -> None:
    """Revisa incidentes y notifica los críticos o de alta severidad.
    
    Args:
        archivo_incidentes: Archivo JSON con los incidentes.
        destinatarios: Lista de emails a notificar.
    """
    
    if destinatarios is None:
        destinatarios = ["admin@empresa.com", "soporte@empresa.com"]
    
    try:
        with open(archivo_incidentes, "r", encoding="utf-8") as f:
            incidentes = json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo {archivo_incidentes}")
        return
    
    incidentes_criticos = [
        inc for inc in incidentes 
        if inc.get("severidad", "").upper() in ["CRÍTICA", "ALTA"] 
        and inc.get("estado", "").upper() == "ABIERTO"
    ]
    
    if not incidentes_criticos:
        print("\n✓ No hay incidentes críticos o de alta severidad abiertos.")
        return
    
    print(f"\n⚠️  Se encontraron {len(incidentes_criticos)} incidentes que requieren notificación.\n")
    
    for incidente in incidentes_criticos:
        enviar_notificacion(incidente, destinatarios, simular=True)
        print("\n" + "-" * 70 + "\n")


if __name__ == "__main__":
    print("=== SISTEMA DE NOTIFICACIONES DE INCIDENTES ===\n")
    print("1. Notificar incidentes críticos pendientes")
    print("2. Crear y notificar un incidente de prueba")
    print("3. Salir")
    
    opcion = input("\nSelecciona una opción: ").strip()
    
    if opcion == "1":
        emails = input("\nEmails de destinatarios (separados por comas): ").strip()
        destinatarios = [e.strip() for e in emails.split(",")] if emails else None
        notificar_incidentes_criticos(destinatarios=destinatarios)
    
    elif opcion == "2":
        # Crear incidente de prueba
        incidente_prueba = {
            "id": datetime.now().strftime("%Y%m%d%H%M%S"),
            "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "tipo": "Acceso no autorizado",
            "severidad": "CRÍTICA",
            "descripcion": "Detección de múltiples intentos de acceso desde IP desconocida",
            "sistema_afectado": "Servidor de producción - 192.168.1.100",
            "reportado_por": "Sistema automático de monitorización",
            "estado": "ABIERTO"
        }
        
        emails = input("\nEmails de destinatarios (separados por comas): ").strip()
        destinatarios = [e.strip() for e in emails.split(",")] if emails else ["admin@empresa.com"]
        
        enviar_notificacion(incidente_prueba, destinatarios, simular=True)
    
    elif opcion == "3":
        print("Saliendo...")
    
    else:
        print("[ERROR] Opción no válida.")
