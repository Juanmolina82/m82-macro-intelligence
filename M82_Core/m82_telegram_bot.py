import os
import requests
import time

TOKEN = "TU_BOT_TOKEN" # Coloque su Token real aquí
CHAT_ID = "TU_CHAT_ID"

def send_alert(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"Error: {e}")

# Alerta de Inicio de Sistema
send_alert("🏛️ **MOLINA GLOBAL | M82 CORE ACTIVE**\nTriangulation established.\nMonitoring: CPI 3.8% | Hormuz Blockade.")

# Loop para vigilar el Bridge y despachar alertas críticas
last_content = ""
while True:
    if os.path.exists(os.path.expanduser("~/M82_Core/m82_bridge.txt")):
        with open(os.path.expanduser("~/M82_Core/m82_bridge.txt"), "r") as f:
            content = f.read()
            if "☢️" in content or "⚠️" in content:
                if content != last_content:
                    send_alert(f"🚨 **M82 CRITICAL ALERT**\n{content}")
                    last_content = content
    time.sleep(5)
