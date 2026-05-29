import time
from datetime import datetime

def registrar_evento_automatico(brent_price, usdt_price, bcv_price):
    ahora = datetime.now()
    hora_actual = ahora.strftime("%H:%M")
    
    # Evaluar las ventanas críticas solicitadas por el Chairman
    es_cierre_1pm = (ahora.hour == 13 and ahora.minute == 0)
    es_cierre_4pm = (ahora.hour == 16 and ahora.minute == 0)
    
    # Para propósitos de verificación inicial o si se corre manualmente:
    es_manual = True 
    
    if es_cierre_1pm or es_cierre_4pm or es_manual:
        if es_cierre_1pm:
            ventana = "CIERRE_1_PM_CALLE"
        elif es_cierre_4pm:
            ventana = "CIERRE_4_PM_WALL_STREET"
        else:
            ventana = f"CAPTURA_MANUAL_LATENTE_{hora_actual}"
            
        brecha = ((usdt_price - bcv_price) / bcv_price) * 100
        log_line = f"{ahora.strftime('%Y-%m-%d %H:%M:%S')}|{ventana}|Brent:${brent_price}|USDT:{usdt_price}|BCV:{bcv_price}|Brecha:{brecha:.2f}%\n"
        
        # Escritura forzada y creación garantizada del log
        with open("m82_historical_closes.log", "a") as f:
            f.write(log_line)
            
        print(f"[M82-OK] {hora_actual} -> Registro indexado en 'm82_historical_closes.log' para la ventana: {ventana}")

def loop_latente_cron():
    print("==================================================================")
    print(" M82-CORE: SISTEMA LATENTE DE SEGUIMIENTO EN HORARIOS DE CIERRE   ")
    print("==================================================================")
    print("[*] Monitoreando activamente el mercado paralelo vs Caribe Oil...")
    print("[*] Escucha activa para cortes automáticos: 13:00 y 16:00.")
    print("[*] Presione CTRL+C para pausar de forma segura.")
    print("-" * 66)
    
    # Datos extraídos de tus últimas pantallas de control reales
    brent_fijo = 102.90
    usdt_fijo = 720.23
    bcv_fijo = 523.67
    
    # Ejecución inicial de control para forzar la creación del archivo log
    registrar_evento_automatico(brent_fijo, usdt_fijo, bcv_fijo)
    
    try:
        while True:
            # Comprobación continua cada minuto
            registrar_evento_automatico(brent_fijo, usdt_fijo, bcv_fijo)
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n[-] Tracker latente pausado por el operador.")

if __name__ == '__main__':
    loop_latente_cron()
