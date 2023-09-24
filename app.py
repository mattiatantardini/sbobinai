import logging
import os

from tantaroba.log import configure_logging
import streamlit as st
import whisper
from st_audiorec import st_audiorec
import pyperclip

from app.style import footer_include_version


def copy_to_clipboard(text: str) -> None:
    pyperclip.copy(text)


if __name__ == "__main__":
    configure_logging()
    footer_include_version()

    logging.info("Welcome to sbobinai app!")
    st.title("Your first app!")
    wav_audio_data = st_audiorec()
    
    os.makedirs("audio", exist_ok=True)
    with open("audio/test1.wav", "wb") as audio:
        audio.write(wav_audio_data)
    
    with st.spinner("Sto caricando il modello e trascrivendo l'audio..."):
        model = whisper.load_model("small")
        result = model.transcribe("audio/test1.wav", fp16=False)

    
    st.text_area("Testo trascritto:", result["text"])

    st.button("Copia", on_click=copy_to_clipboard, args=(result["text"],))



    # st.balloons()

    
