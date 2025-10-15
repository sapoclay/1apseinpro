import json

def evaluate_risks(file="informe_integral.json"):
    with open(file) as f:
        data = json.load(f)

    probabilidad = len(data["ports"]) / 100
    impacto = 0.7 if data["riesgo"] == "ALTO" else 0.4
    riesgo = probabilidad * impacto

    print(f"Riesgo calculado: {riesgo:.2f}")
    if riesgo > 0.5:
        print("⚠️ Riesgo elevado. Requiere medidas.")
    else:
        print("✅ Riesgo aceptable.")

if __name__ == "__main__":
    evaluate_risks()
