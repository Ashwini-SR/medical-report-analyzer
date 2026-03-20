import streamlit as st
import requests

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(page_title="Clinical AI", layout="wide")

# ---------------- TITLE & STYLE ---------------- #
st.markdown("""
<style>
/* GLOBAL */
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
    background-color: #0f172a;
    color: #e2e8f0;
}

/* MAIN CONTAINER */
.main-box {
    background: #020617;
    padding: 30px;
    border-radius: 16px;
    border: 1px solid #1e293b;
    text-align: center;
    margin-bottom: 25px;
}

/* TITLE */
.title {
    font-size: 42px;
    font-weight: 700;
    color: #38bdf8;
}

/* SUBTITLE */
.subtitle {
    font-size: 18px;
    color: #94a3b8;
}

/* FILE UPLOADER */
section[data-testid="stFileUploader"] {
    border: 2px dashed #38bdf8;
    border-radius: 12px;
    padding: 15px;
    background-color: #020617;
}

/* CARDS */
.card {
    background: #020617;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #1e293b;
    margin-bottom: 15px;
}

/* HEADINGS */
h1, h2, h3 {
    color: #f1f5f9;
}

/* SUCCESS / WARNING COLORS */
.stSuccess { color: #22c55e !important; }
.stWarning { color: #facc15 !important; }
.stError { color: #ef4444 !important; }

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-box">
    <div class="title"> Clinical Intelligence Engine</div>
    <div class="subtitle">AI-powered analysis of patient reports</div>
</div>
""", unsafe_allow_html=True)
st.caption("Built for ET Gen AI Hackathon • Clinical Decision Support System")
st.markdown("---")

# ---------------- FILE UPLOAD ---------------- #
uploaded_file = st.file_uploader("📂 Upload Patient Report (PDF)", type=["pdf"])

def call_backend(file):
    url = "http://127.0.0.1:8000/process"
    files = {"file": (file.name, file, "application/pdf")}
    try:
        response = requests.post(url, files=files)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Backend error: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")
        return None

# ---------------- MAIN LOGIC ---------------- #
if uploaded_file is not None:
    st.success("✅ File uploaded successfully!")

    with st.spinner("🤖 AI analyzing report..."):
        data = call_backend(uploaded_file)

    if data is None or "error" in data:
        st.error(data["error"] if data and "error" in data else "Backend failed")
        st.stop()

    st.success(" Analysis complete!")
    st.markdown("---")

    # ---------------- DISPLAY COLUMNS ---------------- #
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 📄 Status")
        st.success("Processed")

    with col2:
        st.markdown("### ⚠️ Risk Level")
        if data["risk"] == "High":
            st.error("🔴 HIGH RISK")
        elif data["risk"] == "Medium":
            st.warning("🟡 MEDIUM RISK")
        else:
            st.success("🟢 LOW RISK")

    with col3:
        st.markdown("### 🧪 Parameters")
        st.info(f"{len(data['extracted'])} Checked")

    st.markdown("---")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧠 Patient Summary")
    st.write(data["summary"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.subheader("📊 Key Insights")
    for insight in data["insights"]:
        if "High" in insight:
            st.error(f"🔴 {insight}")
        elif "Low" in insight:
            st.warning(f"🟡 {insight}")
        else:
            st.success(f"🟢 {insight}")
    import pandas as pd

    if "timeline" in data:
        st.subheader("📈 Report Trend")

        df = pd.DataFrame(data["timeline"])
        st.line_chart(df.set_index("test"))
    st.subheader("📄 Extracted Report Values")
    for key, value in data["extracted"].items():
        if key.lower() in ["glucose", "cholesterol"]:
            st.error(f"🔴 {key}: {value}")
        elif key.lower() == "hemoglobin":
            st.warning(f"🟡 {key}: {value}")
        else:
            st.success(f"🟢 {key}: {value}")

    st.markdown("---")
    st.subheader("💡 Why this Risk?")
    st.info(data["explanation"])

    st.markdown("---")
    with st.expander("🔍 View Full Technical Data"):
        st.json(data)

else:
    st.info("👆 Upload a patient report to begin analysis")

# ---------------- FOOTER ---------------- #
st.markdown("---")
st.caption("🚀 Designed to reduce doctor workload and improve patient safety")
