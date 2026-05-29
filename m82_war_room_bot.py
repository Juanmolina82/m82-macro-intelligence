#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from datetime import datetime
import telebot

# 📜 LICENCIA: Apache 2.0 | Molina Holdings LLC
# 🛰️ COMANDO: M82 War Room | CPI: 3.8% (Target Max)
# 🛡️ UMBRAL CRÍTICO: US10Y @ 4.5% (Línea Roja de Equity)

# IMPORTANTE:
# NO pongas el token en duro en el código.
# Antes de ejecutar, en Termux haz:
#   export M82_TELEGRAM_TOKEN="TU_TOKEN_NUEVO_DE_BOTFATHER"
TOKEN = os.getenv("M82_TELEGRAM_TOKEN")

if not TOKEN:
    raise RuntimeError("M82_TELEGRAM_TOKEN no está definido en el entorno.")

# parse_mode="Markdown" permite usar *negritas* y _cursivas_
bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

# ---------------------------------------------------------------------
# /start y /status -> Estado del Monolith
# ---------------------------------------------------------------------
@bot.message_handler(commands=['start', 'status'])
def send_status(message):
    status_msg = (
        "🏛️ *M82 MONOLITH ACTIVE*
"
        "--------------------------
"
        "📈 *CPI Abril:* 3.8% (HOT!)
"
        "🦅 *US10Y Yield:* 4.44% (cerca del 4.5% línea roja)
"
        "🧱 *Foco táctico:* Cobre e insumos de IA
"
        f"📅 *Hora local:* {datetime.now().strftime('%H:%M:%S')}"
    )
    bot.reply_to(message, status_msg)

# ---------------------------------------------------------------------
# /market_view -> Placeholder para conectar con M82 Markets
# ---------------------------------------------------------------------
@bot.message_handler(commands=['market_view'])
def market_view(message):
    reply = (
        "📊 *M82 Market View (beta)*
"
        "- Próximo paso: conectar este comando con los módulos de mercado:
"
        "  `m82_realtime_markets.py`, `m82_quantum_edge.py`, etc.
"
    )
    bot.reply_to(message, reply)

# ---------------------------------------------------------------------
# Fallback: cualquier otro texto
# ---------------------------------------------------------------------
@bot.message_handler(func=lambda m: True)
def fallback(message):
    reply = (
        "🤖 Comandos disponibles:
"
        "/status - Estado del M82 Monolith
"
        "/market_view - Vista táctica de mercado (beta)
"
    )
    bot.reply_to(message, reply)

# ---------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------
def main():
    print("M82 War Room Bot iniciado. Esperando comandos...")
    bot.infinity_polling(timeout=60, long_polling_timeout=60)

if __name__ == "__main__":
    main()
