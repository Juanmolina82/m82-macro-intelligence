import yfinance as yf
import time
import os

TICKERS = ["^IXIC", "CL=F", "GC=F", "MU", "AVGO"]
BRIDGE_PATH = os.path.expanduser("~/M82_Core/m82_bridge.txt")

while True:
    try:
        data = yf.download(TICKERS, period="1d", interval="1m", progress=False).tail(1)
        with open(BRIDGE_PATH, "w") as f:
            f.write(f"🏛️  MOLINA GLOBAL | WAR ROOM | {time.strftime('%H:%M:%S')}\n")
            f.write("--------------------------------------------------\n")
            f.write(f"🔥 FED ALERT: Goolsbee 'Disappointed' - CPI 3.8%\n")
            f.write(f"⚠️ SERVICIOS AL ALZA: Inflación Estructural Detectada\n")
            f.write("--------------------------------------------------\n")
            for t in TICKERS:
                price = data['Close'][t].iloc[-1]
                f.write(f"{t:<10} | {price:>10.2f}\n")
            f.write("--------------------------------------------------\n")
            f.write("🛰️  ESTADO: TELEFONO OPTIMIZADO (3s REFRESH)\n")
        time.sleep(3) # Refresco más lento para no calentar el móvil
    except:
        time.sleep(5)
