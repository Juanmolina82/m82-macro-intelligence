def calculate_ddog_upside():
    CURRENT_PRICE = 185.06
    NEW_TARGET = 220.00
    
    upside_potential = ((NEW_TARGET - CURRENT_PRICE) / CURRENT_PRICE) * 100
    
    print("🛰️ M82 TARGET ANALYSIS: DATADOG (DDOG)")
    print(f"💰 CURRENT: ${CURRENT_PRICE}")
    print(f"🎯 RAYMOND JAMES TARGET: ${NEW_TARGET}")
    print(f"📈 REMAINING UPSIDE: {upside_potential:.2f}%")
    
    if upside_potential > 15:
        print("\n🔥 ACTION: MAINTAIN OVERWEIGHT POSITION.")
        print("🛡️ STRATEGY: Use trailing stop-loss at $175 to protect the 'Cup with Handle' breakout.")

if __name__ == "__main__":
    calculate_ddog_upside()
