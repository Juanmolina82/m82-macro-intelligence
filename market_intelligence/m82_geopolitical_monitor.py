import requests
import yfinance as yf
from pyfinviz.news import News

# --- M82 PROPRIETARY CONFIGURATION ---
TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
CHAT_ID = "7154211158"
# ---------------------------------------

def get_yfinance_data(symbol):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.fast_info
        price = info['last_price']
        prev_close = info['previous_close']
        change = ((price - prev_close) / prev_close) * 100
        return f"${price:,.2f} ({change:+.2f}%)"
    except: return "N/A"

def get_finviz_intel():
    try:
        news_client = News()
        headlines = news_client.news_df.head(5)['Headline'].tolist()
        return [f"• {h}" for h in headlines[:5]]
    except: return ["⚠️ News Feed: Standby."]

def send_intel(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})

if __name__ == "__main__":
    spy = get_yfinance_data("SPY")
    qqq = get_yfinance_data("QQQ")
    dia = get_yfinance_data("DIA")
    tlt = get_yfinance_data("TLT")
    
    try:
        t10y_raw = yf.Ticker("^TNX").fast_info['last_price']
        t10y = f"{t10y_raw:.2f}%"
    except: t10y = "N/A"

    news = get_finviz_intel()
    
    report = (
        "🏛️ **M82 ASSET MATRIX**\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "📈 **Equities & Indices (M82 Platform):**\n"
        f"  • SPY: {spy}\n"
        f"  • QQQ: {qqq}\n"
        f"  • DIA: {dia}\n\n"
        "🏦 **Fixed Income & Bonds:**\n"
        f"  • US 10Y Yield: {t10y}\n"
        f"  • TLT (Long Bond): {tlt}\n\n"
        "📊 **M82 Order Flow Analysis:**\n"
        "  • Status: Active (Patente de Licencia General)\n\n"
        "📰 **Market Pulse (Finviz):**\n"
        f"{'\n'.join(news)}\n\n"
        "⚡ *Molina Holdings: M82 Intellectual Property*"
    )
    send_intel(report)
