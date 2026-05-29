import os, time, yfinance as yf

TICKERS = ['STT', 'BLK', 'VXZ', 'CL=F', 'USO']

def run():
    while True:
        try:
            data = yf.download(TICKERS, period="1d", interval="1m", progress=False).tail(1)
            with open(os.path.expanduser("~/M82_Core/m82_bridge.txt"), "w") as f:
                f.write(f"🏛️  MOLINA GLOBAL | WAR ENGINE | {time.strftime('%T')}\n")
                f.write("="*50 + "\n")
                f.write("🇬🇧 FITCH UPGRADE: BARCLAYS/NATWEST/LLOYDS -> AA\n")
                f.write("💎 PRIVATE EQUITY: BLACKSTONE (BX) MOVE TO GREECE\n")
                f.write("🔥 PIPELINE: KMI/TENNESSEE RESTRICTED NYC/NJ\n")
                f.write("-" * 50 + "\n")
                for t in TICKERS:
                    price = data['Close'][t].iloc[-1]
                    f.write(f"{t:<10} | {price:>10.2f}\n")
                f.write("="*50 + "\n")
                f.write("🛡️  ESTADO: SINCRONIZACIÓN FORZADA OK\n")
            time.sleep(3)
        except Exception as e:
            time.sleep(5)

if __name__ == "__main__":
    run()
