import telebot
import yfinance as yf
import time
import sys

TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.reply_to(message, "🏛️ **MOLINA GLOBAL — COMMAND ONLINE**\n\nUse:\n/status - Reporte V3.2\n/price [TICKER] - Precio actual")

@bot.message_handler(commands=['status'])
def send_status(message):
    bot.reply_to(message, "🛰️ Generando reporte maestro para el Chairman...")
    # Aquí puedes invocar tu reporte principal
    bot.send_message(message.chat.id, "✅ Sistema Operativo V3.2")

@bot.message_handler(commands=['price'])
def get_price(message):
    try:
        ticker_name = message.text.split()[-1].upper()
        ticker = yf.Ticker(ticker_name)
        price = ticker.fast_info['last_price']
        bot.reply_to(message, f"📊 **M82 Data Feed:**\n{ticker_name}: ${price:,.2f}")
    except:
        bot.reply_to(message, "⚠️ Error en Ticker. Ejemplo: /price NVDA")

def run_bot():
    print("📡 MOLINA GLOBAL: Iniciando escucha protegida...")
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(f"⚠️ Conexión caída: {e}. Reiniciando en 5s...")
            time.sleep(5)

if __name__ == "__main__":
    run_bot()
