import streamlit as st
import streamlit.components.v1 as components
import datetime
import pandas as pd
import numpy as np

def app():

    st.title("Food Security Diagnostic Quiz")
    st.write("Here, you can answer a few questions to assess your predicted food security situation.")

    st.info('This is a purely informational message')

    user_id = st.text_input("ID", value="Your ID", max_chars=7)
    info = st.text_area("Share some information about you", "Put information here",
                        help='You can write about your hobbies or family')
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
    birth_date = st.date_input("Date of Birth", min_value=datetime.date(1921, 1, 1),
                               max_value=datetime.date(2003, 12, 31))
    smoke = st.checkbox("Do you smoke?")
    genre = st.radio("Which movie genre do you like?",
                     options=['horror', 'adventure', 'romantic'])
    weight = st.slider("Choose your weight", min_value=40., max_value=150., step=0.5)
    physical_form = st.selectbox("Select level of your physical condition",
                                 options=["Bad", "Normal", "Good"])
    colors = st.multiselect('What are your favorite colors',
                            options=['Green', 'Yellow', 'Red', 'Blue', 'Pink'])
    image = st.file_uploader("Upload your photo", type=['jpg', 'png'])

    col1, col2 = st.beta_columns(2)
    with col1:
        st.image("https://static.streamlit.io/examples/cat.jpg", width=300)
        st.button("Like cats")
    with col2:
        st.image("https://static.streamlit.io/examples/dog.jpg", width=355)
        st.button("Like dogs")

    submit = st.button("Submit")

    if submit:
        st.write("You submitted the form")


    st.markdown("## Party time!")
    st.write("Yay! You're done with this tutorial of Streamlit. Click below to celebrate.")
    btn = st.button("Celebrate!")
    if btn:
        st.balloons()
