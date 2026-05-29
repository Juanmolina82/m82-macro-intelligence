import yfinance as yf
import datetime
import os

tickers = {
    "MU": "Micron Technology",
    "NVDA": "NVIDIA Corp",
    "NQ=F": "Nasdaq 100 Futures",
    "GC=F": "Gold Futures (XAU)"
}

def get_market_data():
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H:%M')
    file_date = now.strftime('%Y%m%d_%H%M')
    
    report = [f"--- MOLINA HOLDINGS LLC | INTEL REPORT | {timestamp} ---",
              f"{'TICKER':<10} | {'PRECIO':<10} | {'CAMBIO %':<10} | {'NOMBRE'}",
              "-" * 60]
    
    for symbol, name in tickers.items():
        try:
            t = yf.Ticker(symbol)
            data = t.history(period="2d")
            if len(data) >= 2:
                current = data['Close'].iloc[-1]
                prev = data['Close'].iloc[-2]
                change = ((current - prev) / prev) * 100
                report.append(f"{symbol:<10} | ${current:<9.2f} | {change:>8.2f}% | {name}")
        except:
            report.append(f"{symbol:<10} | Error en Data")

    final_report = "\n".join(report)
    print(final_report)
    
    # Crear carpeta de logs si no existe
    log_dir = "../../logs/market_reports"
    os.makedirs(log_dir, exist_ok=True)
    
    # Guardar reporte
    with open(f"{log_dir}/intel_{file_date}.txt", "w") as f:
        f.write(final_report)
    print(f"\n[SISTEMA] Reporte guardado en: logs/market_reports/intel_{file_date}.txt")

if __name__ == "__main__":
    get_market_data()
