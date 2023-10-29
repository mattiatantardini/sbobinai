import os

import streamlit as st
from st_audiorec import st_audiorec

from app.model.model import run_model
from settings.constants import AUDIO_FOLDER

def record(prompt:str):
    wav_audio_data = st_audiorec()
        
    if wav_audio_data is not None:
        filepath = os.path.join(AUDIO_FOLDER, "test1.wav")
        os.makedirs(AUDIO_FOLDER, exist_ok=True)
        with open(filepath, "wb") as audio:
            audio.write(wav_audio_data)

        transcribe = st.button("Trascrivi", use_container_width=True)

        if transcribe:
            text = run_model(filepath, prompt=prompt)
            st.code(text, language=None)