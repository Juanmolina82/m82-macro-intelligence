#!/usr/bin/env python3
import os
import json
from datetime import datetime

def inicializar_y_procesar_matriz():
    print("==================================================================")
    print(" M82-CORE v2.0: MOTOR DE INTELIGENCIA Y MAPEO DE TUBERÍAS         ")
    print("==================================================================")
    
    archivo_db = "m82_watchlist_matrix.json"
    archivo_log = "m82_quantum_energy.log"
    timestamp_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    watchlist_data = {
        "metadata": {
            "version": "14.5-Sovereign",
            "last_update": timestamp_actual,
            "system_status": "OPERATIONAL",
            "focus_vector": "Venezuela 3.0 / Clearing & Frontier Infrastructure"
        },
        "capas": {
            "CAPA_1_FISICA": {
                "descripcion": "Infraestructura Física, Recursos y Upstream Energético",
                "focus": "Capex Real, Cubicaje y Capacidad de Reinversión",
                "nodos": {
                    "OXY": {"nombre": "Occidental Petroleum", "tipo": "Energía / Upstream", "yield_target": "1.8%"},
                    "CHINA_SHENHUA": {"nombre": "China Shenhua Energy", "tipo": "Carbón / Materia Prima", "yield_target": "6.5%"},
                    "ZIJIN_MINING": {"nombre": "Zijin Mining Group", "tipo": "Metales Críticos / Oro", "yield_target": "1.7%"},
                    "TRANSALTA": {"nombre": "TransAlta Corp", "tipo": "Electricidad / Utilities Base", "yield_target": "1.6%"}
                }
            },
            "CAPA_2_FINANCIERA": {
                "descripcion": "Custodia Global, Clearing de Activos y Fontanería Financiera",
                "focus": "Volumen de Activos Bajo Custodia (AUC) y Emisión de ETFs",
                "nodos": {
                    "STT": {"nombre": "State Street Corp", "tipo": "Custodia Core / ETF Plumbing", "yield_target": "2.8%"},
                    "BLK": {"nombre": "BlackRock Inc", "tipo": "Gestor de Activos / Dueño Silencioso", "yield_target": "2.2%"},
                    "JPM": {"nombre": "JPMorgan Chase & Co", "tipo": "Clearing Dólar / Banca Sistémica", "yield_target": "1.9%"},
                    "BAM": {"nombre": "Brookfield Asset Mgmt", "tipo": "Private Equity / Infraestructura Estructural", "yield_target": "3.5%"},
                    "KKR": {"nombre": "KKR & Co Inc", "tipo": "Activos Alternativos / Comprador Distressed", "yield_target": "1.2%"}
                }
            },
            "CAPA_3_COMPUTO": {
                "descripcion": "Rieles de Datos, Procesamiento de Silicio y Capa Lógica de IA",
                "focus": "Monopolio Informático y Soberanía de Datos Corporativos",
                "nodos": {
                    "MSFT": {"nombre": "Microsoft Corp", "tipo": "Cloud / Azure AI Rails", "yield_target": "0.7%"},
                    "AVGO": {"nombre": "Broadcom Inc", "tipo": "Diseño de Silicio / Redes", "yield_target": "1.1%"},
                    "AMD": {"nombre": "Advanced Micro Devices", "tipo": "Procesamiento Gráfico & Cómputo", "yield_target": "0.0%"},
                    "PLTR": {"nombre": "Palantir Technologies", "tipo": "Sistemas Operativos de Inteligencia / Defensa", "yield_target": "0.0%"}
                }
            }
        }
    }

    try:
        with open(archivo_db, "w", encoding="utf-8") as f_json:
            json.dump(watchlist_data, f_json, indent=4, ensure_ascii=False)
        
        with open(archivo_log, "w", encoding="utf-8") as f_log:
            f_log.write(f"// M82 SOVEREIGN MATRIX LOG | AUDIT TIMESTAMP: {timestamp_actual}\n")
            f_log.write(f"// VECTOR DE ENFOQUE: {watchlist_data['metadata']['focus_vector']}\n")
            f_log.write("="*80 + "\n")
            for capa_id, capa_info in watchlist_data["capas"].items():
                f_log.write(f"[{capa_id}] - {capa_info['descripcion']}\n")
                f_log.write(f"CRITERIO ANALÍTICO: {capa_info['focus']}\n")
                f_log.write("-"*80 + "\n")
                for ticker, detalles in capa_info["nodos"].items():
                    f_log.write(f"   -> TICKER: {ticker:<15} | {detalles['nombre']:<25} | TIPO: {detalles['tipo']:<30} | TARGET YIELD: {detalles['yield_target']}\n")
                f_log.write("="*80 + "\n")
                
        print(f"[OK] Base de datos JSON estructurada en:\n -> {os.path.abspath(archivo_db)}")
        print(f"[OK] Manifiesto analítico guardado en:\n -> {os.path.abspath(archivo_log)}")
        print("\n" + "-"*40 + " RESUMEN OPERATIVO M82 " + "-"*40)
        for capa_id, capa_info in watchlist_data["capas"].items():
            print(f"[*] {capa_id:<20}: {len(capa_info['nodos'])} Nodos Estratégicos Bajo Monitoreo.")
        print("-" * 103)
    except IOError as e:
        print(f"[CRITICAL] Error: {e}")
    print("==================================================================")

if __name__ == '__main__':
    inicializar_y_procesar_matriz()
