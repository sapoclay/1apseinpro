"""Detección rápida de IPs con actividad anómala en un access.log."""

from collections import Counter


def analyze_logs(filename):
    """Imprime las IPs con más de 50 accesos en el fichero indicado."""

    with open(filename, encoding="utf-8") as descriptor:
        # Obtenemos la IP (primer campo) de cada línea con contenido.
        ips = [line.split()[0] for line in descriptor if line.strip()]

    contador = Counter(ips)
    sospechosas = {ip: total for ip, total in contador.items() if total > 50}

    print("IPs sospechosas (más de 50 accesos):")
    for ip, total in sospechosas.items():
        print(f"{ip} -> {total} accesos")


if __name__ == "__main__":
    analyze_logs("access.log")
