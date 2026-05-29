# -*- coding: utf-8 -*-
import os
import sys

# 1. Asegurar la instalación automática de reportlab en Termux
try:
    import reportlab
except ImportError:
    print("[INFO] Instalandor ReportLab en Termux para soporte nativo de PDFs...")
    os.system("pip install reportlab")
    print("[INFO] Librería instalada correctamente.")

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def construir_pdf_termux():
    pdf_filename = "M82_Consolidated_Audit_Report_V24.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        rightMargin=40, leftMargin=40,
        topMargin=40, bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    story = []
    
    # Estilos Personalizados
    style_title = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#1A365D'),
        spaceAfter=4
    )
    
    style_subtitle = ParagraphStyle(
        'SubTitleStyle',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#3182CE'),
        spaceAfter=15
    )
    
    style_h2 = ParagraphStyle(
        'H2Style',
        parent=styles['Heading2'],
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#1A365D'),
        spaceBefore=15,
        spaceAfter=10
    )
    
    style_body = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#2D3748'),
        alignment=4 # Justificado
    )
    
    style_table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontSize=9,
        leading=11,
        textColor=colors.HexColor('#2D3748')
    )

    style_table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontSize=9,
        leading=11,
        textColor=colors.white,
        fontName='Helvetica-Bold'
    )

    # Encabezado Principal
    story.append(Paragraph("M82 WORLD SPY SYSTEM", style_title))
    story.append(Paragraph("CONSOLIDATED AUDIT REPORT // INFRASTRUCTURE AS CODE V24.0", style_subtitle))
    story.append(Spacer(1, 10))
    
    # Sección I
    story.append(Paragraph("I. Marco de Gobernabilidad Política", style_h2))
    txt_I = ("El <b>Manifiesto de Panamá - Por el Gran Acuerdo Nacional</b>, respaldado de manera "
             "inelástica por María Corina Machado y el Presidente Electo Edmundo González Urrutia, "
             "unifica la representación civil legítima. El canal institucional se alinea directamente con el "
             "Plan de Transición de 3 Fases coordinado bajo el track estratégico del Secretario Marco Rubio.")
    story.append(Paragraph(txt_I, style_body))
    story.append(Spacer(1, 10))
    
    # Sección II
    story.append(Paragraph("II. Matriz de Rotación Sectorial (LSEG Workspace)", style_h2))
    
    # Datos de la Tabla Estructurada
    data = [
        [Paragraph("Sector / Índice", style_table_header), 
         Paragraph("Cuadrante", style_table_header), 
         Paragraph("Comp. Técnico", style_table_header), 
         Paragraph("Flujo Neto", style_table_header), 
         Paragraph("Estado de Impulso", style_table_header)],
        [Paragraph("<b>XLK</b> (Tech)", style_table_cell), Paragraph("LEADING", style_table_cell), Paragraph("+16.89", style_table_cell), Paragraph("+505.0 M", style_table_cell), Paragraph("Rally Dell (+29.1%) en IA", style_table_cell)],
        [Paragraph("<b>XLV</b> (Healthcare)", style_table_cell), Paragraph("IMPROVING", style_table_cell), Paragraph("-6.70", style_table_cell), Paragraph("+138.0 M", style_table_cell), Paragraph("Acumulación preventiva", style_table_cell)],
        [Paragraph("<b>XLE</b> (Energy)", style_table_cell), Paragraph("LAGGING", style_table_cell), Paragraph("-10.20", style_table_cell), Paragraph("-392.0 M", style_table_cell), Paragraph("Drawdown técnico -36.31", style_table_cell)]
    ]
    
    t = Table(data, colWidths=[90, 75, 75, 70, 200])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2B6CB0')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F7FAFC')]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E0')),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))
    
    # Sección III
    story.append(Paragraph("III. Capa Fiduciaria e Inmunidad Contable", style_h2))
    txt_III = ("El capital corporativo privado bajo custodia de <b>Molina Holdings LLC</b> valorado en "
               "USD 2,330,000,000, permanece blindado de forma absoluta mediante fideicomisos privados "
               "inelásticos. Las estructuras de activos físicos midstream (corredor operativo de 1.23M bpd) "
               "se encuentran totalmente aisladas de litigios externos de acreedores (Citgo/PDV Holding) "
               "y han sido auditadas bajo principios contables US GAAP por la firma internacional <b>KPMG US</b>.")
    story.append(Paragraph(txt_III, style_body))
    story.append(Spacer(1, 20))
    
    # Pie de página / Estado de Consola
    style_footer = ParagraphStyle(
        'FooterStyle',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.HexColor('#718096')
    )
    story.append(Paragraph("<b>ESTADO: OPERATIONAL_STABLE</b> // REPOSITORIO DE CLOUD SIN CONFLICTOS", style_footer))
    
    # Construcción física del documento
    doc.build(story)
    print(f"\n[SUCCESS] PDF Compilado nativamente en Termux: {pdf_filename}")

if __name__ == '__main__':
    construir_pdf_termux()
