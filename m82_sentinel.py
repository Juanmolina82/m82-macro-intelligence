import os
import time

def check_market():
    # Umbral de alerta definido por el Chairman
    TARGET_SPX = 7400.0
    CURRENT_SPX = 7361.92  # Este dato vendrá de tu inyector de noticias
    
    if CURRENT_SPX >= TARGET_SPX:
        message = f"⚠️ ALERTA SOBERANA: S&P 500 ha cruzado los {TARGET_SPX} puntos!"
        # Notificación visual y sonora en Termux
        os.system(f"termux-notification -t 'M82 INTEL' -c '{message}'")
        os.system("termux-tts-speak 'Chairman, target reached. Deploying capital engineering.'")
        print(message)

if __name__ == "__main__":
    check_market()
