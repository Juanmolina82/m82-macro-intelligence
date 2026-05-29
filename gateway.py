import websocket
import json
import ssl
import sys
import time

class AMPFuturesGateway:
    def __init__(self, api_url, token):
        self.api_url = api_url
        self.token = token
        self.ws = None
        self.is_connected = False

    def connect(self):
        print("\n[M82 CONSOLE] Inicializando conexion con la pasarela CQG/AMP...")
        websocket.enableTrace(False)
        self.ws = websocket.WebSocketApp(
            self.api_url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    def on_open(self, ws):
        self.is_connected = True
        print("[M82 CONSOLE] Autopista de red abierta. Autenticando credenciales...")
        auth_request = {
            "action": "authenticate",
            "token": self.token,
            "client_id": "M82_Sovereign_Console"
        }
        ws.send(json.dumps(auth_request))

    def subscribe_market_data(self, symbol):
        if not self.is_connected:
            print("[ALERTA] No se puede suscribir: Sin conexion activa.")
            return
        subscription_msg = {
            "action": "subscribe",
            "symbol": symbol,
            "levels": 1,
            "request_id": 82001
        }
        self.ws.send(json.dumps(subscription_msg))
        print(f"[M82 CONSOLE] Flujo de datos en tiempo real activado para: {symbol}")

    def execute_order(self, symbol, side, qty, price=None):
        if not self.is_connected:
            print("[ALERTA INTERNA] Orden rechazada: Terminal desconectada.")
            return
        order_msg = {
            "action": "place_order",
            "symbol": symbol,
            "side": side,
            "quantity": qty,
            "order_type": "MARKET" if price is None else "LIMIT",
            "account": "AMP_MOLINA_HOLDINGS_LIVE"
        }
        if price:
            order_msg["price"] = price
        self.ws.send(json.dumps(order_msg))
        print(f"[M82 CONSOLE] ORDEN TRANSMITIDA DIRECTO A CHICAGO -> {side} {qty} {symbol}")

    def on_message(self, ws, message):
        data = json.loads(message)
        if data.get("type") == "market_data":
            print(f"[TICK M82] {data['symbol']} | Precio Spot Futuros: {data['price']} | Vol: {data['volume']}")
        else:
            print(f"[RESPUESTA PASARELA] {data}")

    def on_error(self, ws, error):
        print(f"[ALERTA ERROR] Falla en la conexion de la API: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        self.is_connected = False
        print("[M82 CONSOLE] Conexion con el servidor de AMP finalizada.")

if __name__ == "__main__":
    API_ENDPOINT = "wss://demo-api.ampfutures.com/v1/cqg/connect"
    SECURITY_TOKEN = "M82_SECURE_TOKEN_ALPHA_NUMERIC_VALIDATION"
    
    print("\n==================================================")
    print("[M82 SYSTEM] Archivo 'gateway.py' compilado con exito.")
    print("==================================================")
