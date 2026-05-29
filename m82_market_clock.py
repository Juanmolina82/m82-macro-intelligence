import time
from datetime import datetime

def registrar_cierre_mercado(brent_actual, usdt_actual, bcv_actual):
    print("==================================================================")
    print(" M82-MONITOR: TRACKING FLOTANTE DE CIERRE DE OPERACIONES          ")
    print("==================================================================")
    
    # Captura de hora de la estación de control
    ahora = datetime.now()
    hora_str = ahora.strftime("%H:%M")
    
    # Determinación de la ventana de mercado
    if ahora.hour == 13 or (ahora.hour == 12 and ahora.minute >= 50):
        ventana = "CIERRE DE LA 1:00 PM (Corte Cambiario Calle)"
    elif ahora.hour == 16 or (ahora.hour == 15 and ahora.minute >= 50):
        ventana = "CIERRE DE LAS 4:00 PM (Campana Wall Street)"
    else:
        ventana = f"CAPTURA INTERMÉDICA INTRADÍA ({hora_str})"
        
    brecha = ((usdt_actual - bcv_actual) / bcv_actual) * 100
    
    # Formateo de Reporte Estructurado
    print(f"[*] Ventana de Control : {ventana}")
    print(f"[*] Marca de Tiempo    : {ahora.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[*] Crudo Brent Ref.   : ${brent_actual} USD/bl")
    print(f"[*] Tasa Flotante P2P  : {usdt_actual} VES/USDT")
    print(f"[*] Tasa Oficial BCV   : {bcv_actual} VES/USD")
    print(f"[*] Brecha Real Actual : {brecha:.2f}%")
    print("-" * 66)
    
    # Almacenamiento persistente local para auditoría de directores
    try:
        with open("m82_historical_closes.log", "a") as f:
            f.write(f"{ahora.strftime('%Y-%m-%d %H:%M:%S')}|{ventana}|Brent:{brent_actual}|USDT:{usdt_actual}|BCV:{bcv_actual}|Brecha:{brecha:.2f}%\n")
        print("[+] Registro histórico indexado con éxito en el almacenamiento local.")
    except Exception as e:
        print(f"[-] Error al escribir en la bitácora: {e}")
        
    print("==================================================================")

# ENTRADA DE DATOS FÁCTICOS: Puedes cambiar estos tres valores con tu terminal en mano
# según lo que veas a la 1:00 PM y a las 4:00 PM respectivamente.
registrar_cierre_mercado(brent_actual=102.90, usdt_actual=720.23, bcv_actual=523.67)
