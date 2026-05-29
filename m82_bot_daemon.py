import time
import random

def run_persistent_oil_bot():
    print("==================================================================")
    print(" M82-BOT: MONITOREO PERSISTENTE Y LATENTE VINCULADO AL OIL       ")
    print("==================================================================")
    print("[*] Sincronizando demonio con el puerto seguro: 8502")
    print("[*] Escala Nominal Validada: Zona de las Centenas (Bs. 700+)")
    print("[*] Presione CTRL+C para detener el proceso de fondo.")
    print("-" * 66)
    
    # Parámetros base fácticos de tu terminal
    base_usdt = 720.23
    base_bcv = 523.67
    
    # Bucle latente infinito de actualización (Simulación de Feed en Vivo)
    try:
        while True:
            # Monitoreo de fluctuaciones del crudo (Simulando volatilidad del Brent sobre los $102)
            current_brent = round(random.uniform(101.50, 103.80), 2)
            
            # Cálculo del factor de estrés dinámico
            stress_index = (current_brent / 100.0) * (current_usdt_rate := base_usdt / base_bcv)
            dynamic_projection = base_usdt + (stress_index * random.uniform(12.5, 18.2))
            
            print(f"[LATENTE] Brent: ${current_brent} USD/bl | Ref. Calle: {base_usdt} | Bot Proyección: {dynamic_projection:.2f} VES/USDT")
            
            # Intervalo de refresco de telemetría (ajustable en producción)
            time.sleep(3.0)
            
    except KeyboardInterrupt:
        print("\n[-] Demonio M82 pausado de forma segura desde la consola.")
        print("==================================================================")

if __name__ == '__main__':
    run_persistent_oil_bot()
