import os

import whisper
import streamlit as st

from settings.constants import AUDIO_FOLDER


def run_model(filename: str, model_type: str = "small", prompt: str="") -> str:
    with st.spinner("Sto caricando il modello e trascrivendo l'audio..."):
        model = whisper.load_model(model_type)
        result = model.transcribe(filename, fp16=False, initial_prompt=prompt)
    return result["text"]