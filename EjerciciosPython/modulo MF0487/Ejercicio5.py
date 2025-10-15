"""Generador interactivo de plan de auditoría en formato JSON."""

import json


def create_audit_plan() -> None:
    """Solicita los campos principales de un plan de auditoría y los guarda en JSON."""

    # Cada campo se acompaña de un ejemplo para orientar la respuesta del usuario.
    plan = {
        "alcance": input(
            "Define el alcance de la auditoría (ej. Infraestructura cloud de producción): "
        ),
        "criterios": input(
            "Normativa aplicable (ej. ISO 27001, RGPD, ENS...): "
        ),
        "recursos": input(
            "Recursos necesarios (ej. 2 auditores, acceso remoto, herramientas de escaneo): "
        ),
        "fases": input(
            "Fases del proceso (ej. Planificación, recabado de evidencias, informe): "
        ),
        "indicadores": input(
            "Indicadores de éxito (ej. % de controles cumplidos, nº hallazgos críticos = 0): "
        ),
    }

    with open("plan_auditoria.json", "w", encoding="utf-8") as descriptor:
        json.dump(plan, descriptor, indent=4, ensure_ascii=False)

    print("Plan guardado en plan_auditoria.json")


if __name__ == "__main__":
    create_audit_plan()
