import os

import whisper
import streamlit as st


def upload():

    audios = st.file_uploader("Carica gli audio", type=["mp3", "mp4", "wav"], accept_multiple_files=True)
    transcribe = st.button("Trascrivi")

    if transcribe:
        for a in audios:
            filename = a.name
            with open(os.path.join("audio", filename), "wb") as audio:
                audio.write(a.getvalue())

            with st.spinner("Sto caricando il modello e trascrivendo l'audio..."):
                model = whisper.load_model("small")
                result = model.transcribe(os.path.join("audio", filename), fp16=False)

            st.code(result["text"], language=None)
