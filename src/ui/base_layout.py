import streamlit as st

def style_background_home():
    st.markdown('''
    <style>
                .stApp{
                background: #183A37 !important;}

                .stApp div[data-testid="stColumn"]{
                background: #EFD6AC !important;
                padding: 2.5rem 2rem !important;
                border-radius: 5rem !important;
                }
    </style>
        ''', unsafe_allow_html=True)
    
def style_background_dashboard():
    st.markdown('''
    <style>
                .stApp{
                background: #EFD6AC !important;
                }

                .stApp div[data-testid="stColumn"]{
                background: #EFD6AC !important;
                padding: 2.5rem 2rem !important;
                border-radius: 5rem !important;
                }
                
    </style>
        ''', unsafe_allow_html=True)
    

def style_base_layout():
    st.markdown(
        '''

        <style>

        /*Header Font*/
        @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300..700&family=Stack+Sans+Notch:wght@200..700&family=Stalinist+One&display=swap');
        
        /*Body Font*/
        @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300..700&family=Outfit:wght@100..900&family=Stack+Sans+Notch:wght@200..700&family=Stalinist+One&display=swap');

        #MainMenu,footer,header {visibility: hidden;}

        [data-testid="stDivider"] {
            border-top: 2px solid black !important; /* Your color */
        }


        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 1rem;
            padding-left: 5rem;
            padding-right: 5rem;
    
        }

        h1{
        font-family: "Stalinist One", sans-serif !important;
        font-weight: 400 !important;
        font-style: normal;
        font-size: 3rem !important;
        line-height: 1.2 !important;
        margin-bottom: 1rem !important;
        color: #C44900!important;
        }

        h2{ 
        font-family: "Outfit", sans-serif !important;
        margin-top: 0rem !important;
        margin-bottom: 0.5rem !important;
        }

        button[kind="secondary"] {
        border-radius: 1.5rem !important;
        padding: 10px 20px !important;
        background-color: #432534 !important;
        border: none !important;
        transition: transform 0.25s ease-in-out !important;
        }

        button[kind="tertiary"]{
                        border-radius: 1.5rem !important;
                        background-color: #1A0E14 !important;
                        color: white !important;
                        padding: 10px 20px !important;
                        border: none !important;
                        transition: transform 0.25s ease-in-out !important;
                        }

        button:hover{
        transform: scale(1.05) !important;}
        </style>

        ''',
        unsafe_allow_html=True
    )

def style_base_layout_dashboard():
    st.markdown(
        '''

        <style>

        /*Header Font*/
        @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300..700&family=Stack+Sans+Notch:wght@200..700&family=Stalinist+One&display=swap');
        
        /*Body Font*/
        @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300..700&family=Outfit:wght@100..900&family=Stack+Sans+Notch:wght@200..700&family=Stalinist+One&display=swap');

        #MainMenu,footer,header {visibility: hidden;}

        .stTextInput > div > div > input {
            background-color: #183A37 !important;
            color: white; !important;
        }

        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 1rem;
            
        }

        h1{
        font-family: "Stalinist One", sans-serif !important;
        font-weight: 400 !important;
        font-style: normal;
        font-size: 3rem !important;
        line-height: 1.2 !important;
        margin-bottom: 1rem !important;
        color: #432534 !important;
        }

        h2{
        font-family: "Outfit", sans-serif !important;
        color: #432534 !important;
        }

        button[kind="primary"] {
        border-radius: 1.5rem !important;
        padding: 10px 20px !important;
        background-color: #432534 !important;
        border: none !important;
        transition: transform 0.25s ease-in-out !important;
        }

        button:hover{
        transform: scale(1.05) !important;}

        button[kind="secondary"] {
        border-radius: 1.5rem !important;
        padding: 10px 20px !important;
        background-color: #432534 !important;
        border: none !important;
        transition: transform 0.25s ease-in-out !important;
        }
        
        button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: #1A0E14 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }


        
        </style>

        ''',
        unsafe_allow_html=True
    )