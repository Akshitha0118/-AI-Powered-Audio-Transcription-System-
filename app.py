# Install dependencies
# !pip install streamlit groq

import streamlit as st
import os
from groq import Groq

# 🔐 Set API key (use env variable in real apps)
os.environ["GROQ_API_KEY"] = "your groq api key "

client = Groq()

# -----------------------------
# 🎨 Custom CSS Styling
# -----------------------------
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
        color: white;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #38bdf8;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #94a3b8;
        margin-bottom: 20px;
    }
    .box {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# 🧾 Header Section
# -----------------------------
st.markdown('<div class="title">🎙️ AI-Powered Audio Transcription System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload audio & get instant transcription using Groq + Whisper</div>', unsafe_allow_html=True)

# -----------------------------
# 📂 File Upload
# -----------------------------
uploaded_file = st.file_uploader("Upload Audio File", type=["mp3", "wav", "m4a"])

# -----------------------------
# 🔁 Transcription Logic
# -----------------------------
if uploaded_file is not None:
    st.audio(uploaded_file)

    if st.button("🚀 Transcribe"):
        with st.spinner("Transcribing... ⏳"):

            # Save file temporarily
            with open("temp_audio.mp3", "wb") as f:
                f.write(uploaded_file.read())

            # Call Groq API
            with open("temp_audio.mp3", "rb") as file:
                transcription = client.audio.transcriptions.create(
                    file=("temp_audio.mp3", file.read()),
                    model="whisper-large-v3",
                    temperature=0,
                    response_format="verbose_json",
                )

            # Display output
            st.markdown('<div class="box">', unsafe_allow_html=True)
            st.subheader("📝 Transcription Output")
            st.write(transcription.text)
            st.markdown('</div>', unsafe_allow_html=True)