import os

def inicializar_nodos_separados():
    print("==================================================================")
    print(" M82-SECURE: CONFIGURACIÓN DE NODOS DE DATOS COMPARTIMENTADOS     ")
    print("==================================================================")
    
    # Definición de archivos de registro específicos por canal
    canales = {
        "cambiario": "m82_cambiario_caribe.log",
        "infraestructura": "m82_quantum_energy.log",
        "corporativo": "m82_branding_pr.log"
    }
    
    for nombre, archivo in canales.items():
        if not os.path.exists(archivo):
            with open(archivo, "w") as f:
                f.write(f"--- INICIO DE CANAL SEPARADO: {nombre.upper()} ---\n")
            print(f"[+] Nodo inicializado con éxito: {archivo}")
        else:
            print(f"[*] Nodo {nombre} detectado y listo para operación.")
            
    print("-" * 66)
    print("[OK] Canales segregados. Los flujos ya no se mezclarán por defecto.")
    print("==================================================================")

if __name__ == '__main__':
    inicializar_nodos_separados()
