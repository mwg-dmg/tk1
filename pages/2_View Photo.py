import streamlit as st
import pandas as pd

st.set_page_config(page_title="MWG",page_icon="&",layout="centered",initial_sidebar_state="auto",menu_items=None)
url="tkphoto.csv"
df=pd.read_csv(url)

if "page" not in st.session_state:
    st.session_state.page = 1
if "page" not in st.session_state:
    st.session_state.page = 0
if "j" not in st.session_state:
    st.session_state.j = 0
if "status" not in st.session_state:
    st.session_state.status =0
if "text" not in st.session_state:
    st.session_state.text = ""
if "nflag" not in st.session_state:
    st.session_state.nflag = 0
def mainpage():
    st.session_state.page = 1
    st.session_state.status =1
def ij_next(i):
    i=i
    st.session_state.j +=1
    return(i,st.session_state.j)
def ij_pre(i):
    i=i
    st.session_state.j -=1
    return(i,st.session_state.j)
def get_ij_start(i):
    i=i
    st.session_state.j = 0
    return(i,st.session_state.j)
def read_data(i,j):
    df1=df[[df.columns[i]]]
    st.session_state.nflag=0      
    df1=df1.dropna()    
    jmax=((len(df1[[df1.columns[0]]]))-1)
    if j>jmax:
        j=j-1
        st.session_state.j -=1
        st.session_state.nflag=1
    if j<0:
        j=0
        st.session_state.j = 0
        st.session_state.pflag=1    
    return(df1[df1.columns[0]][j])

def view_next_photo():
    st.title(":blue[GPP TREKKERS]") 
    placeholder = st.empty()
    with placeholder.container():
                i_in=st.session_state.page-2
                list=[]
                list=ij_next(i_in)
                i=list[0]
                j=list[1]
                file=read_data(i,j)
                col1,col2=st.columns(2)
                with col1:
                    st.button("Prev Photo",on_click=view_pre_photo,disabled=(j==0))                    
                with col2:                    
                    st.button("Next Photo",on_click=view_next_photo,disabled=(st.session_state.nflag==1))                
                if file.endswith("mp4"):        
                    try:
                        video_file=open(file,"rb")
                        video_bytes=video_file.read()                    
                        st.video(video_bytes)
                    except:
                        st.write("Error in opening photo, please click on Next or Previous button")
                else:
                    try:
                        st.image(file)
                    except:
                        st.write("Error in opening photo, please click on Next or Previous button")
                st.write(st.session_state.text)
                st.button("Back to Main Page",on_click=mainpage,disabled=(st.session_state.page ==1))      

def view_pre_photo():
    st.title(":blue[GPP TREKKERS]") 
    placeholder = st.empty()
    with placeholder.container():
                i_in=st.session_state.page-2
                list=[]
                list=ij_pre(i_in)
                i=list[0]
                j=list[1]
                #st.write(i)
                #st.write(j)
                
                file=read_data(i,j)
                
                #st.write(file)
                col1,col2=st.columns(2)
                with col1:
                    st.button("Prev Photo",on_click=view_pre_photo,disabled=(j==0))                    
                with col2:                    
                    st.button("Next Photo",on_click=view_next_photo,disabled=(st.session_state.nflag==1))
                
                if file.endswith("mp4"):
                    try:
                        video_file=open(file,"rb")
                        video_bytes=video_file.read()                    
                        st.video(video_bytes)
                    except:
                        st.write("Error in opening photo, please click on Next or Previous button")
                else:
                    try:
                        st.image(file)
                    except:
                        st.write("Error in opening photo, please click on Next or Previous button")
                st.write(st.session_state.text)
                st.button("Back to Main Page",on_click=mainpage,disabled=(st.session_state.page ==1))
                
def view_photo():
    st.title(":blue[GPP TREKKERS]") 
    placeholder = st.empty()
    
    st.session_state.status =1
    with placeholder.container():
                i_in=st.session_state.page-2
                
                list=[]
                list=get_ij_start(i_in)
                i=list[0]
                j=list[1]
                file=read_data(i,j)
                col1,col2=st.columns(2)
                with col1:
                    st.button("Prev Photo",on_click=view_pre_photo,disabled=(j==0))                    
                with col2:                    
                    st.button("Next Photo",on_click=view_next_photo,disabled=(st.session_state.nflag==1))
                
                if file.endswith("mp4"):
                    try:
                        video_file=open(file,"rb")
                        video_bytes=video_file.read()                    
                        st.video(video_bytes)
                    except:
                        st.write("Error in opening photo, please click on Next or Previous button")
                else:
                    try:
                        st.image(file)
                    except:
                        st.write("Error in opening photo, please click on Next or Previous button")
                st.write(st.session_state.text)
                st.button("Back to Main Page",on_click=mainpage,disabled=(st.session_state.page ==1))
