
# 🎙️ AudioTranscriber — AI-Powered Speech to Text

> Instantly convert audio files into accurate text using **Groq API** + **Whisper Large V3** + **Streamlit**

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red?style=flat&logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-API-orange?style=flat)
![Whisper](https://img.shields.io/badge/Whisper-Large--V3-green?style=flat)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

---

## 📌 About The Project

**AudioTranscriber** is a simple yet powerful web application that converts audio files into text using state-of-the-art AI models. It leverages **Groq's ultra-fast inference engine** and **OpenAI's Whisper Large V3** model for highly accurate speech recognition — all wrapped in a clean and interactive **Streamlit** interface.

---

## ✨ Features

- 🎵 Upload audio files (MP3, WAV, M4A)
- ⚡ Ultra-fast transcription powered by Groq API
- 🧠 High accuracy using Whisper Large V3 model
- 🎧 Built-in audio player to preview uploaded files
- 🌙 Clean dark-themed modern UI
- 📋 Instant text output ready to copy

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core backend language |
| 🌐 Streamlit | Web interface framework |
| ⚡ Groq API | Ultra-fast AI inference engine |
| 🎙️ Whisper Large V3 | Speech recognition model |

---

## 📁 Project Structure

```
AudioTranscriber/
│
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── temp_audio.mp3       # Temporary file (auto-generated, auto-deleted)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A Groq API key → [Get it here](https://console.groq.com)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/AudioTranscriber.git
cd AudioTranscriber
```

2. **Install dependencies**
```bash
pip install streamlit groq
```

3. **Set your Groq API key**

Open `app.py` and replace:
```python
os.environ["GROQ_API_KEY"] = "your_api_key_here"
```
with your actual API key. Or set it as an environment variable:
```bash
export GROQ_API_KEY="your_actual_api_key"
```

4. **Run the application**
```bash
streamlit run app.py
```

5. Open your browser and go to `http://localhost:8501`

---

## 🎯 How To Use

1. Launch the app using the command above
2. Upload an audio file (MP3, WAV, or M4A)
3. Preview the audio using the built-in player
4. Click **🚀 Transcribe**
5. Wait a few seconds for the AI to process
6. Copy your transcribed text!

---

## 💡 Use Cases

- 📅 Meeting & conference transcriptions
- 🎙️ Podcast to text conversion
- 🎓 Lecture notes from recordings
- 🗣️ Interview transcriptions
- 📝 Voice memo to written notes

---

## ⚙️ Configuration

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `whisper-large-v3` | Whisper model used for transcription |
| `temperature` | `0` | Lower = more accurate & deterministic |
| `response_format` | `verbose_json` | Returns detailed transcription data |

---

## 📦 Requirements

```txt
streamlit
groq
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🔐 API Key Security

> ⚠️ **Important:** Never hardcode your API key in production. Use environment variables or a `.env` file.

```bash
# Recommended: use a .env file
GROQ_API_KEY=your_actual_api_key_here
```

Add `.env` to your `.gitignore`:
```bash
echo ".env" >> .gitignore
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---



## ⭐ Show Your Support

If you found this project helpful, please give it a **⭐ star** on GitHub — it means a lot!

---

> Built with ❤️ using Python, Streamlit, and Groq API
