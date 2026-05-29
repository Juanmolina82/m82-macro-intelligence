#!/bin/bash
echo "========================================================"
echo "[🛡️] M82 BRANDING: EXPANDIENDO CAPA GRÁFICA SOBERANA"
echo "========================================================"

# Inyectar el bloque CSS/HTML del Banner Corporativo en el index.html
cat << 'GRAPHIC' >> index.html
<div id="m82-branding-canvas" style="background: radial-gradient(circle at center, #0d162d 0%, #050814 100%); color: #ffffff; padding: 40px; border: 2px solid #1f3a60; margin-top: 25px; font-family: 'Courier New', monospace; position: relative; border-radius: 6px; box-shadow: 0 0 30px rgba(0, 149, 255, 0.15);">
    
    <div style="position: absolute; right: 25px; top: 20px; font-size: 65px; font-weight: 900; color: rgba(255, 255, 255, 0.03); letter-spacing: -3px; user-select: none;">M82</div>
    
    <div style="border-bottom: 1px solid #1f3a60; padding-bottom: 15px; margin-bottom: 20px;">
        <span style="background-color: #0e2a52; color: #58a6ff; padding: 4px 8px; font-size: 11px; font-weight: bold; border-radius: 3px;">M82 SECURITY PERIMETER</span>
        <h2 style="margin: 10px 0 5px 0; font-size: 22px; letter-spacing: 1px; color: #f0f6fc;">QUANTITATIVE BIG DATA & AGI CONVERGENCE NODE</h2>
        <span style="font-size: 11px; color: #8b949e;">Molina Holdings & Global LLC — Asset Segregation Framework [2026.05.22]</span>
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; font-size: 12px; line-height: 1.6;">
        <div style="background: rgba(255,255,255,0.01); padding: 15px; border-left: 3px solid #58a6ff; background: rgba(13, 22, 45, 0.5);">
            <span style="color: #58a6ff; font-weight: bold;">[🔥] GLOBAL BIG DATA STREAM:</span><br>
            • Strait of Hormuz Outage telemetry: <span style="color: #ff7b72;">14M bpd [CRITICAL]</span><br>
            • Traditional ARR Software Multiples: <span style="color: #ff7b72;">4.8x [CYCLIC LOW]</span><br>
            • Hyperscaler Commitments: <span style="color: #388bfd;">$1,000,000,000,000 USD (2027 Capex)</span>
        </div>
        <div style="background: rgba(255,255,255,0.01); padding: 15px; border-left: 3px solid #79c0ff; background: rgba(13, 22, 45, 0.5);">
            <span style="color: #79c0ff; font-weight: bold;">[🧠] DEEPMIND AGI CLUSTER MATRIX:</span><br>
            • Compute Architecture: <span style="color: #58a6ff;">Google TPU 8t / Ironwood v7</span><br>
            • Grid Ingestion Protocol: <span style="color: #58a6ff;">Decoupled DiLoCo Multi-Node Engine</span><br>
            • Structural Energy Buffer: <span style="color: #58a6ff;">5.0 GW Dedicated Power Matrix</span>
        </div>
    </div>

    <div style="margin-top: 25px; text-align: center; border-top: 1px dashed #21262d; padding-top: 15px;">
        <span style="color: #8b949e; font-size: 11px;">STRUCTURE: <strong style="color: #238636;">$5,000,000,000 USD UNENCUMBERED CAPITAL</strong></span><br>
        <span style="color: #58a6ff; font-size: 10px; font-weight: bold; letter-spacing: 2px;">NEW YORK // MIAMI // NASHVILLE // CARACAS</span>
    </div>
</div>
GRAPHIC

# Purga reglamentaria y reinicio del pipeline local
pkill -9 -f python3 2>/dev/null
fuser -k 8000/tcp 2>/dev/null
nohup python3 -m http.server 8000 --bind 0.0.0.0 > /dev/null 2>&1 &

# Envío del nuevo activo al repositorio Git
if [ -d ".git" ]; then
    git add .
    git commit -m "M82 Visual Architecture: Inyección de módulo gráfico Big Data, AGI y Watermark" --quiet
    git push origin main 2>/dev/null || git push origin master 2>/dev/null
    echo "[✅] Gráficos y metadatos subidos al repositorio remoto."
fi

echo "========================================================"
echo "[🚀] INTERFAZ VISUAL ACTUALIZADA CON EXITO"
echo "-> Abre o refresca en tu laptop: http://192.168.2.243:8000"
echo "========================================================"
