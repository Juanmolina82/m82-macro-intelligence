import yfinance as yf
import pandas as pd
import datetime

assets = ["MU", "NVDA", "NQ=F", "GC=F"]

def fetch_historical_audit():
    print("--- MOLINA HOLDINGS LLC | HISTORICAL DATA AUDIT ---")
    today = datetime.date.today()
    
    for asset in assets:
        print(f"[PROCESANDO] Extrayendo data histórica para: {asset}")
        ticker = yf.Ticker(asset)
        # Extraemos el último año de data diaria
        df = ticker.history(period="1y")
        
        # Guardamos en formato CSV para la posteridad
        filename = f"{asset.replace('=F', '')}_1Y_History.csv"
        df.to_csv(filename)
        print(f"[EXITO] Archivo generado: {filename}")
    
    print("-" * 50)

if __name__ == "__main__":
    fetch_historical_audit()
