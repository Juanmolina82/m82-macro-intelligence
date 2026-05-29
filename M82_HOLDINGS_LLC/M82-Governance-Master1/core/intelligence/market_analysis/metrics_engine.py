import pandas as pd
import os

def run_analytics():
    print("--- MOLINA HOLDINGS LLC | ESTRATEGIA DE CORRELACIÓN Y CRECIMIENTO ---")
    path = "../historical_data/"
    assets = ["MU_1Y_History.csv", "NVDA_1Y_History.csv", "NQ_1Y_History.csv", "GC_1Y_History.csv"]
    
    data_frames = {}
    for asset in assets:
        name = asset.split('_')[0]
        if os.path.exists(path + asset):
            df = pd.read_csv(path + asset, index_col='Date', parse_dates=True)
            data_frames[name] = df['Close']
    
    # Unificamos data para correlación
    master_df = pd.DataFrame(data_frames).pct_change().dropna()
    
    print("\n[1] MATRIZ DE CORRELACIÓN (Resiliencia del Portafolio):")
    print(master_df.corr())
    
    print("\n[2] RENDIMIENTO MENSUAL PROMEDIO:")
    monthly_perf = master_df.resample('M').sum() * 100
    print(monthly_perf.tail(3)) # Mostramos los últimos 3 meses
    print("-" * 60)

if __name__ == "__main__":
    run_analytics()
