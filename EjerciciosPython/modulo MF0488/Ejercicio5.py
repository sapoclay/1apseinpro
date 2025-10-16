"""Generador de informes de incidentes en formato HTML."""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict


def generar_informe_html(archivo_incidentes: str = "incidentes.json", 
                         archivo_salida: str = "informe_incidentes.html") -> None:
    """Genera un informe HTML a partir de los incidentes registrados.
    
    Args:
        archivo_incidentes: Archivo JSON con los incidentes.
        archivo_salida: Nombre del archivo HTML de salida.
    """
    
    try:
        with open(archivo_incidentes, "r", encoding="utf-8") as f:
            incidentes = json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo {archivo_incidentes}")
        return
    except json.JSONDecodeError:
        print(f"[ERROR] El archivo {archivo_incidentes} no es un JSON válido")
        return
    
    if not incidentes:
        print("[AVISO] No hay incidentes para generar el informe.")
        return
    
    # Calcular estadísticas
    total = len(incidentes)
    por_severidad = {}
    por_tipo = {}
    
    for inc in incidentes:
        severidad = inc.get("severidad", "DESCONOCIDA")
        tipo = inc.get("tipo", "Desconocido")
        
        por_severidad[severidad] = por_severidad.get(severidad, 0) + 1
        por_tipo[tipo] = por_tipo.get(tipo, 0) + 1
    
    # Generar HTML
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Informe de Incidentes de Seguridad</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .stat-card h3 {{
            margin-top: 0;
            color: #667eea;
        }}
        .incidente {{
            background: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border-left: 5px solid #667eea;
        }}
        .incidente.critica {{
            border-left-color: #e74c3c;
        }}
        .incidente.alta {{
            border-left-color: #e67e22;
        }}
        .incidente.media {{
            border-left-color: #f39c12;
        }}
        .incidente.baja {{
            border-left-color: #3498db;
        }}
        .badge {{
            display: inline-block;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 0.85em;
            font-weight: bold;
            margin-right: 10px;
        }}
        .badge.critica {{
            background-color: #e74c3c;
            color: white;
        }}
        .badge.alta {{
            background-color: #e67e22;
            color: white;
        }}
        .badge.media {{
            background-color: #f39c12;
            color: white;
        }}
        .badge.baja {{
            background-color: #3498db;
            color: white;
        }}
        .badge.abierto {{
            background-color: #27ae60;
            color: white;
        }}
        .badge.cerrado {{
            background-color: #95a5a6;
            color: white;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            color: #7f8c8d;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 Informe de Incidentes de Seguridad</h1>
        <p>Generado: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    </div>
    
    <div class="stats">
        <div class="stat-card">
            <h3>Total de Incidentes</h3>
            <p style="font-size: 2em; margin: 0; font-weight: bold; color: #667eea;">{total}</p>
        </div>
"""
    
    # Estadísticas por severidad
    html += """        <div class="stat-card">
            <h3>Por Severidad</h3>
            <ul style="list-style: none; padding: 0;">
"""
    for sev, count in sorted(por_severidad.items()):
        html += f"                <li><strong>{sev}:</strong> {count}</li>\n"
    
    html += """            </ul>
        </div>
        <div class="stat-card">
            <h3>Por Tipo</h3>
            <ul style="list-style: none; padding: 0;">
"""
    
    for tipo, count in sorted(por_tipo.items()):
        html += f"                <li><strong>{tipo}:</strong> {count}</li>\n"
    
    html += """            </ul>
        </div>
    </div>
    
    <h2 style="color: #667eea;">Detalle de Incidentes</h2>
"""
    
    # Listar incidentes
    for inc in incidentes:
        severidad_class = inc.get("severidad", "").lower()
        html += f"""    <div class="incidente {severidad_class}">
        <h3>Incidente #{inc.get('id', 'N/A')}</h3>
        <p>
            <span class="badge {severidad_class}">{inc.get('severidad', 'N/A')}</span>
            <span class="badge {inc.get('estado', 'ABIERTO').lower()}">{inc.get('estado', 'ABIERTO')}</span>
        </p>
        <p><strong>Fecha:</strong> {inc.get('fecha_hora', 'N/A')}</p>
        <p><strong>Tipo:</strong> {inc.get('tipo', 'N/A')}</p>
        <p><strong>Sistema afectado:</strong> {inc.get('sistema_afectado', 'N/A')}</p>
        <p><strong>Descripción:</strong> {inc.get('descripcion', 'N/A')}</p>
        <p><strong>Reportado por:</strong> {inc.get('reportado_por', 'N/A')}</p>
    </div>
"""
    
    html += """    <div class="footer">
        <p>Informe generado automáticamente por el Sistema de Gestión de Incidentes</p>
    </div>
</body>
</html>
"""
    
    with open(archivo_salida, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"\n✓ Informe HTML generado: {archivo_salida}")


if __name__ == "__main__":
    generar_informe_html()
