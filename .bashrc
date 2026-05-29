# === M82 MASTER TERMINAL INITIALIZATION ===
clear
echo -e "\033[0;32m🦅 ARCO DE INFRAESTRUCTURA UNIFICADA M82 ACTIVO\033[0m"

# 1. Enrutamiento automático al directorio de trabajo activo
if [ -d ~/pplx-kernels ]; then
    cd ~/pplx-kernels
elif [ -d ~/M82-Command ]; then
    cd ~/M82-Command
fi

# 2. Inicialización del motor con última base de datos guardada
if [ -f ./m82_robust_platform.py ]; then
    python3 m82_robust_platform.py
else
    echo -e "\033[0;31m⚠ ALERTA: Componentes fuera de ruta. Ejecute './m82_deploy_master.sh'\033[0m"
fi
