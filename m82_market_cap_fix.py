import os
from datetime import datetime

def registrar_market_caps():
    print("==================================================================")
    print(" M82-QUANTUM v13.3: COMPARTIMENTO DE VALORACIONES DE MERCADO REAL ")
    print("==================================================================")
    
    ahora = datetime.now()
    stamp = ahora.strftime("%Y-%m-%d %H:%M")
    
    # Destino del log estrictamente aislado de tecnología
    archivo_target = "m82_quantum_energy.log"
    
    # Datos exactos extraídos de la gráfica de barras de Schwab Network
    log_data = (
        f"{stamp}|MARKET_CAP_CONFIRMED|QBTS_Val:$7.1B|RGTI_Val:$4.8B|"
        f"INFQ_Val:$1.2B|Gov_Investment:$100M_Each|Dilucion_QBTS:1.40%\n"
    )
    
    with open(archivo_target, "a") as f:
        f.write(log_data)
        
    print(f"[*] Datos de Capitalización Bursátil Guardados.")
    print(f"[*] D-Wave Market Value  : $7.1B (Dilución mínima para Baratz)")
    print(f"[*] Rigetti Market Value : $4.8B")
    print(f"[*] Infleqtion Market Val: $1.2B")
    print("-" * 66)
    print(f"[OK] Historial de infraestructura cerrado y respaldado en:\n -> {os.path.abspath(archivo_target)}")
    print("==================================================================")

if __name__ == '__main__':
    registrar_market_caps()
