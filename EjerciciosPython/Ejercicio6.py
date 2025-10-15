from Ejercicio1 import scan_ports
from Ejercicio3 import test_common_paths
import json

def full_audit(host):
    result = {
        "host": host,
        "ports": scan_ports(host, range(20, 1025)),
        "web_paths": test_common_paths(f"http://{host}")
    }
    result["riesgo"] = "ALTO" if len(result["ports"]) > 10 else "MEDIO"
    return result

if __name__ == "__main__":
    host = input("Host a auditar: ")
    res = full_audit(host)
    with open("informe_integral.json", "w") as f:
        json.dump(res, f, indent=4)
    print("Auditoría completa guardada en informe_integral.json")
