#!/bin/bash
echo "🚀 Iniciando M82 Global Intelligence Core..."
cd ~/M82_Global_Intelligence/core

# Ejecutar el motor principal (Ajusta el nombre del script si es necesario)
python3 brain_core.py

# Al cerrar el motor, sincronizar automáticamente
echo "🔄 Sincronizando resultados con el Búnker GitHub..."
m82-sync
