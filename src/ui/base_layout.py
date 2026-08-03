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

def style_teacher_page():
    

    st.markdown(
        """
        <style>

        /*
           ATTENDX TEACHER DASHBOARD
           Theme:
           Cream  : #EFD6AC
           Green  : #183A37
           Plum   : #432534
           Black  : #1A0E14
           Orange : #C44900
       */


       

        @import url(
            'https://fonts.googleapis.com/css2?family=Fredoka:wght@300..700'
            '&family=Outfit:wght@100..900'
            '&family=Stalinist+One&display=swap'
        );


        .stApp {
            background: #EFD6AC !important;
        }

        .main {
            background: #EFD6AC !important;
        }

        .block-container {
            max-width: 1100px !important;

            padding-top: 2rem !important;
            padding-bottom: 3rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }


        #MainMenu,
        footer,
        header {
            visibility: hidden !important;
        }


     

        html,
        body,
        [class*="css"] {
            font-family: "Outfit", sans-serif;
        }

        p,
        label,
        span {
            font-family: "Outfit", sans-serif;
        }


       
       

        h1 {
            font-family: "Stalinist One", sans-serif !important;

            color: #432534 !important;

            font-size: 3rem !important;
            line-height: 1.15 !important;

            font-weight: 400 !important;

            margin-bottom: 1rem !important;
        }

        h2 {
            font-family: "Outfit", sans-serif !important;

            color: #432534 !important;

            font-weight: 700 !important;
        }

        h3 {
            font-family: "Outfit", sans-serif !important;

            color: #432534 !important;

            font-weight: 700 !important;
        }



        [data-testid="stDivider"] {
            border-top: 2px solid #432534 !important;

            opacity: 0.8;
        }




        button {
            font-family: "Outfit", sans-serif !important;

            border-radius: 1.5rem !important;

            border: none !important;

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease,
                background-color 0.2s ease !important;
        }


        /* Primary */

        button[kind="primary"] {
            background: #432534 !important;

            color: white !important;

            border: none !important;

            border-radius: 1.5rem !important;

            padding: 0.7rem 1.3rem !important;
        }


        /* Secondary */

        button[kind="secondary"] {
            background: #432534 !important;

            color: white !important;

            border: none !important;

            border-radius: 1.5rem !important;

            padding: 0.7rem 1.3rem !important;
        }


        /* Tertiary / black buttons */

        button[kind="tertiary"] {
            background: #1A0E14 !important;

            color: white !important;

            border: none !important;

            border-radius: 1.5rem !important;

            padding: 0.7rem 1.3rem !important;
        }


        /* Button hover */

        button:hover {
            transform: translateY(-2px) scale(1.02) !important;

            box-shadow:
                0 8px 20px rgba(67, 37, 52, 0.20) !important;
        }


        button:active {
            transform: scale(0.98) !important;
        }



        .stTextInput input,
        .stTextArea textarea {

            background: #183A37 !important;

            color: white !important;

            border: 2px solid transparent !important;

            border-radius: 1rem !important;

            font-family: "Outfit", sans-serif !important;
        }


        .stTextInput input::placeholder,
        .stTextArea textarea::placeholder {

            color: rgba(255,255,255,0.65) !important;
        }


        .stTextInput input:focus,
        .stTextArea textarea:focus {

            border-color: #C44900 !important;

            box-shadow: none !important;
        }



        div[data-baseweb="select"] > div {

            background: #1A0E14 !important;

            color: white !important;

            border: none !important;

            border-radius: 1rem !important;

            min-height: 48px !important;
        }


        div[data-baseweb="select"] span {

            color: white !important;

            font-family: "Outfit", sans-serif !important;
        }



        [data-testid="stFileUploader"] {

            background: rgba(255,255,255,0.35) !important;

            border: 2px dashed #432534 !important;

            border-radius: 1.5rem !important;

            padding: 1rem !important;
        }


        [data-testid="stFileUploader"] section {

            background: transparent !important;

            border: none !important;
        }



        [data-testid="stMetric"] {

            background: rgba(255,255,255,0.35) !important;

            border: 1px solid rgba(67,37,52,0.15) !important;

            border-radius: 1.5rem !important;

            padding: 1rem !important;
        }


        [data-testid="stMetricValue"] {

            color: #432534 !important;

            font-family: "Outfit", sans-serif !important;

            font-weight: 700 !important;
        }



        [data-testid="stDataFrame"] {

            border-radius: 1.5rem !important;

            overflow: hidden !important;

            border: 1px solid rgba(67,37,52,0.15) !important;
        }



        [data-testid="stAlert"] {

            border-radius: 1.25rem !important;

            font-family: "Outfit", sans-serif !important;
        }


        img {

            border-radius: 1.5rem !important;
        }



        .stApp div[data-testid="stColumn"] {

            background: transparent !important;

            border-radius: 1.5rem !important;
        }



        .attendance-section {

            background: rgba(255,255,255,0.32);

            border: 1px solid rgba(67,37,52,0.15);

            border-radius: 2rem;

            padding: 2rem;

            margin: 1.5rem 0;
        }


        .attendance-title {

            font-family: "Stalinist One", sans-serif;

            color: #432534;

            font-size: 2rem;

            margin-bottom: 1.5rem;
        }


      

        .teacher-nav {

            display: flex;

            justify-content: center;

            gap: 1rem;

            margin: 2rem 0;
        }


        .teacher-card {

            background: rgba(255,255,255,0.38);

            border: 1px solid rgba(67,37,52,0.12);

            border-radius: 2rem;

            padding: 1.8rem;

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease;
        }


        .teacher-card:hover {

            transform: translateY(-5px);

            box-shadow:
                0 15px 35px rgba(67,37,52,0.12);
        }


        .teacher-header {

            display: flex;

            align-items: center;

            justify-content: space-between;

            margin-bottom: 2rem;
        }


        .teacher-logo {

            font-family: "Stalinist One", sans-serif;

            color: #432534;

            font-size: 2.5rem;
        }


        .teacher-welcome {

            font-family: "Outfit", sans-serif;

            color: white;

            background: #432534;

            padding: 0.8rem 1.3rem;

            border-radius: 2rem;

            font-weight: 600;
        }



        ::-webkit-scrollbar {

            width: 8px;
        }


        ::-webkit-scrollbar-track {

            background: #EFD6AC;
        }


        ::-webkit-scrollbar-thumb {

            background: #432534;

            border-radius: 10px;
        }


        @media (max-width: 768px) {

            .block-container {

                padding-left: 1rem !important;

                padding-right: 1rem !important;
            }


            h1 {

                font-size: 2rem !important;
            }


            .attendance-section {

                padding: 1.2rem;
            }


            .teacher-header {

                flex-direction: column;

                gap: 1rem;

                align-items: flex-start;
            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )
