from datetime import datetime
import os

def indexar_fondos_federales(ticker, fondos, variacion, tasa_calle):
    ahora = datetime.now()
    fecha_hora = ahora.strftime("%Y-%m-%d %H:%M")
    
    # Registro formal en el log histórico M82
    log_line = f"{fecha_hora}|GOVT_EQUITY_DEAL|Ticker:{ticker}|Funds:${fondos}M|Gain:+{variacion}%|CalleUSDT:{tasa_calle}\n"
    
    archivo_log = "m82_historical_closes.log"
    with open(archivo_log, "a") as f:
        f.write(log_line)
        
    print("==================================================================")
    print(" M82-MONITOR v12.7: REGISTRO DE PARTICIPACIÓN PATRIMONIAL FED    ")
    print("==================================================================")
    print(f"[*] Entidad Registrada : {ticker}")
    print(f"[*] Inyección Federal  : ${fondos} Millones de USD (Equity)")
    print(f"[*] Cierre de Mercado  : +{variacion}%")
    print(f"[*] Tasa Flotante P2P  : {tasa_calle} VES/USDT")
    print("-" * 66)
    print(f"[OK] Evento indexado con éxito en:\n -> {os.path.abspath(archivo_log)}")
    print("==================================================================")

if __name__ == '__main__':
    # Datos oficiales fijados al cierre del cable (MarketWatch / LSEG)
    indexar_fondos_federales(ticker="IBM_ANDERON", fondos=1000, variacion=11.3, tasa_calle=720.23)
    indexar_fondos_federales(ticker="D-WAVE_QBTS", fondos=100, variacion=28.4, tasa_calle=720.23)
