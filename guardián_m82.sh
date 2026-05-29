#!/bin/bash
while true; do
  if ! pgrep -f core_v6.py > /dev/null; then
    echo "$(date): El Core V6 se detuvo. Reiniciando..." >> ~/m82_guardián.log
    cd ~/MOLINA-GLOBAL-CORE-V6 && nohup python core_v6.py > core.log 2>&1 &
  fi
  sleep 60
done
