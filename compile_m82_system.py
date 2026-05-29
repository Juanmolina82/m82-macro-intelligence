import os
import matplotlib.pyplot as plt

def generate_m82_chart():
    weeks = ['May 01', 'May 08', 'May 15']
    volumes = [400000, 588000, 713000]

    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    fig, ax = plt.subplots(figsize=(7, 3.4), dpi=300)
    
    ax.plot(weeks, volumes, color='#1a365d', linewidth=2.5, marker='o', markersize=8)
    ax.fill_between(weeks, volumes, color='#ebf8ff', alpha=0.5)

    for i, txt in enumerate(volumes):
        ax.annotate(f"{txt:,} bpd", (weeks[i], volumes[i]), textcoords="offset points", 
                    xytext=(0,10), ha='center', fontsize=9, fontweight='bold', color='#2d3748')

    ax.set_title('VE-CRDIMPW-EIA TRACKER: PARABOLIC SURGE INTO US GULF COAST', fontsize=9.5, fontweight='bold', color='#1a365d', pad=14)
    ax.set_ylabel('Barrels per Day (bpd)', fontsize=8, fontweight='bold', color='#4a5568')
    ax.set_ylim(300000, 800000)
    ax.tick_params(axis='both', labelsize=9, colors='#4a5568')
    ax.grid(True, linestyle='--', alpha=0.6, color='#e2e8f0')
    
    for spine in ['top', 'right', 'left', 'bottom']:
        ax.spines[spine].set_visible(False)

    plt.tight_layout()
    chart_path = 'm82_corridor_velocity_2026.png'
    plt.savefig(chart_path, bbox_inches='tight', transparent=True)
    plt.close()
    return chart_path

