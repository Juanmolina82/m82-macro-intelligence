import sqlite3
import os
from datetime import datetime

def update_pulse():
    db_path = '/data/data/com.termux/files/home/M82_Global_Intelligence/core/M82_Intel_Vault.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Crear tabla de estado si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS system_status 
                     (id INTEGER PRIMARY KEY, state TEXT, last_sync TEXT, spx_level REAL)''')
    
    # Insertar o actualizar estado
    cursor.execute("INSERT OR REPLACE INTO system_status (id, state, last_sync, spx_level) VALUES (1, 'ONLINE', ?, 7361.92)", 
                   (datetime.now().strftime("%Y-%m-%d %H:%M:%S"),))
    
    conn.commit()
    conn.close()
    
    print("✅ Dashboard M1982: ONLINE | Database Synced")
    # Alerta de voz sintética
    os.system("termux-tts-speak 'Chairman, M 82 Core is now online. Pulse synchronization complete.'")

if __name__ == "__main__":
    update_pulse()
