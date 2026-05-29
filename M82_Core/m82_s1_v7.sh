#!/bin/bash
# M82 WORKSPACE | S1 ULTRA-LIGHT | ZERO LATENCY
ROOT_DIR="$HOME/M82_Core"
BRIDGE="$ROOT_DIR/m82_bridge.txt"
OBS_DIR="$ROOT_DIR/obs_sources"
COPYRIGHT="© 2026 MOLINA HOLDINGS LLC & MOLINA GLOBAL LLC"

# El respaldo ahora es un proceso independiente que no detiene el monitor
sync_bg() {
    (cd $ROOT_DIR && git add . && git commit -m "M82 Sync" --quiet && git push origin main --quiet) &
}

while true; do
    clear
    echo -e "\e[1;31m🏛️  M82 GLOBAL COMMAND CENTER | S1 | $(date +%H:%M:%S)\e[0m"
    echo -e "\e[1;37m--------------------------------------------------------\e[0m"
    
    # Visualización instantánea de noticias del Bridge
    if [ -s "$BRIDGE" ]; then
        echo -e "\e[1;32m📰 M82 LIVE INTELLIGENCE:\e[0m"
        tail -n 12 "$BRIDGE" | sed 's/^/   /'
    fi
    
    echo -e "\e[1;37m--------------------------------------------------------\e[0m"
    
    # Datos de Mercado (Si el archivo existe, lo muestra de golpe)
    [ -f "$OBS_DIR/m82_top_news.txt" ] && echo -e "   ⚡ FLASH: $(cat $OBS_DIR/m82_top_news.txt)"
    
    echo -e "\e[1;37m--------------------------------------------------------\e[0m"
    echo -e "\e[1;30m   $COPYRIGHT\e[0m"

    # Lanzar sincronización en background cada 5 ciclos para no saturar
    ((count++))
    if [ $count -eq 5 ]; then
        sync_bg
        count=0
    fi
    
    sleep 2
done
