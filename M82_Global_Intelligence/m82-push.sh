#!/bin/bash
cd ~/M82_Global_Intelligence
git add .
git commit -m "M1982 AGI: Global Equities Sync $(date +'%Y-%m-%d %H:%M')"
git push origin main
echo "🏛️ Búnker GitHub Sincronizado Exitosamente."
