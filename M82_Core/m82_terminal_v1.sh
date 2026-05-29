#!/bin/bash
# M82 WORKSPACE | MASTER MONITOR (S1) | SILENT MODE
ROOT_DIR="$HOME/M82_Core"
BRIDGE="$ROOT_DIR/m82_bridge.txt"
COPYRIGHT="© 2026 MOLINA HOLDINGS LLC & MOLINA GLOBAL LLC"

while true; do
    clear
    echo -e "\e[1;31m🏛️  M82 WORKSPACE | MASTER MONITOR (S1) | $(date +%H:%M:%S)\e[0m"
    echo -e "\e[1;37m--------------------------------------------------------\e[0m"
    
    # 1. Mostrar flujos de Mercado (Desde el motor de Python)
    if ls $ROOT_DIR/obs_sources/m82_*.txt 1> /dev/null 2>&1; then
        echo -e "\e[1;33m📊 M82 REAL-TIME FLOWS:\e[0m"
        cat $ROOT_DIR/obs_sources/m82_*.txt | sed 's/^/   /'
    else
        echo -e "\e[1;30m   Esperando inyección de datos de mercado...\e[0m"
    fi

    echo -e "\e[1;37m--------------------------------------------------------\e[0m"
    
    # 2. Mostrar Información de Sesión 2 (Bridge)
    echo -e "\e[1;32m📥 INTELIGENCIA RECIBIDA (M82 BRIDGE):\e[0m"
    if [ -s "$BRIDGE" ]; then
        # Muestra las últimas 10 líneas de información cruzada
        tail -n 10 "$BRIDGE" | sed 's/^/   /'
    else
        echo -e "\e[1;30m   Canal despejado. Listo para recibir data masiva...\e[0m"
    fi
    
    echo -e "\e[1;37m--------------------------------------------------------\e[0m"
    echo -e "\e[1;30m   $COPYRIGHT\e[0m"

    # 3. Resguardo automático a GitHub (Silencioso)
    if [ -d "$ROOT_DIR/.git" ]; then
        cd $ROOT_DIR
        git add . && git commit -m "M82 Workspace Update $(date +%H:%M)" --quiet && git push origin main --quiet
    fi
    
    sleep 60
done
