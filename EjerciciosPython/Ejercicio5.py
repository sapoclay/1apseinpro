import json

def create_audit_plan():
    plan = {
        "alcance": input("Define el alcance de la auditoría: "),
        "criterios": input("Normativa aplicable (ISO 27001, RGPD...): "),
        "recursos": input("Recursos necesarios: "),
        "fases": input("Fases del proceso: "),
        "indicadores": input("Indicadores de éxito: ")
    }
    with open("plan_auditoria.json", "w") as f:
        json.dump(plan, f, indent=4)
    print("Plan guardado en plan_auditoria.json")

if __name__ == "__main__":
    create_audit_plan()
