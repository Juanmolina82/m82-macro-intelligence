#!/bin/bash
# CONFIGURACIÓN SEGURA DE GITHUB VIA M82 WORKSPACE
GITHUB_USER="MolinaHoldings"
GITHUB_REPO="m82-workspace-core"
GITHUB_TOKEN="TU_PERSONAL_ACCESS_TOKEN_AQUÍ"

echo "=== [M82 WORKSPACE] Iniciando sincronización forzada hacia GitHub desde dispositivo móvil ==="
cd m82-workspace
git init
git config --local user.name "$GITHUB_USER"
git add .
git commit -m "Fix: Resolve mobile shell syntax error and establish clean architecture monolingual deploy"
git branch -M main
git remote remove origin 2>/dev/null
git remote add origin https://$GITHUB_USER:$GITHUB_TOKEN@github.com/$GITHUB_USER/$GITHUB_REPO.git
git push -u origin main --force
echo "=== [M82 WORKSPACE] Sincronización exitosa. Datos institucionales blindados en GitHub. ==="
