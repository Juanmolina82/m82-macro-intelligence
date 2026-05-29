from datetime import datetime

def inyectar_datos_cloud(ticker, base_multiplier, brent_price, usdt_rate):
    ahora = datetime.now()
    fecha_hora = ahora.strftime("%Y-%m-%d %H:%M")
    
    # Ecuación de correlación: Multiplicador premium cloud frente al costo de energía del Caribe
    risk_index = (base_multiplier * brent_price) / 100
    
    log_line = f"{fecha_hora}|DATA_CLOUD_UPDATE|Ticker:{ticker}|PremiumRatio:{base_multiplier}X|BrentRef:${brent_price}|RiskIndex:{risk_index:.2f}|CalleUSDT:{usdt_rate}\n"
    
    with open("m82_historical_closes.log", "a") as f:
        f.write(log_line)
        
    print("==================================================================")
    print(" M82-DATA-CLOUD: INDEXACIÓN DE METADATOS COMPLETA                ")
    print("==================================================================")
    print(f"[*] Ticker Evaluado  : {ticker}")
    print(f"[*] Ratio de Prima   : {base_multiplier}X (Zacks Hold #3)")
    print(f"[*] Coeficiente Riesgo: {risk_index:.2f}")
    print(f"[OK] Módulo inyectado en la bitácora latente de la firma.")
    print("==================================================================")

if __name__ == '__main__':
    # Datos actualizados del cable de LSEG Workspace y Monitor Dólar (2:12 PM)
    inyectar_datos_cloud(ticker="SNOW", base_multiplier=9.14, brent_price=102.90, usdt_rate=720.23)
