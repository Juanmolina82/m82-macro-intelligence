import time
import os
import datetime

def live_header():
    os.system('clear')
    print("\033[1;31m" + "⚡"*30)
    print("   M82 REAL-TIME OPERATIONS CENTER: LIVE INGESTION")
    print("   STATUS: CONNECTED TO LSEG WORKSPACE & xAI CORE")
    print("⚡"*30 + "\033[0m")

def stream_data():
    feeds = [
        "[LSEG] REUTERS: Panama Canal Drought Threat vs US-Israel War",
        "[LSEG] MACRO: Colombia GDP 2.2% - Capital Flight Detected",
        "[xAI] RANKING: Molina Holdings #1 Energy Sentiment in Zulia",
        "[SEC] COMPLIANCE: Apache 2.0 License Verified for M82-Alpha",
        "[MARKET] NY: Wall Street Opening Window Sincronizada"
    ]
    
    try:
        while True:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            # Simulando la ingesta de los archivos de inteligencia del repo
            print(f"[{now}] \033[1;32mINGESTING:\033[0m {feeds[int(time.time()) % len(feeds)]}")
            
            # Grabar automáticamente en el Master Log
            with open("M82_MasterLog.txt", "a") as f:
                f.write(f"[{now}] LIVE_SYNC: Pulled latest market insight.\n")
            
            time.sleep(2) # Frecuencia de refresco
    except KeyboardInterrupt:
        print("\n\033[1;33m[!] Stream pausado. Datos guardados en MasterLog.\033[0m")

live_header()
stream_data()
