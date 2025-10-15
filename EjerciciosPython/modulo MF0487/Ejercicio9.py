"""Calcula un índice de riesgo a partir del informe integral de auditoría."""

import json


def evaluate_risks(file="informe_integral.json"):
    """Lee el informe integral y muestra un índice de riesgo simplificado."""

    with open(file, encoding="utf-8") as descriptor:
        data = json.load(descriptor)

    probabilidad = len(data.get("ports", [])) / 100
    impacto = 0.7 if data.get("riesgo") == "ALTO" else 0.4
    riesgo = probabilidad * impacto

    print(f"Riesgo calculado: {riesgo:.2f}")
    if riesgo > 0.5:
        print("⚠️ Riesgo elevado. Requiere medidas.")
    else:
        print("✅ Riesgo aceptable.")


if __name__ == "__main__":
    evaluate_risks()
