import streamlit as st
import requests
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(page_title="Clinical AI", layout="wide")

# ---------------- STYLE ---------------- #
st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(135deg,#020617,#030712,#020617);
}

/* REMOVE TOP WHITE BAR */
header[data-testid="stHeader"] {
    background: linear-gradient(180deg,#020617,#030712) !important;
}

/* REMOVE WHITE MAIN AREA */
.main {
    background: transparent !important;
}

/* REMOVE EXTRA TOP SPACE */
.block-container {
    padding-top: 1rem !important;
}

/* SIDEBAR FULL DARK */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#020617,#030712,#020617);
    border-right: 1px solid #111827;
}

/* REMOVE WHITE SPACE IN SIDEBAR */
section[data-testid="stSidebar"] > div {
    background: transparent;
}

/* SIDEBAR TEXT COLOR */
section[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

/* NAVIGATION BUTTON STYLE */
div[role="radiogroup"] > label {

    background: linear-gradient(145deg,#030712,#020617);

    padding: 14px;

    margin-bottom: 10px;

    border-radius: 14px;

    border: 1px solid #111827;

    transition: 0.3s;

}

/* HOVER EFFECT */
div[role="radiogroup"] > label:hover {

    background: linear-gradient(145deg,#111827,#030712);

    border: 1px solid #a855f7;

    transform: translateX(3px);

}

/* SELECTED PAGE TEXT */
div[role="radiogroup"] input:checked + div {

    color: #ffffff;

    font-weight: 600;

}

/* HEADER CARD */
.main-box {

    background: linear-gradient(120deg,#030712,#020617,#030712);

    padding: 40px;

    border-radius: 20px;

    border: 1px solid #111827;

    text-align: center;

    margin-bottom: 25px;

    margin-top: 40px;   /* moves box downward */

    box-shadow: 0 0 40px rgba(168,85,247,0.35);

}

/* FORCE DARK MODE FOR UPLOADER (WORKS EVEN IN LIGHT MODE) */

[data-testid="stFileUploader"] {
    background: linear-gradient(145deg,#020617,#030712) !important;
    border: 1px dashed #a855f7 !important;
    border-radius: 16px !important;
    padding: 18px !important;
}

/* INNER BOX */
[data-testid="stFileUploader"] section {
    background: linear-gradient(145deg,#020617,#030712) !important;
}

/* DROP ZONE */
[data-testid="stFileUploaderDropzone"] {
    background: linear-gradient(145deg,#020617,#030712) !important;
    border-radius: 14px !important;
}

/* REMOVE WHITE BACKGROUND */
[data-testid="stFileUploaderDropzone"] div {
    background: transparent !important;
}

/* TEXT COLOR */
[data-testid="stFileUploaderDropzone"] * {
    color: white !important;
}

/* BUTTON STYLE */
[data-testid="stFileUploaderDropzone"] button {
    background: linear-gradient(90deg,#a855f7,#ec4899) !important;
    color: white !important;
    border-radius: 8px !important;
    border: none !important;
}

/* LABEL COLOR */
label {
    color: white !important;
}

/* TITLE */
.title {

    font-size: 46px;

    font-weight: 700;

    background: linear-gradient(90deg,#a855f7,#ec4899,#f472b6);

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

}

/* SUBTITLE */
.subtitle {

    font-size: 18px;

    color: #e5e7eb;

}

/* SECTION TITLE BAR */
.blue-bar {

    background: linear-gradient(90deg,#a855f7,#ec4899);

    color: white;

    padding: 16px 26px;

    border-radius: 40px;

    font-size: 22px;

    font-weight: 600;

    margin-bottom: 18px;

    box-shadow: 0 0 20px rgba(236,72,153,0.35);

}

/* SUCCESS */
.stSuccess {

    background: rgba(34,197,94,0.15);

    border-radius: 12px;

}

/* WARNING */
.stWarning {

    background: rgba(250,204,21,0.15);

    border-radius: 12px;

}

/* ERROR */
.stError {

    background: rgba(239,68,68,0.15);

    border-radius: 12px;

}

/* FILE UPLOADER MAIN BOX */
section[data-testid="stFileUploader"] {

    background: linear-gradient(145deg,#030712,#020617) !important;

    border: 1px dashed #a855f7 !important;

    border-radius: 16px !important;

    padding: 20px !important;

}

/* REMOVE WHITE INSIDE UPLOADER */
section[data-testid="stFileUploader"] div {

    background: transparent !important;

    color: white !important;

}

/* UPLOAD BUTTON */
section[data-testid="stFileUploader"] button {

    background: linear-gradient(90deg,#a855f7,#ec4899) !important;

    color: white !important;

    border-radius: 8px !important;

    border: none !important;

}

/* INFO BOX */
.stAlert {

    background: linear-gradient(145deg,#030712,#020617);

    border-radius: 12px;

}
/* FIX WHITE BACKGROUND INSIDE UPLOAD BOX */
section[data-testid="stFileUploader"] > div {

    background: linear-gradient(145deg,#030712,#020617) !important;

    border-radius: 16px !important;

}

/* DROP AREA */
div[data-testid="stFileUploaderDropzone"] {

    background: linear-gradient(145deg,#030712,#020617) !important;

    border: 1px dashed #a855f7 !important;

    border-radius: 16px !important;

}

/* REMOVE WHITE BOX INSIDE */
div[data-testid="stFileUploaderDropzone"] div {

    background: transparent !important;

}

/* TEXT COLOR INSIDE */
div[data-testid="stFileUploaderDropzone"] * {

    color: #ffffff !important;

}

/* BROWSE BUTTON */
div[data-testid="stFileUploaderDropzone"] button {

    background: linear-gradient(90deg,#a855f7,#ec4899) !important;

    color: white !important;

    border-radius: 8px !important;

    border: none !important;

}

</style>
""", unsafe_allow_html=True)



# ---------------- HEADER ---------------- #
st.markdown("""
<div class="main-box">
<div class="title">Clinical Intelligence Engine</div>
<div class="subtitle">AI-powered analysis of patient reports</div>
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
st.sidebar.markdown("## 🧭 Navigation")

st.sidebar.markdown("""
### 🏥 Clinical AI
AI Decision Support System
""")

page = st.sidebar.radio(
    "Navigation",
    [
        "Upload Report",
        "Patient Summary",
        "Key Insights",
        "Clinical Explanation",
        "Trends",
        "Extracted Values",
        "Medical Codes",
        "Technical Data"
    ]
)

# ---------------- FILE UPLOAD ---------------- #
uploaded_file = st.sidebar.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

def call_backend(file):
    url = "http://127.0.0.1:8000/process"

    try:
        files = {"file": (file.name, file, "application/pdf")}
        response = requests.post(url, files=files)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Backend error {response.status_code}"}

    except Exception as e:
        return {"error": str(e)}


# ---------------- GET DATA ---------------- #
if uploaded_file and "data" not in st.session_state:
    with st.spinner("Analyzing new report..."):
        st.session_state.data = call_backend(uploaded_file)

data = st.session_state.get("data")
# HANDLE BACKEND ERROR
if data and "error" in data:
    st.error(f"❌ {data['error']}")
    st.stop()

# ---------------- PAGE CONTENT ---------------- #

if page == "Upload Report":

    st.info("Upload medical report from sidebar")


elif data is None:

    st.warning("Please upload report first")


# ---------------- SUMMARY ---------------- #
elif page == "Patient Summary":

    st.markdown('<div class="blue-bar">🧠 Patient Summary</div>',
                unsafe_allow_html=True)

    st.write(data["summary"])


# ---------------- INSIGHTS ---------------- #
elif page == "Key Insights":

    st.markdown('<div class="blue-bar">📊 Key Insights</div>',
                unsafe_allow_html=True)

    for insight in data["insights"]:

        if "High" in insight:
            st.error(insight)

        elif "Low" in insight:
            st.warning(insight)

        else:
            st.success(insight)


# ---------------- EXPLANATION ---------------- #
elif page == "Clinical Explanation":

    st.markdown('<div class="blue-bar">🧾 Clinical Explanation</div>',
                unsafe_allow_html=True)

    for exp in data["explanation"]:
        st.write("•", exp)


# ---------------- TREND ---------------- #
elif page == "Trends":

    st.markdown('<div class="blue-bar">📈 Report Trend</div>',
                unsafe_allow_html=True)

    if "timeline" in data and len(data["timeline"]) > 0:
        df = pd.DataFrame(data["timeline"])
        st.line_chart(df.set_index("test"))
    else:
        st.warning("No trend data available")


# ---------------- VALUES ---------------- #
elif page == "Extracted Values":

    st.markdown('<div class="blue-bar">📄 Extracted Values</div>',
                unsafe_allow_html=True)

    for key, value in data["extracted"].items():

        if key.lower() in ["glucose", "cholesterol"]:
            st.error(f"{key}: {value}")

        elif key.lower() == "hemoglobin":
            st.warning(f"{key}: {value}")

        else:
            st.success(f"{key}: {value}")
elif page == "Medical Codes":

    st.markdown('<div class="blue-bar">🏷 Medical Coding (ICD-10 & CPT)</div>',
                unsafe_allow_html=True)

    # ---------------- ICD CODES ---------------- #
    st.subheader("🧾 ICD-10 Codes (Diagnosis)")

    if data.get("icd_codes"):
        for code in data["icd_codes"]:
            st.success(f"{code['code']} — {code['description']}")
    else:
        st.info("No diagnosis codes assigned (all values normal)")

    # ---------------- CPT CODES ---------------- #
    st.subheader("🧪 CPT Codes (Tests Performed)")

    if data.get("cpt_codes"):
        for code in data["cpt_codes"]:
            st.info(f"{code['code']} — {code['description']}")
    else:
        st.warning("No CPT codes detected")

    # ---------------- CLARIFICATION ---------------- #
    if data.get("clarification_needed"):

        st.markdown("### ⚠️ Clarification Required")

        st.error(
            "Some lab values could not be mapped clearly. "
            "Medical review is recommended before final coding."
        )

    # ---------------- REASONING ---------------- #
    st.markdown("### 🧠 Coding Reasoning")

    if data.get("coding_reasoning"):
        for r in data["coding_reasoning"]:
            st.write(f"• {r}")

# ---------------- RAW JSON ---------------- #
elif page == "Technical Data":

    st.markdown('<div class="blue-bar">🔍 Technical Data</div>',
                unsafe_allow_html=True)

    st.json(data)


# ---------------- FOOTER ---------------- #
st.sidebar.markdown("---")
st.sidebar.caption("Clinical AI System")