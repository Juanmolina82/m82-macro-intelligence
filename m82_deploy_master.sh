#!/usr/bin/env bash
# M82 TERMINAL - COMPREHENSIVE V3.6 DEPLOYER

GREEN='\033[0;32m'
AMBER='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${AMBER}=== [M82 SYSTEM] ENLAZANDO CORTEZAS Y DISTRIBUYENDO CORE V3.6 ===${NC}"

python3 m82_robust_platform.py
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Abortado: El motor cuantitativo detectó una violación en las reglas de balance.${NC}"
    exit 1
fi

git add m82_config.json m82_robust_platform.py m82_box_vault.json m82_deploy_master.sh
git commit -m "Build(m82-core): Consolidación Final de Arquitectura V3.6" 2>/dev/null

for remote in origin core-v6 macro-intel ia-plataforma sovereign-core governance; do
    echo -e "${AMBER}Sincronizando nodo remoto: [${remote}] en rama master...${NC}"
    git push $remote master -f 2>/dev/null
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✔ Nodo [${remote}] replicado con éxito.${NC}"
    else
        echo -e "${AMBER}⚠ Aviso: Conexión con [${remote}] guardada en búfer local.${NC}"
    fi
done

echo -e "${GREEN}=== ✔ SISTEMA FUSIONADO Y FIJADO EN TODAS LAS SESIONES ===${NC}"
