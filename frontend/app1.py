import streamlit as st

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(page_title="Clinical AI", layout="wide")

# ---------------- CUSTOM UI ---------------- #
st.markdown("""
<style>

/* FONT */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&family=Poppins:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background-color: #0b1120;
    color: white;
}

/* GLOW BOX */
.main-box {
    background: linear-gradient(145deg, #0f172a, #020617);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(0, 255, 255, 0.2);
    transition: 0.4s;
    text-align: center;
    margin-bottom: 20px;
}

.main-box:hover {
    box-shadow: 0 0 25px #00c6ff, 0 0 60px #0072ff;
    transform: scale(1.01);
}

/* TITLE */
.title {
    font-family: 'Orbitron', sans-serif;
    font-size: 48px;
    font-weight: 600;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* SUBTITLE */
.subtitle {
    font-size: 20px;
    color: #cbd5f5;
}

/* UPLOAD */
section[data-testid="stFileUploader"] {
    border: 2px dashed #00c6ff;
    border-radius: 12px;
    padding: 10px;
    background-color: #020617;
}

/* METRIC */
.stMetric {
    background-color: #020617;
    border-radius: 10px;
    padding: 10px;
    border: 1px solid #00c6ff;
}

/* SIDEBAR */
.css-1d391kg {
    background-color: #020617;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
with st.sidebar:
    st.title("⚙️ Settings")
    st.write("Model: Clinical AI v1")
    st.write("Mode: Demo")
    st.write("Status: Active 🟢")

# ---------------- TITLE BOX ---------------- #
st.markdown("""
<div class="main-box">
    <div class="title"> Clinical Intelligence Engine</div>
</div>
""", unsafe_allow_html=True)

# ---------------- SUBTITLE ---------------- #
st.markdown('<div class="subtitle">Smart AI assistant for analyzing patient reports</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Built for ET Gen AI Hackathon • Clinical Decision Support System")

# ---------------- FILE UPLOAD ---------------- #
uploaded_file = st.file_uploader("📂 Upload Patient Report (PDF)", type=["pdf"])
if uploaded_file is None:
    st.warning("⚠️ Please upload a patient report to start analysis")

# ---------------- DUMMY DATA ---------------- #
def get_dummy_data():
    return {
        "summary": "Patient shows elevated glucose and cholesterol levels indicating metabolic imbalance.",
        "risk": "High",
        "insights": [
            "Glucose level is significantly above normal",
            "Cholesterol is higher than recommended range",
            "Possible diabetes and cardiovascular risk"
        ],
        "extracted": {
            "Glucose": "250 mg/dL",
            "Cholesterol": "220 mg/dL",
            "Hemoglobin": "11 g/dL"
        },
        "explanation": "Risk is high because glucose and cholesterol are above safe limits."
    }

# ---------------- MAIN LOGIC ---------------- #
if uploaded_file is not None:

    st.success("✅ File uploaded successfully!")
    st.toast("Processing report...", icon="🤖")

    import time

    with st.spinner("🤖 AI analyzing report..."):
        time.sleep(2)
        data = get_dummy_data()

    st.success("🎉 Analysis complete!")

    st.markdown("---")

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

    st.subheader("Patient Summary")
    st.write(data["summary"])

    st.markdown("---")

    st.subheader("📊 Key Insights")
    for insight in data["insights"]:
        st.write(f"✔ {insight}")

    st.markdown("---")

    st.subheader("📄 Extracted Report Values")

    cols = st.columns(len(data["extracted"]))

    for i, (key, value) in enumerate(data["extracted"].items()):
        with cols[i]:
            if key in ["Glucose", "Cholesterol"]:
                st.error(f"🔴 {key}: {value}")
            elif key == "Hemoglobin":
                st.warning(f"🟡 {key}: {value}")   # <-- FIXED HERE
            else:
                st.success(f"🟢 {key}: {value}")

    st.markdown("---")
    st.success("🧠 AI Generated Insights")

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
st.info("💡 This demo uses simulated AI results. Backend integration will provide real-time analysis.")
