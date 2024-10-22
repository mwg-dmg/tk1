import streamlit as st
import pandas as pd
st.set_page_config(page_title="MWG",page_icon="&",layout="centered",initial_sidebar_state="auto",menu_items=None)
if "page" not in st.session_state:
    st.session_state.page = 1


def Lout():
    st.session_state.page=0
    st.session_state.status =0




st.title(":green[Upcomming Trek]")
st.title(":blue[Pawankhind,  Manoli Lake]")