def Tn1():
    st.session_state.page=2
    st.session_state.text="1)Rajmachi"                
    view_photo()
def Tn2():
    st.session_state.page=3
    st.session_state.text="2)Korigad"                
    view_photo()
def Tn3():
    st.session_state.page=4
    st.session_state.text="3)Ghangad"                
    view_photo()
def Tn4():
    st.session_state.page=5
    st.session_state.text="4)Dharamveergad and Rehkuri"                
    view_photo()
def Tn5():
    st.session_state.page=6
    st.session_state.text="5)Nilkantheshwar"                
    view_photo()
def Tn6():
    st.session_state.page=7
    st.session_state.text="6)Tikona Fort"                
    view_photo()
def Tn7():
    st.session_state.page=8
    st.session_state.text="7)Lalwadi Waterfalls"                
    view_photo()
def Tn8():
    st.session_state.page=9
    st.session_state.text="8)Vetal Tekadi"                
    view_photo()
def Tn9():
    st.session_state.page=10
    st.session_state.text="9)Dhak  Bahiri"                
    view_photo()
def Tn10():
    st.session_state.page=11
    st.session_state.text="10)Tung Fort"                
    view_photo()
def Tn11():
    st.session_state.page=12
    st.session_state.text="11)Bhor and Bhatgar Dam"                
    view_photo()
def Tn12():
    st.session_state.page=13
    st.session_state.text="12)Hanuman Tekadi"                
    view_photo()
def Tn13():
    st.session_state.page=14
    st.session_state.text="13)Raireshwar Fort"                
    view_photo()
def Tn14():
    st.session_state.page=15
    st.session_state.text="14)Bhamchandra Caves"                
    view_photo()
def Tn15():
    st.session_state.page=16
    st.session_state.text="15)Khed-Shivapur"                
    view_photo()
def Tn16():
    st.session_state.page=17
    st.session_state.text="16)Railingi Pathar"                
    view_photo()
def Tn17():
    st.session_state.page=18
    st.session_state.text="17)Rohida Fort"                
    view_photo()
def Tn18():
    st.session_state.page=19
    st.session_state.text="18)K2S"                
    view_photo()
def Tn19():
    st.session_state.page=20
    st.session_state.text="19)Lingya Ghat"                
    view_photo()
def Tn20():
    st.session_state.page=21
    st.session_state.text="20)Hathi Matha"                
    view_photo()
def Tn21():
    st.session_state.page=22
    st.session_state.text="21)Video of all Treks"                
    view_photo()       



placeholder = st.empty()
if st.session_state.page == 0:
    with placeholder.container():
        st.write("Click on Home to Log in")
        st.write("If you want to login again Click on Home to Log in")
elif st.session_state.page > 0:    
    with placeholder.container():
        if (st.session_state.page == 1):
            
                st.title(":blue[GPP TREKKERS]")  

                st.button("1)Rajmachi Fort -25 Nov 2015",on_click=Tn1) 
                st.button('2)Korigad -20 oct 2017',on_click=Tn2)
                st.button('3)Ghangad -18 June 2017',on_click=Tn3)
                st.button('4)Dharmaveergad and Rehkuri -9 Sept 2017',on_click=Tn4)
                st.button('5)Nilkantheshwar- 28 Oct 2017',on_click=Tn5)
                st.button('6)Tikona Fort - 29 Dec 2017',on_click=Tn6)
                st.button('7)Lalwadi Waterfalls-28 July 2018',on_click=Tn7)
                st.button('8)Vetal Tekadi- 26 Jan 2019',on_click=Tn8)
                st.button('9)Dhak  Bahiri- 12 Feb 2019',on_click=Tn9)
                st.button('10)Tung Fort- 10 Mar 2019',on_click=Tn10)
                st.button('11)Bhor and Bhatgar Dam- 12 Aug 2019',on_click=Tn11)
                st.button('12)Hanuman Tekadi- 15 Aug 2019',on_click=Tn12)
                st.button('13)Raireshwar Fort- 2 Oct 2019',on_click=Tn13)
                st.button('14)Bhamchandra Caves – 10 Oct 2020',on_click=Tn14)
                st.button('15)Khed-Shivapur- 28 Nov 2021',on_click=Tn15)
                st.button('16)Railingi Pathar- 8-9 Jan 2022',on_click=Tn16)
                st.button('17)Rohida Fort- 30 Oct 2022',on_click=Tn17)
                st.button('18)K2S-  5 Mar 2023',on_click=Tn18)
                st.button('19)Lingya Ghat- 17 Jul 2023',on_click=Tn19)                
                st.button('20)Hathi Matha-14 Dec 2024',on_click=Tn20)
                st.button('21)Video of all Treks',on_click=Tn21)
                

                st.write("---")
                st.write(":rainbow[Website created and maintained by MWG and AAG]")
