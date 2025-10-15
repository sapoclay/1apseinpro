"""Generación de informe PDF a partir del resultado de la auditoría integral."""

import json

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def generar_informe(json_file, pdf_file="informe_final.pdf"):
    """Crea un PDF resumido con los campos presentes en json_file."""

    with open(json_file, encoding="utf-8") as descriptor:
        data = json.load(descriptor)

    documento = SimpleDocTemplate(pdf_file, pagesize=A4)
    estilos = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Informe de Auditoría de Seguridad", estilos["Title"]))
    story.append(Spacer(1, 12))
    for clave, valor in data.items():
        story.append(Paragraph(f"<b>{clave.capitalize()}:</b> {valor}", estilos["Normal"]))
        story.append(Spacer(1, 8))

    documento.build(story)
    print(f"Informe generado: {pdf_file}")


if __name__ == "__main__":
    generar_informe("informe_integral.json")
