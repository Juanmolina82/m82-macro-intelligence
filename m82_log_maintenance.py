#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

def ejecutar_mantenimiento_ledger():
    print("==================================================================")
    print(" M82-MAINTENANCE: OPTIMIZACIÓN Y ROTACIÓN DEL LEDGER DE CAPITAL   ")
    print("==================================================================")
    
    archivo_log = "m82_quantum_energy.log"
    archivo_bak = "m82_quantum_energy.log.bak"
    
    if not os.path.exists(archivo_log):
        print(f"[FAIL] No se encontró el archivo {archivo_log} para mantenimiento.")
        print("==================================================================")
        return

    # 1. Crear respaldo de seguridad atómico del estado actual (.bak)
    try:
        with open(archivo_log, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
        
        with open(archivo_bak, 'w', encoding='utf-8') as f_bak:
            f_bak.writelines(lineas)
        print(f"[OK] Respaldo de seguridad creado en: {archivo_bak}")
        
        # 2. Algoritmo de filtrado: Eliminar duplicados manteniendo el orden cronológico
        lineas_limpias = []
        entradas_vistas = set()
        duplicados_eliminados = 0
        
        for linea in lineas:
            # Si es una línea de datos transaccionales, aislamos el cuerpo del mensaje para comparar
            if "|" in linea:
                partes = linea.strip().split("|", 1)
                cuerpo_transaccion = partes[1] if len(partes) > 1 else linea
                
                if cuerpo_transaccion not in entradas_vistas:
                    entradas_vistas.add(cuerpo_transaccion)
                    lineas_limpias.append(linea)
                else:
                    duplicados_eliminados += 1
            else:
                # Mantener líneas de formato o cabeceras de texto intactas
                lineas_limpias.append(linea)
        
        # 3. Reescribir el archivo original optimizado
        with open(archivo_log, 'w', encoding='utf-8') as f:
            f.writelines(lineas_limpias)
            
        print(f"[OK] Depuración completada con éxito.")
        print(f"[*] Registros redundantes purgados : {duplicados_eliminados}")
        print(f"[*] Estado del Ledger actual       : OPTIMIZADO (HANDSHAKE)")
        print("-" * 66)
        print(f"[SYSTEM] Archivo maestro reestructurado en raíz:\n -> {os.path.abspath(archivo_log)}")
        
    except IOError as e:
        print(f"[CRITICAL] Error de E/S durante el mantenimiento: {e}")
        
    print("==================================================================")

if __name__ == '__main__':
    ejecutar_mantenimiento_ledger()
