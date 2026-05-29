#!/bin/bash
echo "🛡️ M82 Sentinel Watchdog Activado..."
while true; do
    python m82_final_bot.py
    echo "🚨 Bot caído. Reiniciando en 3 segundos..."
    sleep 3
done
