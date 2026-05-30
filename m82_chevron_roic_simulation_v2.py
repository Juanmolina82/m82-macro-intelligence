# -*- coding: utf-8 -*-
"""
============================================================================
SISTEMA M82 - SIMULACIÓN DE ROIC DE CHEVRON E INTEGRACIÓN CON CELONIS
============================================================================
"""
import json
import os
import time

def ejecutar_simulacion_pro():
    print("=" * 80)
    print("   [M82 SYSTEM] EXECUTING RIGOROUS CHEVRON ROIC MODEL (US GAAP / IFRS)   ")
    print("=" * 80)

    # Parámetros Base del Canal Midstream
    volumen_bpd = 1230000
    dias_ano = 365
    volumen_anual = volumen_bpd * dias_ano
    precio_barril_wti = 75.00
    ingreso_bruto = volumen_anual * precio_barril_wti
    capital_invested = 4500000000.0
    opex_por_barril = 12.00
    opex_anual = volumen_anual * opex_por_barril
    depreciacion = capital_invested * 0.05

    # Escenarios de Ajuste: [Regalía %, Impuesto %]
    escenarios = {
        "ACTUAL": {"regalia": 0.333, "tax": 0.50},
        "PROPUESTA_MEDIA": {"regalia": 0.20, "tax": 0.34},
        "PROPUESTA_AGRESIVA": {"regalia": 0.12, "tax": 0.25}
    }

    resultados = []

    for nombre, rates in escenarios.items():
        regalia_rate = rates["regalia"]
        tax_rate = rates["tax"]
        
        costo_regalias = ingreso_bruto * regalia_rate
        ebitda = ingreso_bruto - costo_regalias - opex_anual
        ebit = ebitda - depreciacion
        impuestos = max(0.0, ebit * tax_rate)
        nopat = ebit - impuestos
        roic = (nopat / capital_invested) * 100.0
        
        resultados.append({
            "Escenario": nombre,
            "Regalia_Pct": f"{regalia_rate*100}%",
            "Impuesto_Pct": f"{tax_rate*100}%",
            "Ingreso_Gross_USD": ingreso_bruto,
            "Costo_Regalias_USD": costo_regalias,
            "NOPAT_USD": nopat,
            "ROIC_Pct": f"{round(roic, 2)}%",
            "Viabilidad": "VIABLE" if roic >= 12.0 else "RECHAZADO"
        })

    # Persistencia Segura en el JSON Maestro de Telemetría
    json_file = 'm82_ultimate_telemetry_v240.json'
    if os.path.exists(json_file):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            data = {}
    else:
        data = {}

    if "release_metadata" not in data:
        data["release_metadata"] = {}

    data["release_metadata"]["version"] = "24.8.1-CHEVRON-CELONIS-INTEGRATED"
    data["release_metadata"]["last_update_utc"] = int(time.time())
    data["chevron_simulated_scenarios"] = resultados

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # Mostrar Matriz por Consola
    print(f"{'ESCENARIO':<20} | {'REGALÍA':<8} | {'IMPUESTO':<10} | {'ROIC (%)':<10} | {'ESTATUS':<10}")
    print("-" * 70)
    for r in resultados:
        print(f"{r['Escenario']:<20} | {r['Regalia_Pct']:<8} | {r['Impuesto_Pct']:<10} | {r['ROIC_Pct']:<10} | {r['Viabilidad']:<10}")
    print("=" * 80)
    print("[SUCCESS] Operational telemetry pipeline updated cleanly for Deloitte audit tracks.")

if __name__ == '__main__':
    ejecutar_simulacion_pro()
