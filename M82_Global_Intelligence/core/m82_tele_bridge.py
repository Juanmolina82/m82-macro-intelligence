import requests

# Datos limpios y directos
TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
CHAT_ID = "1020305418"

def send_m82_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"🏛️ **M1982 PULSE**\n{message}",
        "parse_mode": "Markdown"
    }
    try:
        # Timeout corto para que no se quede pegado si no hay internet
        requests.post(url, json=payload, timeout=5)
    except:
        pass
