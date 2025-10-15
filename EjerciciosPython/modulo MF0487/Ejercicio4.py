"""Comprobador simple de versiones recientes en PyPI para requirements.txt."""

from typing import Dict, Optional

import requests


def check_vulnerable(package: str) -> Optional[str]:
    """Devuelve la versión más reciente disponible en PyPI para *package*.

    Si la consulta falla o el paquete no existe, devuelve ``None``.
    """

    url = f"https://pypi.org/pypi/{package}/json"
    try:
        # Consulta a la API pública de PyPI con un timeout corto.
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return None
        return response.json()["info"]["version"]
    except Exception:
        return None


def analyze_requirements(file: str = "requirements.txt") -> Dict[str, str]:
    """Lee un archivo requirements.txt y devuelve las últimas versiones disponibles."""

    with open(file, encoding="utf-8") as config:
        # Cada línea puede incluir '==versión'; nos quedamos con el nombre del paquete.
        packages = [line.strip().split("==")[0] for line in config if line.strip()]

    report: Dict[str, str] = {}
    for pkg in packages:
        latest = check_vulnerable(pkg)
        report[pkg] = latest or "Desconocido"
    return report


if __name__ == "__main__":
    # Imprime por pantalla el informe sintetizado para cada dependencia.
    resultado = analyze_requirements()
    for paquete, version in resultado.items():
        print(f"{paquete}: versión más reciente {version}")
