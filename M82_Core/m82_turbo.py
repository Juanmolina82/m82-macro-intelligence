import yfinance as yf
import time
import os

# Configuración de Tickers de Alta Intensidad
TICKERS = ["^IXIC", "ZW=F", "CL=F", "GC=F", "EURUSD=X"]
BRIDGE_PATH = os.path.expanduser("~/M82_Core/m82_bridge.txt")

print("🏛️ MOLINA GLOBAL | TURBO ENGINE STARTING...")

while True:
    try:
        # Descarga rápida del último tick
        data = yf.download(TICKERS, period="1d", interval="1m", progress=False).tail(2)
        
        with open(BRIDGE_PATH, "w") as f:
            f.write(f"🏛️ MOLINA GLOBAL | LIVE FEED | {time.strftime('%H:%M:%S')}\n")
            f.write("--------------------------------------------------\n")
            for ticker in TICKERS:
                last_price = data['Close'][ticker].iloc[-1]
                prev_price = data['Close'][ticker].iloc[-2]
                change = ((last_price - prev_price) / prev_price) * 100
                symbol = "▲" if change >= 0 else "▼"
                f.write(f"{ticker:10} | {last_price:10.2f} | {symbol} {change:+.2f}%\n")
            f.write("--------------------------------------------------\n")
            f.write("🔥 CPI SHOCK: 3.8% | TARGET: NYC JURISDICTIONAL RISK\n")
            f.write("🛰️ STATUS: ULTRA-LOW LATENCY SYNC ACTIVE\n")
            
        # Latencia reducida a 2 segundos para no banear la IP pero mantener flujo constante
        time.sleep(2)
    except Exception as e:
        time.sleep(1)