def generate_m82_document(chart_img_path):
    from weasyprint import HTML
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M82 Workspace - Molina Holdings Strategy Memo</title>
        <style>
            @page {{
                size: letter;
                margin: 20mm 15mm 20mm 15mm;
                @bottom-right {{
                    content: "Page " counter(page);
                    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                    font-size: 8pt;
                    color: #718096;
                }}
                @bottom-left {{
                    content: "M82 WORKSPACE // MASTER DATA CONSOLIDATION // MOLINA HOLDINGS LLC & MOLINA GLOBAL LLC v4.8";
                    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                    font-size: 8pt;
                    font-weight: bold;
                    color: #1a365d;
                }}
            }}
            
            body {{
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                font-size: 9.5pt;
                line-height: 1.45;
                color: #2d3748;
                margin: 0;
                padding: 0;
            }}

            .page-break {{
                page-break-before: always;
            }}

            .memo-header {{
                border-bottom: 3px solid #1a365d;
                padding-bottom: 8px;
                margin-bottom: 15px;
            }}

            .logo-title {{
                font-size: 15pt;
                font-weight: bold;
                color: #1a365d;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                margin: 0;
            }}

            .sub-title {{
                font-size: 8pt;
                font-weight: bold;
                color: #4a5568;
                margin: 2px 0 0 0;
                letter-spacing: 1px;
            }}

            .meta-table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 18px;
                background-color: #f7fafc;
            }}

            .meta-table td {{
                padding: 5px 8px;
                font-size: 8.5pt;
                border: 1px solid #e2e8f0;
            }}

            .meta-table td.label {{
                font-weight: bold;
                color: #1a365d;
                width: 18%;
                text-transform: uppercase;
                background-color: #edf2f7;
            }}

            h2 {{
                font-size: 10.5pt;
                color: #1a365d;
                border-bottom: 1.5px solid #2b6cb0;
                padding-bottom: 2px;
                margin-top: 18px;
                margin-bottom: 8px;
                text-transform: uppercase;
                page-break-after: avoid;
            }}

            p {{
                margin: 0 0 8px 0;
                text-align: justify;
            }}

            .highlight-box {{
                background-color: #f0fff4;
                border-left: 4px solid #38a169;
                padding: 10px 12px;
                margin: 12px 0;
                font-size: 9pt;
                text-align: justify;
            }}

            .highlight-box strong {{
                color: #276749;
            }}

            .data-table {{
                width: 100%;
                border-collapse: collapse;
                margin: 12px 0;
            }}

            .data-table th {{
                background-color: #1a365d;
                color: #ffffff;
                font-weight: bold;
                font-size: 8pt;
                text-transform: uppercase;
                padding: 6px 8px;
                border: 1px solid #1a365d;
            }}

            .data-table td {{
                padding: 6px 8px;
                font-size: 8.5pt;
                border: 1px solid #e2e8f0;
            }}

            .data-table tr:nth-child(even) {{
                background-color: #f7fafc;
            }}

            .text-center {{ text-align: center; }}
            .font-bold {{ font-weight: bold; }}

            .chart-container {{
                text-align: center;
                margin: 15px 0;
            }}

            .chart-container img {{
                width: 75%;
                height: auto;
            }}

            .cc-footer {{
                margin-top: 20px;
                padding-top: 10px;
                border-top: 1px dashed #cbd5e0;
                font-size: 8.5pt;
                color: #4a5568;
            }}
        </style>
    </head>
    <body>

        <div class="memo-header">
            <h1 class="logo-title">M82 Workspace // Institutional Data Decoupling</h1>
            <div class="sub-title">MOLINA HOLDINGS LLC & MOLINA GLOBAL LLC // REPORT CONSOLIDADO MAYO 2026</div>
        </div>

        <table class="meta-table">
            <tr>
                <td class="label">Macro & Fed Link:</td>
                <td>S&P 500 P/E: 21.1x | US GDP: 1.6% | PCE Inflation: 3.8% | Bessent-Warsh Accord</td>
                <td class="label">Date:</td>
                <td>May 28, 2026</td>
            </tr>
            <tr>
                <td class="label">EIA Inventory Sync:</td>
                <td>Crude: -3.3M bbl | SPR: -9.1M bbl | Refinery Capacity: 94.5% | Gas: Week 15 Draw</td>
                <td class="label">Auditor Control:</td>
                <td class="font-bold" style="color: #2b6cb0;">KPMG US Independent Audit</td>
            </tr>
        </table>

        <h2>1. Desconexión Estructural: Múltiplos Bursátiles vs. Escasez Física</h2>
        <p>
            <strong>Análisis Macroeconómico Integrado (EIA & Equity Valuation Sync):</strong> Al cierre de la jornada de este jueves, el mercado de capitales tradicional exhibe una dislocación asimétrica que valida la tesis de arbitraje del fondo. Mientras los índices bursátiles en Wall Street operan en máximos históricos ficticios debido a la concentración extrema en firmas mega-cap de tecnología (llevando el ratio PER adelantado del S&P 500 a un nivel estirado de <strong>21.1x</strong> frente a su media de 16.0x), los indicadores de la economía real señalan un escenario de estanflación estructural combinada con una severa escasez física de commodities.
        </p>
        <p>
            El crecimiento del PIB de EE. UU. se ha desacelerado al 1.6% en el primer trimestre, mientras que el índice de precios PCE escaló al 3.8% interanual. Paralelamente, los datos oficiales de la EIA revelan que el sistema de refinación norteamericano está operando bajo presión crítica: la utilización de capacidad saltó al <strong>94.5%</strong> para procesar cerca de 17 millones de bpd, provocando la <strong>quinta caída semanal consecutiva en inventarios de crudo (-3.3M bbl)</strong> y la <strong>décima quinta (15ª) semana consecutiva de drenaje en gasolina (-2.6M bbl)</strong>. Para mitigar los cuellos de botella derivados del conflicto en el Estrecho de Hormuz, el Departamento de Energía liquidó <strong>9.1 millones de barriles de la Reserva Estratégica (SPR)</strong> en un solo ciclo.
        </p>

        <ul>
            <li><strong>Inmunización del Tracker VE-CRDIMPW-EIA:</strong> Frente al dilema de política monetaria que enfrenta el Presidente de la Fed, Kevin Warsh, y tras su desayuno estratégico de coordinación institucional con el Secretario del Tesoro, Scott Bessent, queda confirmado que el banco central no puede expandir múltiplos de papel sin pinchar la burbuja de Wall Street. Nuestro corredor de flujo físico captura valor directamente de la inelástica demanda de refinación pesada, operando de forma independiente al ciclo de tasas de interés.</li>
        </ul>

        <div class="chart-container">
            <img src="{chart_img_path}" alt="VE-CRDIMPW-EIA Tracker Chart">
        </div>

        <h2>2. Monetización, Liquidez y Gobernanza Escrow</h2>
        <p>
            Durante las tres semanas de operaciones de marcha blanca en mayo de 2026, el volumen físico consolidado e inyectado en la Costa del Golfo alcanzó los <strong>11.9 millones de barriles</strong>, liquidando un valor acumulado en el mercado de spot de <strong>$857.3 millones de dólares (USD)</strong>.
        </p>
        
        <div class="highlight-box">
            <strong>Protección Fiduciaria y Respaldo de Big Four:</strong> El volumen acumulado total desde el inicio del ciclo operacional (3 de enero) se consolida en <strong>32.4 millones de barriles</strong>, movilizando nocionales financieros líquidos por un valor de <strong>~$2,330 millones de dólares (USD)</strong>. Siguiendo rigurosos protocolos corporativos coordinados con <strong>KPMG US</strong>, estos capitales se encuentran totalmente aislados de la volatilidad cambiaria o de correcciones bursátiles en cuentas escrow segregadas, moviéndose con absoluta predictibilidad hacia el hito de liquidación del <strong>19 de junio</strong>.
        </div>

        <div class="page-break"></div>

        <div class="memo-header">
            <h1 class="logo-title">M82 Workspace // Strategic Horizon</h1>
            <div class="sub-title">STATE 51 MODEL & INSTITUTIONAL DISTRIBUTION CODES</div>
        </div>

        <h2>3. El Horizonte Macro y el Modelo State 51</h2>
        <p>
            El flujo masivo y tutelado de este corredor energético actúa como el cimiento técnico real para la restauración duradera del Estado de Derecho (Rule of Law). El objetivo post-electoral de largo plazo permanece inalterado: consolidar la integración económica regional bajo el perímetro regulatorio y de defensa del modelo hemisférico <strong>#State51</strong>.
        </p>
        <p>
            Frente al estiramiento de las valoraciones de papel tradicionales, la predictibilidad financiera internacional de vanguardia no se busca en la volatilidad de Wall Street, sino en contratos de derecho privado y estructuras corporativas herméticas bajo Common Law de control estadounidense. <strong>Molina Holdings LLC</strong> (Tennessee) y <strong>Molina Global LLC</strong> (Delaware) operan como vehículos limpios ex-sovereign, aislando los activos privados midstream de cualquier contingencia aduanera, burbuja financiera o reconfiguración del orden de divisas en ultramar.
        </p>

        <h2>4. Fiduciary Distribution Network</h2>
        <table class="data-table">
            <thead>
                <tr>
                    <th>Estructura Legal M82</th>
                    <th>Jurisdicción de Control</th>
                    <th>Estatus de Operación en Marcha Blanca</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="font-bold">Molina Holdings LLC</td>
                    <td>Tennessee, USA</td>
                    <td>Custodio de la Propiedad Intelectual y Matriz de Inversión Corporativa.</td>
                </tr>
                <tr>
                    <td class="font-bold">Molina Global LLC</td>
                    <td>Delaware, USA</td>
                    <td>Socio General (General Partner) y ejecutor de los esquemas de distribución.</td>
                </tr>
                <tr>
                    <td class="font-bold">Auditoría Externa</td>
                    <td>KPMG US / Federal</td>
                    <td>Verificación de saldos en cuentas escrow e inmunización de flujos de capital.</td>
                </tr>
            </tbody>
        </table>

        <div class="cc-footer">
            <strong>M82 Workspace Institutional CC Distribution Network:</strong><br>
            Cc: Jane Fraser (Citi) // Andy Sieg (Citi Wealth) // Doug Burgum // MarketAxess // María Corina Machado Parisca // Pedro Urruchurtu Noselli
        </div>

    </body>
    </html>
    """
    
    html_path = 'temp_m82_master_memo.html'
    pdf_path = 'Molina_Holdings_M82_Master_v4.8.pdf'
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    print("[M82 INITIATING V4.8] Compilando reporte maestro con datos consolidados de la EIA, PER Bursatil y Desayuno Bessent-Warsh...")
    HTML(html_path).write_pdf(pdf_path)
    
    if os.path.exists(html_path):
        os.remove(html_path)
        
    print(f"\n[M82 MASTER INTEGRATION COMPLETE] PDF V4.8 generado con exito: {pdf_path}")

if __name__ == "__main__":
    chart_file = generate_m82_chart()
    generate_m82_document(chart_file)

# ==============================================================================
# INELASTIC COLLATERAL RIDER (INTEGRATED FROM APOLLO-BLACKSTONE INFRASTRUCTURE DOCTRINE)
# ==============================================================================
# * Application: Synthetic High-Grade structuring applied to Midstream & Energy.
# * Asset Isolation: Physical infrastructure operations are legally uncoupled from 
#   local fiat/political volatility through Delaware-governed leaseback mechanisms.
# * Credit Enhancement: Commercial risk minimized via global operator guarantees, 
#   mirroring the Broadcom/Google TPU protective structure.
# * Institutional Destination: Capturing global treasury liquidity fleeing paper 
#   markets to anchor it into physical energy assets (US to Venezuela Corridor).
