import os

def check_holdings():
    print("\033[1;34m" + "\n[ M82 HOLDINGS - ESTATUS GLOBAL ]" + "\033[0m")
    # Lista de carpetas a verificar
    assets = ["M82-Sovereign-Core", "M82-Bunker", "M82-Governance-Master1", "MOLINA-GLOBAL-CORE-V6"]
    
    for asset in assets:
        path = os.path.expanduser(f"~/M82_HOLDINGS_LLC/{asset}")
        status = "ONLINE " if os.path.exists(path) else "OFFLINE"
        color = "\033[92m" if "ONLINE" in status else "\033[91m"
        print(f"-> {asset:<25} | {color}{status}\033[0m")
    print("")

if __name__ == "__main__":
    check_holdings()
