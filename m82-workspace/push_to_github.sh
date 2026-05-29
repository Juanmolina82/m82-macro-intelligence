#!/bin/bash
# CONFIGURACIÓN SEGURA DE GITHUB VIA M82 WORKSPACE
GITHUB_USER="MolinaHoldings"
GITHUB_REPO="m82-workspace-core"
GITHUB_TOKEN="TU_PERSONAL_ACCESS_TOKEN_AQUÍ"

echo "=== [M82 WORKSPACE] Sincronizando la Doctrina Edge-Island en la nube de forma forzada ==="
cd m82-workspace
git init
git config --local user.name "$GITHUB_USER"
git add .
git commit -m "Feat: Core integration of Edge-Island Strategy for unencumbered mobile nodes"
git branch -M main
git remote remove origin 2>/dev/null
git remote add origin https://$GITHUB_USER:$GITHUB_TOKEN@github.com/$GITHUB_USER/$GITHUB_REPO.git
git push -u origin main --force
echo "=== [M82 WORKSPACE] Sincronización completada. Repositorio actualizado con éxito. ==="
