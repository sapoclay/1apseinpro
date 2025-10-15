from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import json

def generar_informe(json_file, pdf_file="informe_final.pdf"):
    with open(json_file) as f:
        data = json.load(f)

    doc = SimpleDocTemplate(pdf_file, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Informe de Auditoría de Seguridad", styles['Title']))
    story.append(Spacer(1, 12))
    for k, v in data.items():
        story.append(Paragraph(f"<b>{k.capitalize()}:</b> {v}", styles['Normal']))
        story.append(Spacer(1, 8))
    doc.build(story)
    print(f"Informe generado: {pdf_file}")

if __name__ == "__main__":
    generar_informe("informe_integral.json")
