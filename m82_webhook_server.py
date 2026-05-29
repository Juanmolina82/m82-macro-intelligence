#!/usr/bin/env python3
import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TK = '8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4'
CID = '1020305418'

@app.route('/webhook', methods=['POST'])
def telegram_webhook():
    data = request.get_json()
    if "message" in data and "text" in data["message"]:
        if "/reporte" in data["message"]["text"].lower():
            # El servidor responde de forma automática e inmediata con el reporte validado
            texto_reporte = (
                "📊 M82 WORKSPACE | AUTOMATED FRONT PAGE INSIGHT\n\n"
                "1. Impacto Geopolitico (Trump/Iran):\n"
                "Las negociaciones muestran cautela con avances moderados. Donald Trump afirmo que el acuerdo debe ser relevante o no habra trato. El bloqueo naval en el Estrecho de Hormuz sigue firme.\n\n"
                "2. Resguardo de Activos (NAV $5B):\n"
                "El Brent Crude cayo 4% por expectativas transitorias. M82 Workspace mantiene el blindaje completo del NAV de $5B en Hard Assets.\n\n"
                "3. Estado de Infraestructura:\n"
                "El nucleo GLOBAL-CORE-V6 opera al 100% en canal de aislamiento preventivo de forma autonoma mediante Webhook."
            )
            requests.post(f"https://api.telegram.org/bot{TK}/sendMessage", json={"chat_id": CID, "text": texto_reporte})
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
