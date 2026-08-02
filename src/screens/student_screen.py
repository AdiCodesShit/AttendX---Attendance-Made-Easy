import streamlit as st
from src.ui.base_layout import style_background_dashboard
from src.ui.base_layout import style_base_layout_dashboard
from src.components.header import header_dashboard
from src.components.footers import footer_dashboard
import numpy as np
from PIL import Image
from src.pipelines.face_pipeline import predict_attendance
from src.database.db import get_all_students, create_student
from src.pipelines.face_pipeline import get_face_embeddings
from src.pipelines.voice_pipeline import get_voice_embedding
import time
from src.pipelines.face_pipeline import train_classifier
from src.components.dialog_enroll import enroll_dialog
from src.database.db import unenroll_student_to_subject, get_student_attendance,get_student_subjects,get_all_students
from src.components.subject_card import subject_card    

def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"""Welcome, {student_data['name']} """)
        if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data 
            st.rerun()


    st.space()

    c1, c2 =st.columns(2)
    with c1:
        st.header('Your Enrolled Subjects')
    with c2:
        if st.button('Enroll in Subject', type='primary', width='stretch'):
            enroll_dialog()


    st.markdown("""
        <hr style="
            border: none;
            height: 2px;
            background-color: #5A2D4D;
            margin: 20px 0;
        ">
        """, unsafe_allow_html=True)


    with st.spinner('Loading your enrolled subjects..'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}

    for log in logs:
        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid] = {"total":0, "attended": 0}

        stats_map[sid]['total'] +=1

        if log.get('is_present'):
            stats_map[sid]['attended'] += 1


    cols = st.columns(2)
    for i, sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid = sub['subject_id']


        stats = stats_map.get(sid,{"total":0, "attended": 0} )
        def unenroll_button():
                if st.button("Unenroll from this course", type='tertiary', width='stretch', icon=':material/delete_forever:'):
                    unenroll_student_to_subject(student_id, sid)
                    st.toast(f'Unenrolled from {sub['name']} successfully!')
                    st.rerun()

        with cols[i % 2]:

            subject_card(
                name = sub['name'],
                code =sub['subject_code'],
                section = sub['section'],
                stats = [
                    ('📅', 'Total', stats['total']),
                    ('✅', 'Attended', stats['attended']),
                ],
                footer_callback=unenroll_button
            )
    footer_dashboard()


def student_screen():
    style_background_dashboard()
    style_base_layout_dashboard()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    col1, col2 = st.columns(2, gap="xxlarge", vertical_alignment="center")

    with col1:
        header_dashboard()
    with col2:
        st.button("Go Back To Home", key="go_back", type="primary", icon=":material/arrow_back:", icon_position="left", on_click=lambda: st.session_state.update(login_type=None))

    st.header("Login Using Face Id", text_alignment="center")

    show_registration =False
    
    photo_source = st.camera_input("Position Your Face In Center")
    
    if photo_source:
        img = np.array(Image.open(photo_source))

        with st.spinner("AI Is Scanning..."):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning("No Faces Found!")
            if num_faces > 1:
                st.warning("Multiple Faces Found!")
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id'] == student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = "student"
                        st.session_state.student_data = student
                        st.toast(f"Welcome Back {student['name']}")
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info("Face Not Recognized! If You Are A New Student, Please Register First.")
                    show_registration = True

    if show_registration:
        with st.container(border=True):
            st.header("Register New Profile.")
            new_name = st.text_input("Enter Your Name", placeholder= "Amit Kasar")

            st.subheader("Optional : Voice Enrollment")
            st.info("Enroll For Voice Only Attendence.")

            audio_data = None

            try:
                audio_data = st.audio_input("Record Your Voice Saying \'I am Present, My Name Is Amit.\'")
            except Exception as e:
                st.error("Audio Data Failed!")

            if st.button("Create Account", type="primary"):
                if new_name:
                    with st.spinner("Creating Profile..."):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name ,face_embedding = face_emb ,voice_embedding = voice_emb)
                            if response_data:
                                train_classifier()

                                st.session_state.is_logged_in = True
                                st.session_state.user_role = "student"
                                st.session_state.student_data = response_data[0]
                                st.toast(f"Profile Created! Hi {new_name}.")
                                time.sleep(1)
                                st.rerun()   
                        else:
                            st.error("Couldn't Capture Your Facial Features, Please Try Again")                             
                else:
                    st.warning("Please Enter Your Name.")

    footer_dashboard()