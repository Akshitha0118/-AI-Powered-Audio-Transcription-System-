# Install dependency
# !pip install groq

import os
from groq import Groq

# 🔐 Set API Key (BEST PRACTICE: use environment variable, not hardcoded)
os.environ["GROQ_API_KEY"] = "your groq api key "

# Initialize client
client = Groq()

# -------------------------------
# 🧠 1. CHAT FUNCTION
# -------------------------------
def chat_with_groq(prompt):
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
    )

    print("\n🤖 Response:\n")
    for chunk in completion:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="")


# -------------------------------
# 🎙️ 2. AUDIO TRANSCRIPTION FUNCTION
# -------------------------------
def transcribe_audio(file_path):
    with open(file_path, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(file_path, file.read()),
            model="whisper-large-v3",
            temperature=0,
            response_format="verbose_json",
        )

    print("\n📝 Transcription:\n")
    print(transcription.text)


# -------------------------------
# 🚀 MAIN EXECUTION
# -------------------------------
if __name__ == "__main__":

    # Chat Example
    chat_with_groq("Explain difference between AI vs GenAI vs Agentic AI with examples")

    # Audio Example (make sure file exists)
    # transcribe_audio("audio.m4a")