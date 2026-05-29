#!/bin/bash
ROOT_DIR="$HOME/M82_Core"
BRIDGE="$ROOT_DIR/m82_bridge.txt"

while true; do
    # Consultar datos con un fallback para evitar el 'nan'
    python3 - << 'PYTHON' > "$ROOT_DIR/rt_tmp.txt"
import yfinance as yf
import numpy as np

tickers = {"^IXIC": "NASDAQ", "ZW=F": "WHEAT", "CL=F": "CRUDE"}
try:
    data = yf.download(list(tickers.keys()), period="2d", interval="1m", progress=False)
    for t in tickers:
        val = data['Close'][t].iloc[-1]
        prev = data['Close'][t].iloc[-2]
        if np.isnan(val): val = prev # Fallback al valor anterior si es NaN
        change = ((val - prev) / prev) * 100
        color = "\033[1;32m" if change >= 0 else "\033[1;31m"
        print(f"{tickers[t]}: {val:.2f} ({color}{change:+.2f}%\033[0m)")
except:
    print("Sincronizando con LSEG/Yahoo...")
PYTHON

    # Mostrar en S2 y empujar a S1
    clear
    echo -e "\e[1;35m🏛️  MOLINA GLOBAL | RT SENTINEL | S2\e[0m"
    echo "------------------------------------------------"
    cat "$ROOT_DIR/rt_tmp.txt"
    echo "------------------------------------------------"
    echo -e "\e[1;33m🔥 CPI: 3.8% | JURISDICTIONAL RISK: HIGH\e[0m"
    
    # Force Push a la Sesión 1
    cp "$ROOT_DIR/rt_tmp.txt" "$BRIDGE"
    echo -e "\n🔥 LATEST CPI: 3.8%" >> "$BRIDGE"
    
    sleep 10
done
