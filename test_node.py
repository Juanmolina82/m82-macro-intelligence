import urllib.request
import json

url = "http://127.0.0.1:8502/api/v12/m82/status"

try:
    print("\n" + "="*50)
    print(" INTERROGANDO NODO SOBERANO PUERTO 8502 ")
    print("="*50)
    
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        
        print(f"[*] Estatus General : {data['status']}")
        print(f"[*] Identificador   : {data['node']}")
        print(f"[*] Vectores Activos: {', '.join(data['surveillance_vectors'])}")
        print(f"[*] Marco Político  : {data['geopolitical_framework']}")
        print("="*50 + "\n")
        
except Exception as e:
    print(f"[-] Error de conexión en el puerto seguro: {e}")
