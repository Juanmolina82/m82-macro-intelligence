import requests, time, threading
from openrouter_engine import ask_m82_oracle

TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
CHAT_ID = "1020305418"

def send_m82(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"🏛️ *M82 CORE*\n{text}", "parse_mode": "Markdown"}
    try: requests.post(url, json=payload, timeout=10)
    except: pass

def listener():
    last_id = 0
    while True:
        try:
            url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={last_id + 1}&timeout=30"
            res = requests.get(url, timeout=35).json()
            for update in res.get("result", []):
                last_id = update["update_id"]
                if "message" in update and "text" in update["message"]:
                    msg = update["message"]["text"]
                    if msg.startswith("/oracle "):
                        query = msg.replace("/oracle ", "")
                        send_m82("🔮 *Consultando al Oráculo...*")
                        send_m82(f"📜 *RESPUESTA:* \n\n{ask_m82_oracle(query)}")
        except: pass
        time.sleep(1)

if __name__ == "__main__":
    send_m82("🛡️ *NÚCLEO M82 ONLINE*\nEscucha activa y reportes sincronizados.")
    # Inicia la escucha en un hilo separado
    threading.Thread(target=listener, daemon=True).start()
    
    # Bucle principal para reportes automáticos (Whale Tracker)
    while True:
        # Aquí puedes poner la lógica de envío automático de ballenas cada 30 min
        time.sleep(1800) 
