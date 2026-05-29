import os, time

DATA_POINTS = [
    "🔥 ENERGY: KMI Pipeline restrictions (NYC/NJ Impact)",
    "💎 PE: Blackstone buys Skroutz | CVC AGM Approved",
    "🇬🇧 BANKS: Fitch Upgrades (BCS, NWG, LYG, SAN) to AA/AA-",
    "📉 MARKET: FTSE (-0.04%), DAX (-1.54%), VODAFONE (-8%)",
    "⚠️  POLITICS: Starmer Crisis in UK vs. Gilt Yields spike",
    "🏛️  FED: Goolsbee signals persistent services inflation",
    "🛰️  GEO: Trump/Iran tension supports Oil prices (+1%)",
    "🏙️  INFRA: Lufthansa increases ITA stake to 90%",
    "📊 BONDS: US 20Y/30Y Yields hitting 5.02%",
    "☢️  RISK: Metro Bank downgrade to BB- (Speculative)"
]

def update_bridge():
    path = os.path.expanduser("~/M82_Core/m82_bridge.txt")
    with open(path, "w") as f:
        f.write(f"🏛️  MOLINA GLOBAL | CONSOLIDATED INTELLIGENCE | {time.strftime('%T')}\n")
        f.write("="*60 + "\n")
        f.write("CORE WORKSPACE INSIGHTS (LAST 10 REPORTS):\n")
        for i, point in enumerate(DATA_POINTS, 1):
            f.write(f"{i:02d}. {point}\n")
        f.write("-" * 60 + "\n")
        f.write("🛡️  STRATEGY: LONG ENERGY | SHORT GROWTH | HOLD AA-BANKS\n")
        f.write("="*60 + "\n")

if __name__ == "__main__":
    update_bridge()
    print("✅ Sesión 1 Actualizada con el Resumen Global.")
