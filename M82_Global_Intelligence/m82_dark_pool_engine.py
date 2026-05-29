import yfinance as yf
import pandas as pd
import os
from datetime import datetime

def detect_dark_flow(ticker, category):
    try:
        data = yf.Ticker(ticker).history(period="5d", interval="1h")
        if data.empty: return
        
        # Calcular Volumen Típico vs Actual
        avg_vol = data['Volume'].mean()
        last_vol = data['Volume'].iloc[-1]
        
        # Ratio de Liquidez Oculta (Estimación M1982)
        # Un pico de volumen sin un movimiento proporcional de precio = Dark Pool Absorption
        price_change = abs(data['Close'].pct_change().iloc[-1])
        vol_spike = last_vol / avg_vol
        
        dark_score = "LOW"
        if vol_spike > 2.0 and price_change < 0.005:
            dark_score = "🚨 CRITICAL: DARK POOL ABSORPTION"
        elif vol_spike > 1.5:
            dark_score = "🟡 HIGH: INSTITUTIONAL POSITIONING"
            
        line = f"| {category: <12} | {ticker: <8} | Vol Spike: {vol_spike:>5.2f}x | {dark_score}"
        print(line)
        return line
    except:
        return None

def run_dark_pool_scan():
    print(f"\n🌑 M1982 DARK POOL SCAN | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("-" * 70)
    
    universe = {
        "EQUITIES": ["SMCI", "AMD", "JPM", "GS"],
        "ETFS": ["SPY", "QQQ", "VXX"],
        "COMMODITIES": ["GC=F", "CL=F", "ZS=F"],
        "CRYPTO": ["BTC-USD", "ETH-USD", "SOL-USD"]
    }
    
    full_report = "DARK POOL REPORT\n"
    for cat, tickers in universe.items():
        for t in tickers:
            res = detect_dark_flow(t, cat)
            if res: full_report += res + "\n"
            
    os.system("termux-tts-speak 'Dark pool scan complete. Institutional flows detected.'")

if __name__ == "__main__":
    run_dark_pool_scan()
