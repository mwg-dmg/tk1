import streamlit as st
import pandas as pd
st.set_page_config(page_title="MWG",page_icon="&",layout="centered",initial_sidebar_state="auto",menu_items=None)
if "page" not in st.session_state:
    st.session_state.page = 0


placeholder = st.empty()
if st.session_state.page == 0:
    with placeholder.container():
        st.write("Click on Home to Log in")
        
        

elif st.session_state.page > 0:    
    with placeholder.container():
        st.title(":blue[GPP TREKKERS]")
        url="tkList.csv"
        dfn=pd.read_csv(url)
        st.table(dfn)
        st.write("---")
        st.write(":rainbow[Website created and maintained by MWG and AAG]")
