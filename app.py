import streamlit as st
from voice.stt import STT
from voice.tts import TTS
from orchestrator.main import get_market_brief

st.title("Finance Assistant")

st.write("Speak your query:")
audio_file = st.file_uploader("Upload audio file", type=["wav", "mp3"])

if audio_file:
    stt = STT()
    query = stt.transcribe(audio_file)
    st.write(f"You asked: {query}")

    if st.button("Get Market Brief"):
        response = get_market_brief(query)
        st.write(response)
        tts = TTS()
        tts.text_to_speech(response['narrative'])
