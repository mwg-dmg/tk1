import streamlit as st
import pandas as pd
st.set_page_config(page_title="MWG",page_icon="&",layout="centered",initial_sidebar_state="auto",menu_items=None)



if "page" not in st.session_state:
    st.session_state.page = 0





def lgin():
    if login=="gpptk" :
        if password=="gpptk123":
            st.session_state.one = ""
            st.session_state.two = ""
            #st.write("Login successful")
            st.session_state.page = 1         
            
    else:
            st.write("Wrong login name or password, Try again")
            st.session_state.one = ""
            st.session_state.two = ""
def Lout():
    st.session_state.page=0
    st.session_state.status =0

         
placeholder = st.empty()
if st.session_state.page == 0:
    with placeholder.container():
        st.title(":blue[GPP TREKKERS]")  
        login=st.text_input('Login Name',key="one",placeholder="Login Name")
        password=st.text_input('Password',key="two",placeholder="Password")
        st.button("Submit",key=None,on_click=lgin)
        st.write("Key in the login name and password, do not use auto words")
elif st.session_state.page > 0:
    
    with placeholder.container():
            st.session_state.page = 1   
            st.image("x1.jpg")
            st.write(
                    """
                        Trekking is an exhilarating experience that offers breath taking
                        views and sense of accomplishment. We have done lot of trekking
                        together. It is a great bonding experience. We enjoyed all the
                        treks and it helped in relaxing our mind every time.
                        The energy continued to be with us for many days after the trek.
                        Trekking leaves an inedible mark on your heart and soul.
                        These treks have created life long memories.
                        But now these memories are fading away.
                        So let us cherish these moments of time we spent together by
                        compiling the photos and videos of our treks. 
                        So go ahead!                        
                        
                    """
                    )
            st.write("""
                        And... yes... if you have any exclusive
                        photo or video of our trek please do not
                        forget to send it to MWG or AAG on Whatsapp.
                    """
                     )
            st.write("Enjoy!!")
            st.write("To open or close side bar click on'>' or 'x'  on top left corner")

        
            st.write("---")
            st.write(":rainbow[Website created and maintained by MWG and AAG]")

           

            
            
        
            

                
        
