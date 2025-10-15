"""Auditoría integral: puertos abiertos, rutas web comunes y nivel de riesgo."""

import json

from Ejercicio1 import scan_ports
from Ejercicio3 import test_common_paths


def full_audit(host):
    """Devuelve un informe compacto con escaneo de puertos y rutas web comunes."""

    resultado = {
        "host": host,
        "ports": scan_ports(host, range(20, 1025)),
        "web_paths": test_common_paths(f"http://{host}")
    }
    # Estimación general basada en el número de puertos descubiertos.
    resultado["riesgo"] = "ALTO" if len(resultado["ports"]) > 10 else "MEDIO"
    return resultado


if __name__ == "__main__":
    objetivo = input("Host a auditar: ")
    informe = full_audit(objetivo)
    with open("informe_integral.json", "w", encoding="utf-8") as descriptor:
        json.dump(informe, descriptor, indent=4, ensure_ascii=False)
    print("Auditoría completa guardada en informe_integral.json")
