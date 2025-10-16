"""Detector de correos de phishing mediante análisis de palabras clave sospechosas."""

import re
from typing import Any, Dict, List


def detectar_phishing(mensaje: str) -> Dict[str, Any]:
    """Analiza un mensaje de correo y detecta indicadores de phishing.
    
    Args:
        mensaje: Texto completo del correo a analizar.
        
    Returns:
        Diccionario con el resultado del análisis y las palabras sospechosas encontradas.
    """
    
    # Palabras y frases comunes en correos de phishing
    palabras_sospechosas = [
        "urgente", "verificar cuenta", "suspendido", "contraseña", 
        "confirmar", "premio", "lotería", "ganador", "haga clic",
        "actualizar datos", "banco", "tarjeta", "caducado"
    ]
    
    mensaje_lower = mensaje.lower()
    encontradas = [palabra for palabra in palabras_sospechosas if palabra in mensaje_lower]
    
    # Detectar URLs sospechosas
    urls = re.findall(r'https?://[^\s]+', mensaje)
    
    # Detectar direcciones de email sospechosas
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', mensaje)
    
    puntuacion_riesgo = len(encontradas) * 10 + len(urls) * 5
    
    resultado = {
        "es_phishing": puntuacion_riesgo > 20,
        "puntuacion": puntuacion_riesgo,
        "palabras_sospechosas": encontradas,
        "urls_encontradas": urls,
        "emails_encontrados": emails,
        "nivel_riesgo": "ALTO" if puntuacion_riesgo > 40 else "MEDIO" if puntuacion_riesgo > 20 else "BAJO"
    }
    
    return resultado


if __name__ == "__main__":
    print("=== DETECTOR DE PHISHING ===\n")
    print("Introduce el texto del correo (finaliza con una línea vacía):")
    
    lineas = []
    while True:
        linea = input()
        if not linea:
            break
        lineas.append(linea)
    
    mensaje = "\n".join(lineas)
    
    if mensaje:
        resultado = detectar_phishing(mensaje)
        
        print("\n--- RESULTADO DEL ANÁLISIS ---")
        print(f"¿Es phishing? {'SÍ' if resultado['es_phishing'] else 'NO'}")
        print(f"Nivel de riesgo: {resultado['nivel_riesgo']}")
        print(f"Puntuación: {resultado['puntuacion']}")
        print(f"\nPalabras sospechosas: {', '.join(resultado['palabras_sospechosas']) if resultado['palabras_sospechosas'] else 'Ninguna'}")
        print(f"URLs encontradas: {len(resultado['urls_encontradas'])}")
        print(f"Emails encontrados: {len(resultado['emails_encontrados'])}")
    else:
        print("[ERROR] No se introdujo ningún texto.")
