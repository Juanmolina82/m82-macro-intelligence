import os
from datetime import datetime

def consolidar_matriz_soberana():
    print("==================================================================")
    print(" M82-LEDGER v12.8: MATRIZ DE CAPITAL DE RIESGO DE ESTADO SECTORIAL")
    print("==================================================================")
    
    ahora = datetime.now()
    fecha_cierre = ahora.strftime("%Y-%m-%d %H:%M")
    
    # Estructura de datos pura basada en el reporte consolidado
    matriz_equity = [
        {"ticker": "IBM", "funds": "$1,000M", "gain": "+11.3%", "asset": "Foundry Anderon 300mm"},
        {"ticker": "GFS", "funds": "$375M", "gain": "+13.9%", "asset": "Litografía Nacional"},
        {"ticker": "INFQ", "funds": "$100M", "gain": "+31.1%", "asset": "Sensores Cuánticos"},
        {"ticker": "RGTI", "funds": "$100M", "gain": "+26.5%", "asset": "Procesadores Superconductores"},
        {"ticker": "QBTS", "funds": "$100M", "gain": "+28.4%", "asset": "Sistemas de Annealing"}
    ]
    
    archivo_log = "m82_historical_closes.log"
    
    # Escritura en bloque para auditoría de la mesa de Miami
    with open(archivo_log, "a") as f:
        f.write(f"\n--- TIMESTAMED CLOSING LEDGER: {fecha_cierre} ---\n")
        for item in matriz_equity:
            line = f"{fecha_cierre}|CLOSED_MATRIX|{item['ticker']}|Funds:{item['funds']}|Gain:{item['gain']}|Asset:{item['asset']}\n"
            f.write(line)
            print(f"[INDEXADO] -> {item['ticker']} | {item['funds']} | {item['gain']} | {item['asset']}")
            
    print("-" * 66)
    print(f"[OK] Ledger consolidado de forma permanente en:\n -> {os.path.abspath(archivo_log)}")
    print("==================================================================")

if __name__ == '__main__':
    consolidar_matriz_soberana()
