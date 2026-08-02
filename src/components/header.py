import streamlit as st
import base64

def header_home():
    with open("src/components/Logo-Photoroom.png", "rb") as f:
        img = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <div style="display:flex;justify-content:center;">
        <img src="data:image/png;base64,{img}" width="100">
    </div>

    <h1 style="text-align: center;">AttendX</h1>
    """, unsafe_allow_html=True)

def header_dashboard():
    with open("src/components/Logo.png", "rb") as f:
        img = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <div style="
        display:flex;
        justify-content:center;
        align-items:center;
        gap:10px;
        margin:0;
    ">
    <img src="data:image/png;base64,{img}"
             width="60"
             style="border-radius:16px;">

    <h1 style="
            margin:0;
            font-size:28px !important;
            font-weight:700;
            white-space:nowrap;
            line-height:1;
    ">
        AttendX
    </h1>
    </div>
    """, unsafe_allow_html=True)