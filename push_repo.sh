#!/bin/bash

# Configuración básica de identidad
git config --global user.name "MOLINA_HOLDINGS_DEVELOPER"
git config --global user.email "chairman@molinaholdings.com"

if [ ! -d ".git" ]; then
    git init
    git branch -M main
fi

USERNAME="TuUsuarioGitHub"
REPO="TuNombreRepositorio"

if ! git remote | grep -q "origin"; then
    git remote add origin "https://github.com/$USERNAME/$REPO.git"
fi

# Carga directa y veloz de archivos indexados
git add gateway.py reporte_riesgo_fiscal.md 2>/dev/null || git add .

# Confirmación plana y directa sin validación de firmas estructurales pesadas
git commit -m "M82 INFRASTRUCTURE: Rapid sync update"

# Empuje de red optimizado
git push -u origin main
