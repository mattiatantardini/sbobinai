import os

import streamlit as st

from app.model.model import run_model
from settings.constants import AUDIO_FOLDER


def upload(prompt: str):

    audios = st.file_uploader("Carica gli audio", type=["mp3", "mp4", "wav", "m4a"], accept_multiple_files=True)
    transcribe = st.button("Trascrivi", use_container_width=True)

    if transcribe:
        for a in audios:
            filename = a.name
            filepath = os.path.join(AUDIO_FOLDER, filename)
            with open(filepath, "wb") as audio:
                audio.write(a.getvalue())

            text = run_model(filepath, prompt=prompt)
            st.write(filename)
            st.code(text, language=None)
