import streamlit as st

st.set_page_config(page_title="M82 Ultra-Light v12.0", page_icon="🦅", layout="wide")

st.title("🦅 MOLINA HOLDINGS & GLOBAL LLC")
st.subheader("M82 COMET - Ultra-Light Tactical Terminal v12.0")
st.markdown("---")

# ==============================================================================
# 1. ENTORNO DE VALORACIÓN NETO (DATOS INTEGRADOS FIJOS)
# ==============================================================================
st.markdown("### 🏦 VALORACIÓN DE ACTIVOS PROPIETARIOS")
col1, col2 = st.columns(2)
col1.metric("💰 VALOR NETO EQUITIES EN VIVO", "$30,166.70 USD")
col2.metric("📈 P&L FLOTANTE ESTIMADO DEL DÍA", "-$330.80 USD")
st.markdown("---")

# ==============================================================================
# 2. AUDITORÍA MATRIZ IBD FUNDAMENTALS (RECOPILACIÓN COMPLETA DE SEÑALES)
# ==============================================================================
st.markdown("### 📊 MÓDULO DE AUDITORÍA AVANZADA IBD")
activo = st.selectbox("Seleccione activo para auditar:", ["WALMART (WMT)", "NVIDIA (NVDA)"])

if activo == "WALMART (WMT)":
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Composite Rating", "75")
    c2.metric("RS Rating", "72")
    c3.metric("P/E Ratio", "50")
    c4.metric("Return on Equity", "23%")
    
    st.markdown("#### Historial de Métricas & Proyecciones FactSet (WMT)")
    # Renderizado HTML nativo ultra rápido sin usar Pandas pesado
    st.write(
        """
        <table style='width:100%; border: 1px solid #444; border-collapse: collapse; text-align: left;'>
          <tr style='background-color: #222; color: white;'>
            <th style='padding: 8px;'>Año</th>
            <th style='padding: 8px;'>EPS ($)</th>
            <th style='padding: 8px;'>Sales ($B)</th>
          </tr>
          <tr><td style='padding: 8px;'>2023</td><td style='padding: 8px;'>2.22</td><td style='padding: 8px;'>648.1</td></tr>
          <tr><td style='padding: 8px;'>2024</td><td style='padding: 8px;'>2.51</td><td style='padding: 8px;'>681.0</td></tr>
          <tr><td style='padding: 8px;'>2025</td><td style='padding: 8px;'>2.64</td><td style='padding: 8px;'>713.2</td></tr>
          <tr style='color: #00ff00;'><td style='padding: 8px;'>2026 e</td><td style='padding: 8px;'>2.92</td><td style='padding: 8px;'>748.7</td></tr>
          <tr style='color: #00ff00;'><td style='padding: 8px;'>2027 e</td><td style='padding: 8px;'>3.29</td><td style='padding: 8px;'>784.6</td></tr>
        </table>
        """, unsafe_allow_html=True
    )
else:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Composite Rating", "88")
    c2.metric("RS Rating", "89")
    c3.metric("Forward P/E", "19.0x")
    c4.metric("Debt/Equity", "7.3%")
st.markdown("---")

# ==============================================================================
# 3. RADAR DE OPCIONES INSTITUCIONALES (DERIVADOS EXPOSURE)
# ==============================================================================
st.markdown("### 👁️ RADAR DE EXPOSICIÓN EN OPCIONES INSTITUCIONALES")
opc = st.radio("Flujo institucional activo:", ["MSFT Call Block ($5.37M)", "NVDA Short Put Block ($1.4M)"])
m1, m2, m3 = st.columns(3)
if opc == "MSFT Call Block ($5.37M)":
    m1.metric("Strike Call (K)", "$420.00")
    m2.metric("Prima de Entrada", "$90.00")
    m3.metric("Break-Even Target", "$510.00")
else:
    m1.metric("Strike Put (K)", "$100.00")
    m2.metric("Prima Recibida", "$41.00")
    m3.metric("Break-Even Target", "$59.00")
st.markdown("---")

# ==============================================================================
# 4. ENERGY COMPLEX: BRENT CRUDE FORWARD CURVE (RÉPLICA EXACTA MOOMOO)
# ==============================================================================
st.header("🛢️ ENERGY COMPLEX: BRENT CRUDE FORWARD CURVE")
st.markdown("Distribución de contratos reflejando la estructura analizada de **Backwardation**.")

st.write(
    """
    <table style='width:100%; border: 1px solid #444; border-collapse: collapse; text-align: left;'>
      <tr style='background-color: #222; color: white;'>
        <th style='padding: 8px;'>Contrato / Vencimiento</th>
        <th style='padding: 8px;'>Precio Último</th>
        <th style='padding: 8px;'>Variación</th>
        <th style='padding: 8px;'>Estructura</th>
      </tr>
      <tr><td style='padding: 8px;'><b>BZMain</b> (Front Month)</td><td style='padding: 8px;'>$111.00 USD</td><td style='padding: 8px; color:#ff4b4b;'>-0.98%</td><td style='padding: 8px;'>📋 Base</td></tr>
      <tr><td style='padding: 8px;'><b>BZcurrent</b> (Activo)</td><td style='padding: 8px;'>$111.00 USD</td><td style='padding: 8px; color:#ff4b4b;'>-0.98%</td><td style='padding: 8px;'>📋 Base</td></tr>
      <tr><td style='padding: 8px;'><b>BZnext</b> (Próximo)</td><td style='padding: 8px;'>$106.55 USD</td><td style='padding: 8px; color:#ff4b4b;'>-0.87%</td><td style='padding: 8px; color:#ff4b4b;'>🔴 Backwardation Premium</td></tr>
      <tr><td style='padding: 8px;'><b>BZ2609</b> (Septiembre)</td><td style='padding: 8px;'>$101.73 USD</td><td style='padding: 8px; color:#ff4b4b;'>-1.01%</td><td style='padding: 8px; color:#ff4b4b;'>🔴 Backwardation Premium</td></tr>
      <tr><td style='padding: 8px;'><b>BZ2611</b> (Noviembre)</td><td style='padding: 8px;'>$94.32 USD</td><td style='padding: 8px; color:#ff4b4b;'>-1.19%</td><td style='padding: 8px; color:#ff4b4b;'>🔴 Backwardation Premium</td></tr>
    </table>
    """, unsafe_allow_html=True
)
st.markdown("---")

# ==============================================================================
# 5. GRID DE FUTUROS COMPACTO DE ALTA VELOCIDAD
# ==============================================================================
st.header("🇺🇸 MAJOR US & MICRO FUTURES")
f1, f2, f3, f4 = st.columns(4)
f1.metric("NQ=F (Nasdaq 100)", "28,899.25", "-0.68%")
f2.metric("ES=F (S&P 500)", "7,372.50", "-0.72%")
f3.metric("YM=F (Dow Jones)", "49,430", "-0.68%")
f4.metric("RTY=F (Russell 2000)", "2,752.0", "-1.10%")

st.caption("M82 Sovereign Terminal v12.0 • Ultra-Light Fast Local Engine Ready.")
