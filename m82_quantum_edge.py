from datetime import datetime
import os

def registrar_cierre_infraestructura(brent, usdt, bloom_energy, qbts_gain):
    print("==================================================================")
    print(" M82-MONITOR v12.5: INFRAESTRUCTURA HÍBRIDA (OIL / ENERGÍA / QUANTUM) ")
    print("==================================================================")
    
    ahora = datetime.now()
    fecha_hora = ahora.strftime("%Y-%m-%d %H:%M")
    
    # Índice de estrés energético global cruzado con la tasa local
    energy_stress_index = (brent * bloom_energy) / 1000
    
    log_line = f"{fecha_hora}|QUANTUM_ENERGY_UPDATE|BE_Stock:${bloom_energy}|QBTS_Gain:{qbts_gain}%|EnergyStress:{energy_stress_index:.2f}|CalleUSDT:{usdt}\n"
    
    # Escritura asegurada en el archivo histórico unificado
    archivo_log = "m82_historical_closes.log"
    with open(archivo_log, "a") as f:
        f.write(log_line)
        
    print(f"[*] Marca de Tiempo    : {fecha_hora}")
    print(f"[*] Ticker Bloom (BE)  : ${bloom_energy} USD (Parabólico)")
    print(f"[*] D-Wave Quantum     : +{qbts_gain}% (Inyección Federal $2B)")
    print(f"[*] Coeficiente Energía: {energy_stress_index:.2f}")
    print(f"[*] Tasa Flotante P2P  : {usdt} VES/USDT")
    print("-" * 66)
    print(f"[OK] Métricas consolidadas en el nodo raíz: {os.path.abspath(archivo_log)}")
    print("==================================================================")

if __name__ == '__main__':
    # Entradas exactas de los paneles LSEG, Monitor Dólar y Schwab Network (Corte 3:12 PM)
    registrar_cierre_infraestructura(brent=102.90, usdt=720.23, bloom_energy=307.41, qbts_gain=30.10)
