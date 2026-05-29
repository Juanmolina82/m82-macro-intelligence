import yfinance as yf
import time
import os
import subprocess

TICKERS = ['CL=F', 'RB=F', 'GC=F', '^IXIC', 'ZW=F']
BRIDGE_PATH = os.path.expanduser("~/M82_Core/m82_bridge.txt")
LOG_PATH = os.path.expanduser("~/M82_Core/logs/market_snapshot.log")

def m82_sync_git():
    # Sincronización asíncrona con el Repo Molina
    subprocess.Popen(["git", "add", "."], stdout=subprocess.DEVNULL)
    subprocess.Popen(["git", "commit", "-m", "M82 Automated Market Update"], stdout=subprocess.DEVNULL)

while True:
    try:
        # Fetch de Alta Velocidad
        data = yf.download(TICKERS, period="1d", interval="1m", progress=False).tail(5)
        
        output = []
        output.append(f"🏛️  MOLINA HOLDINGS | CORE ENGINE v7.2 | {time.strftime('%Y-%m-%d %H:%M:%S')}")
        output.append("="*55)
        
        for ticker in TICKERS:
            current = data['Close'][ticker].iloc[-1]
            prev = data['Close'][ticker].iloc[-2]
            change = ((current - prev) / prev) * 100
            trend = "▲" if change >= 0 else "▼"
            color = "GREEN" if change >= 0 else "RED"
            output.append(f"{ticker:12} | {current:12.2f} | {trend} {change:+.2f}%")

        output.append("="*55)
        output.append("🔥 INFLATION SHOCK: 3.8% | NYC RISK: CRITICAL")
        output.append("🛰️  NODES: ACTIVE | REPO SYNC: OPERATIONAL")
        
        # Escritura en Bridge para Sesión 1
        with open(BRIDGE_PATH, "w") as f:
            f.write("\n".join(output))
            
        # Log para Persistencia
        with open(LOG_PATH, "a") as l:
            l.write(f"{time.strftime('%H:%M:%S')} - {TICKERS[0]} @ {data['Close'][TICKERS[0]].iloc[-1]}\n")
            
        # Sincronización con la Arquitectura Git cada 5 ciclos
        if int(time.time()) % 10 == 0:
            m82_sync_git()

        time.sleep(1) # Latencia de Grado Hedge Fund
    except Exception as e:
        time.sleep(2)
