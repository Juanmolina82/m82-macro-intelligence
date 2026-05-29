import yfinance as yf
import datetime

# UNIDADES ESTRATÉGICAS (Ejemplos para la arquitectura de valoración)
# Estos valores se ajustan según la escalabilidad de la firma
portfolio_units = {
    "MU": 1000000,    # Unidades teóricas/reales de Micron
    "NVDA": 500000,   # Unidades de NVIDIA
    "GC=F": 10000,    # Contratos/Onzas de Oro
    "NQ=F": 100       # Contratos de Nasdaq
}

def calculate_nav():
    print(f"--- MOLINA HOLDINGS LLC | NET ASSET VALUE (NAV) | {datetime.date.today()} ---")
    total_value = 0
    
    for ticker, units in portfolio_units.items():
        try:
            asset = yf.Ticker(ticker)
            price = asset.history(period="1d")['Close'].iloc[-1]
            asset_value = price * units
            total_value += asset_value
            print(f"[*] {ticker:<5}: Price ${price:>8.2f} | Holding: {units:>10} | Value: ${asset_value:,.2f}")
        except:
            print(f"[!] Error consultando {ticker}")
            
    print("-" * 70)
    print(f"VALOR TOTAL DEL PATRIMONIO (NAV): ${total_value:,.2f}")
    print("-" * 70)

if __name__ == "__main__":
    calculate_nav()
