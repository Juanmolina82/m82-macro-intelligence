import os
from datetime import datetime

def registrar_oxigeno_imf():
    print("==================================================================")
    print(" M82-LATAM: REGISTRO DE LIQUIDEZ SOBERANA - CONO SUR             ")
    print("==================================================================")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Archivo de registro específico para macroeconomía de Sudamérica
    archivo_target = "m82_latam_macro.log"
    
    log_data = (
        f"{timestamp}|IMF_ARGENTINA|Facility:EFF_Review_2|Amount:$1,000M_USD|"
        f"Impact:Net_Reserve_Oxigen|Target:Debt_Rollover|Status:APPROVED\n"
    )
    
    with open(archivo_target, "a") as f:
        f.write(log_data)
        
    print(f"[*] Operación de Financiamiento Multilateral Indexada.")
    print(f"[*] Soberano Evaluado : Argentina")
    print(f"[*] Inyección Tramo   : ~$1,000 Millones de USD (EFF Arrangement)")
    print(f"[*] Diagnóstico Mesa  : Refinanciamiento circular / Validación de metas")
    print("-" * 66)
    print(f"[OK] Canal de Liquidez LATAM actualizado en:\n -> {os.path.abspath(archivo_target)}")
    print("==================================================================")

if __name__ == '__main__':
    registrar_oxigeno_imf()
