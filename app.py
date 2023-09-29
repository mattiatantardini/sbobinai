import logging
import os

from tantaroba.log import configure_logging
import streamlit as st
import whisper
from st_audiorec import st_audiorec

from app.style import footer_include_version


if __name__ == "__main__":
    configure_logging()
    logging.info("Welcome to sbobinai app!")

    st.set_page_config(
        page_title="SbobinAI", page_icon=None, layout="centered", initial_sidebar_state="expanded")
    footer_include_version()
    
    st.sidebar.title("SbobinAI")
    st.sidebar.write("Sbobinare a mano è solo un ricordo!")

    upload_tab, record_tab = st.tabs(["Carica", "Registra"])

    with upload_tab:
        st.balloons()

    with record_tab:
        wav_audio_data = st_audiorec()
        
        if wav_audio_data is not None:
            os.makedirs("audio", exist_ok=True)
            with open("audio/test1.wav", "wb") as audio:
                audio.write(wav_audio_data)

            transcribe = st.button("Trascrivi")

            if transcribe:
        
                with st.spinner("Sto caricando il modello e trascrivendo l'audio..."):
                    model = whisper.load_model("small")
                    result = model.transcribe("audio/test1.wav", fp16=False)

                st.code(result["text"], language=None)
