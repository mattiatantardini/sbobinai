import logging
import os

from tantaroba.log import configure_logging
import streamlit as st

from app.style import footer_include_version
from app.tabs.upload import upload
from app.tabs.record import record
from settings.constants import MODEL_TYPE_DICT, AUDIO_FOLDER


if __name__ == "__main__":
    configure_logging()
    logging.info("Welcome to sbobinai app!")

    st.set_page_config(
        page_title="SbobinAI", page_icon=None, layout="centered", initial_sidebar_state="expanded")
    footer_include_version()
    
    with st.sidebar:
        st.title("SbobinAI")
        st.write("Sbobinare a mano è solo un ricordo!")
        prompt = st.text_area("Indica l'argomento degli audio per una migliore trascrizione (premi invio per confermare)", value="")

    os.makedirs(AUDIO_FOLDER, exist_ok=True)

    upload_tab, record_tab = st.tabs(["Carica", "Registra"])
    with upload_tab:
        upload(prompt)
    with record_tab:
        record(prompt)

    # Removing temporary audio files
    for af in os.listdir(AUDIO_FOLDER):
        os.remove(os.path.join(AUDIO_FOLDER, af))
