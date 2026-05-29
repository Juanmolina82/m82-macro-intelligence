import time
import random

def monitor_quantum_assets():
    print("==================================================================")
    print(" M82-MARKET: MONITOREO CUÁNTICO - COMPRA ESTATAL DE EE.UU.       ")
    print("==================================================================")
    
    # Portafolio asignado según el cable de WSJ
    portfolio = {
        "IBM": {"name": "International Business Machines", "allocation": 1000, "base_price": 185.50},
        "GFS": {"name": "GlobalFoundries Inc.", "allocation": 375, "base_price": 52.20},
        "QBTS": {"name": "D-Wave Quantum Inc.", "allocation": 100, "base_price": 1.15},
        "RGTI": {"name": "Rigetti Computing", "allocation": 100, "base_price": 1.02},
        "IONQ": {"name": "IonQ Inc.", "allocation": 100, "base_price": 7.80}
    }
    
    # Simulación de sesión regular y After-Hours
    sessions = ["REGULAR SESSION", "AFTER-HOURS TRADING"]
    
    for session in sessions:
        print(f"\n>>> MONITOREO DE MERCADO: {session} <<<")
        print("-" * 66)
        
        for ticker, info in portfolio.items():
            # El After-Hours reacciona con mayor volatilidad a los cables de Washington
            volatility_factor = 1.15 if session == "AFTER-HOURS TRADING" else 1.05
            allocation_weight = info["allocation"] / 1000.0
            
            # Algoritmo de impacto por inyección de liquidez
            surge = (random.uniform(5.0, 15.0) * volatility_factor * allocation_weight)
            simulated_price = info["base_price"] * (1 + (surge / 100))
            
            print(f"[{ticker}] {info['name'][:25]:<25} | Inyección: ${info['allocation']}MM | Imp.: +{surge:.2f}% | Precio: ${simulated_price:.2f}")
            time.sleep(0.5)
            
monitor_quantum_assets()
