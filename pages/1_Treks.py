import streamlit as st
import pandas as pd
st.set_page_config(page_title="MWG",page_icon="&",layout="centered",initial_sidebar_state="auto",menu_items=None)
if "page" not in st.session_state:
    st.session_state.page = 1


placeholder = st.empty()
if st.session_state.page == 0:
    with placeholder.container():
        st.write("You are logged out.You can  close the Tab")
        st.write("If you want to login again Click on Home to Log in")
        
        

elif st.session_state.page > 0: 
    st.session_state.page =1
    with placeholder.container():
        st.title(":blue[GPP TREKKERS]")
        url="tkList.csv"
        dfn=pd.read_csv(url)
        st.table(dfn)
        st.write("---")
        st.write(":rainbow[Website created and maintained by MWG and AAG]")
