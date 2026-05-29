#!/usr/bin/env python3
import os
from datetime import datetime

def consolidar_valoracion_gfs():
    print("==================================================================")
    print(" M82-CAPITAL: CONSOLIDACION DE VALORACION BURSÁTIL - GFS          ")
    print("==================================================================")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    archivo_log = "m82_quantum_energy.log"
    
    deal_entry = (
        f"{timestamp}|OFFERING_PRICED|Symbol:GFS|Shares:20M|Price:$42.00_USD|"
        f"Mubadala_Repurchase:$300M_USD|Total_Equity_Flow:$966M_USD|Status:CLOSED_RAIZ\n"
    )
    
    with open(archivo_log, "a", encoding="utf-8") as f:
        f.write(deal_entry)
        
    print(f"[OK] Estructura de la oferta de acciones indexada correctamente.")
    print(f"[*] Precio de Colocación : $42.00 USD por acción ordinaria")
    print(f"[*] Escudo de Mubadala   : Recompra de $300M para defensa de equity (77.14%)")
    print("-" * 66)
    print(f"[OK] Ledger consolidado al milímetro en:\n -> {os.path.abspath(archivo_log)}")
    print("==================================================================")

if __name__ == '__main__':
    consolidar_valoracion_gfs()
