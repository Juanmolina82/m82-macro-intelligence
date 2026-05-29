#!/bin/bash
# M82 WORKSPACE | MASTER MONITOR (S1) - V5 ROBUST
ROOT_DIR="$HOME/M82_Core"
BRIDGE="$ROOT_DIR/m82_bridge.txt"
COPYRIGHT="© 2026 MOLINA HOLDINGS LLC & MOLINA GLOBAL LLC"

sync_m82() {
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    cd $ROOT_DIR
    git add .
    git commit -m "M82 Sovereign Sync: $TIMESTAMP | $COPYRIGHT" --quiet
    git push origin main --quiet
}

while true; do
    clear
    echo -e "\e[1;31m🏛️  M82 WORKSPACE | MASTER MONITOR (S1) | $(date +%H:%M:%S)\e[0m"
    echo -e "\e[1;37m--------------------------------------------------------\e[0m"
    
    # Datos de Mercado de Python
    if ls $ROOT_DIR/obs_sources/m82_*.txt 1> /dev/null 2>&1; then
        echo -e "\e[1;33m📊 M82 MARKET FLOWS (Real-Time):\e[0m"
        cat $ROOT_DIR/obs_sources/m82_*.txt | sed 's/^/   /'
    fi

    echo -e "\e[1;37m--------------------------------------------------------\e[0m"
    
    # Inteligencia Inyectada desde S2
    echo -e "\e[1;32m📥 M82 BRIDGE INTEL (Session 2):\e[0m"
    if [ -s "$BRIDGE" ]; then
        tail -n 10 "$BRIDGE" | sed 's/^/   /'
    fi
    
    echo -e "\e[1;37m--------------------------------------------------------\e[0m"
    echo -e "\e[1;30m   $COPYRIGHT\e[0m"

    sync_m82
    sleep 60
done
