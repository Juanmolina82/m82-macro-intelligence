#!/bin/bash
ROOT_DIR="$HOME/M82_Core"
BRIDGE="$ROOT_DIR/m82_bridge.txt"
OBS_DIR="$ROOT_DIR/obs_sources"
COPYRIGHT="© 2026 MOLINA HOLDINGS LLC & MOLINA GLOBAL LLC"

sync_m82_github() {
    cd $ROOT_DIR
    git add .
    git commit -m "M82 Secure Snapshot: $(date +'%H:%M') | $COPYRIGHT" --quiet
    git push origin main --quiet
}

while true; do
    clear
    echo -e "\e[1;31m🏛️  M82 GLOBAL COMMAND CENTER | S1 | $(date +%H:%M:%S)\e[0m"
    echo -e "\e[1;37m--------------------------------------------------------\e[0m"
    echo -e "\e[1;33m📊 MERCADOS (LSEG/Bloomberg Feed):\e[0m"
    if ls $OBS_DIR/m82_*.txt 1> /dev/null 2>&1; then
        cat $OBS_DIR/m82_*.txt | grep -v "TOP NEWS" | sed 's/^/   /'
    fi
    echo -e "\e[1;37m--------------------------------------------------------\e[0m"
    echo -e "\e[1;32m📰 M82 TOP NEWS & BRIDGE INTEL (S2):\e[0m"
    [ -f "$OBS_DIR/m82_top_news.txt" ] && echo -e "   ⚡ $(cat $OBS_DIR/m82_top_news.txt)"
    [ -s "$BRIDGE" ] && tail -n 6 "$BRIDGE" | sed 's/^/   /'
    echo -e "\e[1;37m--------------------------------------------------------\e[0m"
    echo -e "\e[1;30m   $COPYRIGHT\e[0m"
    sync_m82_github
    sleep 60
done
