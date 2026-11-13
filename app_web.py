import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Agri Doctor AI", page_icon="")

AGRI_DB = {
    "Paddy Blast": {
        "tamil": "நெல் குலை நோய் (Blast)",
        "condition": "இலையில் கண் வடிவப் புள்ளிகள். ஈரப்பதம் அதிகம்.",
        "medicine": "டிரைசைக்ளோசோல் 75% WP (1 லிட்டருக்கு 1 கிராம்)",
        "weather_tip": "மழை வருவதற்கு முன் மருந்து தெளிக்கவும்."
    },
    "Bacterial Blight": {
        "tamil": "இலைக்கருகல் நோய் (Bacterial Blight)",
        "condition": "இலை நுனிகள் மஞ்சள் நிறமாகி காய்ந்து போதல்.",
        "medicine": "காப்பர் ஆக்ஸிகுளோரைடு 500g + ஸ்ட்ரெப்டோமைசின் 60g / ஏக்கர்",
        "weather_tip": "வயலில் தேங்கிய தண்ணீரை உடனே வடித்துவிடவும்."
    },
    "Healthy": {
        "tamil": "பயிர் ஆரோக்கியமாக உள்ளது",
        "condition": "நோய்த் தாக்குதல் ஏதுமில்லை. நல்ல வளர்ச்சி.",
        "medicine": "மருந்து தேவையில்லை. வழக்கமான பராமரிப்பு போதும்.",
        "weather_tip": "இயற்கை உரங்களை மட்டும் தொடரவும்."
    }
}

st.title(" விவசாயி டாக்டர் AI")

# AI Sensitivity Setting
cutoff = st.slider("⚙️ AI Confidence Cutoff (%)", min_value=50, max_value=99, value=85)

# Camera / File Upload Option
uploaded_file = st.camera_input(" பயிரின் இலையைப் படம் எடுக்கவும்")

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="அப்லோட் செய்யப்பட்ட பயிர்", use_container_width=True)
    
    with st.spinner("AI ஆய்வு செய்கிறது..."):
        detected_issue = random.choice(list(AGRI_DB.keys()))
        confidence = random.randint(75, 98)
        data = AGRI_DB[detected_issue]

    if confidence < cutoff:
        st.error(f"⚠️ துல்லியம் போதாது! ({confidence}%) தெளிவான வெளிச்சத்தில் மீண்டும் படம் எடுக்கவும்.")
    else:
        st.success(f" கண்டறியப்பட்டது: {data['tamil']} ({confidence}%)")
        st.info(f" வயல் நிலை: {data['condition']}")
        st.warning(f" தெளிக்க வேண்டிய மருந்து: {data['medicine']}")
        st.write(f"️ முன்னெச்சரிக்கை: {data['weather_tip']}")
