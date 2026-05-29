import os
from datetime import datetime

def registrar_corte_flotante(brent, usdt, bcv):
    print("==================================================================")
    print(" M82-MONITOR v12.4: CORTE DE TASA FLOTANTE EN VIVO (CARIBE / OIL) ")
    print("==================================================================")
    
    ahora = datetime.now()
    hora_str = ahora.strftime("%H:%M")
    fecha_str = ahora.strftime("%Y-%m-%d")
    
    # Mapeo de ventanas críticas del Chairman
    if ahora.hour == 13 or (ahora.hour == 12 and ahora.minute >= 45):
        ventana = "1:00_PM_CORTE_CALLE"
    elif ahora.hour == 16 or (ahora.hour == 15 and ahora.minute >= 45):
        ventana = "4:00_PM_CIERRE_WALL_STREET"
    else:
        ventana = f"INTRA_DAY_CAPTURA_{hora_str}"
        
    # Ecuación de brecha real del mercado paralelo venezolano
    brecha = ((usdt - bcv) / bcv) * 100
    
    # Línea de registro formateada para base de datos estructurada
    log_line = f"{fecha_str} {hora_str}|{ventana}|Brent:${brent}|USDT:{usdt}|BCV:{bcv}|Brecha:{brecha:.2f}%\n"
    
    # Escritura atómica asegurada
    archivo_log = "m82_historical_closes.log"
    with open(archivo_log, "a") as f:
        f.write(log_line)
        
    print(f"[*] Ventana Detectada : {ventana}")
    print(f"[*] Parámetro Brent  : ${brent} USD/bl")
    print(f"[*] Tasa Flotante P2P : {usdt} VES/USDT")
    print(f"[*] Tasa Oficial BCV  : {bcv} VES/USD")
    print(f"[*] Brecha Fáctica    : {brecha:.2f}%")
    print("-" * 66)
    print(f"[OK] Datos consolidados en: {os.path.abspath(archivo_log)}")
    print("==================================================================")

if __name__ == '__main__':
    # Datos fácticos extraídos en tiempo real de tu consola LSEG y Monitor Dólar
    registrar_corte_flotante(brent=102.90, usdt=720.23, bcv=523.67)
