"""Herramientas básicas para comprobar conectividad y crear un informe CSV."""

import subprocess
import platform
import csv
import shutil

def ping(host):
    """Ejecuta ping contra un host concreto y devuelve la salida en texto."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "3", host]
    return subprocess.run(command, capture_output=True, text=True).stdout

def traceroute(host):
    """Obtiene la ruta hacia un host usando tracert/traceroute si está disponible."""
    cmd = "tracert" if platform.system().lower() == "windows" else "traceroute"
    if shutil.which(cmd) is None:
        return f"La utilidad {cmd} no está disponible en este sistema."
    return subprocess.run([cmd, host], capture_output=True, text=True).stdout

def save_report(results, filename="network_report.csv"):
    """Genera un CSV con los resultados de ping y traceroute para cada host."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Host", "Ping", "Traceroute"])
        for host, data in results.items():
            writer.writerow([host, data["ping"], data["trace"]])

if __name__ == "__main__":
    # Lista de destinos que se usarán para el diagnóstico rápido.
    hosts = ["google.com", "github.com", "python.org"]
    results = {}
    for h in hosts:
        ping_output = ping(h)
        trace_output = traceroute(h)
        results[h] = {
            "ping": ping_output,
            "trace": trace_output
        }
        print(f"\n=== {h} ===")
        print(ping_output.strip() or "Sin datos de ping")
        print(trace_output.strip() or "Sin datos de traceroute")
    save_report(results)
    print("Informe guardado en network_report.csv")
