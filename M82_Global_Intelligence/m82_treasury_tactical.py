def execute_direct_bid_analysis():
    # Parámetros de Subasta Mayo 07, 2026
    DIRECT_BID_1M = 6.30  # +172% vs Avg
    INDIRECT_BID_1M = 47.09 # -30.4% vs Avg
    STOP_RATE_1M = 3.61
    
    print("🛰️ M82 ANALYZING TREASURY ANOMALY...")
    
    # Diagnóstico Molina Holdings
    if DIRECT_BID_1M > 6.0:
        sentiment = "DOMESTIC INSTITUTIONAL FRENZY"
        action = "LOCKING CASH IN 1-MONTH BILLS @ 3.61%"
    
    report = f"💎 SENTIMENT: {sentiment}\n"
    report += f"📊 STOP RATE: {STOP_RATE_1M}%\n"
    report += f"⚠️ RISK: Foreign demand weakening (-30%). Monitor USD stability.\n"
    
    print(report)

if __name__ == "__main__":
    execute_direct_bid_analysis()
