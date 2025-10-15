"""Comparador básico entre configuraciones antiguas y nuevas de firewall."""


def compare_firewall_rules(file1, file2):
    """Muestra reglas añadidas y eliminadas entre dos ficheros de configuración."""

    with open(file1, encoding="utf-8") as original, open(file2, encoding="utf-8") as actualizado:
        reglas_antiguas = set(original.read().splitlines())
        reglas_nuevas = set(actualizado.read().splitlines())

    nuevas = reglas_nuevas - reglas_antiguas
    eliminadas = reglas_antiguas - reglas_nuevas

    print("Reglas añadidas:", nuevas)
    print("Reglas eliminadas:", eliminadas)


if __name__ == "__main__":
    compare_firewall_rules("firewall_old.txt", "firewall_new.txt")
