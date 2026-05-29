import os
from datetime import datetime

def registrar_ajuste_brent():
    print("==================================================================")
    print(" M82-ENERGY v14.1: AJUSTE DE PRECIOS POR REBOTE GEOPOLÍTICO       ")
    print("==================================================================")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    archivo_target = "m82_cambiario_caribe.log"
    
    # Inyección de los precios de liquidación del cierre oficial de Reuters
    energy_data = (
        f"{timestamp}|ENERGY_CLOSE|Brent_Settlement:102.58|WTI_Settlement:96.35|"
        f"DXY_Index:99.13|Gold_Spot:4541.79|Hormuz_Risk:HIGH|Nvidia_NVDA:-1.80%\n"
    )
    
    with open(archivo_target, "a") as f:
        f.write(energy_data)
        
    print(f"[*] Pivot de Commodities Energéticos Indexado con Éxito.")
    print(f"[*] Barril Brent Oficial : $102.58 USD (Contracción de riesgo)")
    print(f"[*] Dólar Global (DXY)   : 99.13 Puntos")
    print(f"[*] Alerta de Monitoreo  : Negociaciones del Estrecho de Ormuz")
    print("-" * 66)
    print(f"[OK] Canal Cambiario/Energético recalibrado en:\n -> {os.path.abspath(archivo_target)}")
    print("==================================================================")

if __name__ == '__main__':
    registrar_ajuste_brent()
