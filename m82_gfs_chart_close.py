import os
from datetime import datetime

def registrar_cierre_grafico_gfs():
    print("==================================================================")
    print(" M82-TECHNICAL: GRABADO DE PRECIO DE CIERRE DE GRÁFICA - GFS      ")
    print("==================================================================")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    archivo_log = "m82_quantum_energy.log"
    
    # Inyección de los datos exactos del monitor visualizado
    chart_data = (
        f"{timestamp}|CHART_CLOSE|Symbol:GFS|Price_Close:52.12|Net_Change:+6.80|"
        f"Percentage:+15.00%|Intraday_Low:46.22|Premium_Over_Offering:+24.1%|Status:RESOLVED\n"
    )
    
    with open(archivo_log, "a") as f:
        f.write(chart_data)
        
    print(f"[OK] Acción del precio de la gráfica indexada de forma limpia.")
    print(f"[*] Precio de Cierre : $52.12 USD (Máximo del Día)")
    print(f"[*] Rango Evaluado  : $46.22 - $52.12 USD")
    print("-" * 66)
    print(f"[OK] Ledger técnico actualizado en raíz:\n -> {os.path.abspath(archivo_log)}")
    print("==================================================================")

if __name__ == '__main__':
    registrar_cierre_grafico_gfs()
