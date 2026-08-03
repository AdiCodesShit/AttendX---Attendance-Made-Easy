import streamlit as st
from src.ui.base_layout import style_base_layout
from src.ui.base_layout import style_background_home
from src.components.header import header_home
from src.components.footers import footer_home
def home_screen():

    header_home()
    style_background_home()
    style_base_layout()

    st.markdown(f"""
    <h2 style="
        text-align: center;
        font-family: 'Poppins', 'Segoe UI', sans-serif;
        font-weight: 600;
        font-size: 2rem;
        line-height: 1.15;
        color: #F5F0E6;
        letter-spacing: 0.3px;
        max-width: 700px;
        margin: 0 auto 2rem auto;
        opacity: 0.95;
    ">
        Face And Voice Assisted<br>
        <span style="color: #E8985E;">Attendance System</span>
    </h2>
    """, unsafe_allow_html=True)
    

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("I'm a Teacher")
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
        st.button("Teacher Portal",icon=":material/arrow_outward:", icon_position="right",on_click=lambda: st.session_state.update(login_type="teacher"))
    with col2:
        st.header("I'm a Student")
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
        st.button("Student Portal", icon=":material/arrow_outward:", icon_position="right", on_click=lambda: st.session_state.update(login_type="student"))
    footer_home()
