import streamlit as st
import streamlit.components.v1 as components
import datetime
import pandas as pd
import numpy as np

def app():

    st.title("Food Security Diagnostic Quiz")
    st.write("Here, you can answer a few questions to assess your predicted food security situation.")

    user_id = st.text_input("ID", value="Your ID", max_chars=7)
    info = st.text_area("Share some information about you", "Put information here",
                        help='You can write about your hobbies or family')
    age = st.number_input("Age", min_value=18, max_value=100, step=1)

    smoke = st.checkbox("Do you smoke?")
    genre = st.radio("Which movie genre do you like?",
                     options=['horror', 'adventure', 'romantic'])
    weight = st.slider("Choose your weight", min_value=40., max_value=150., step=0.5)
    physical_form = st.selectbox("Select level of your physical condition",
                                 options=["Bad", "Normal", "Good"])
    colors = st.multiselect('What are your favorite colors',
                            options=['Green', 'Yellow', 'Red', 'Blue', 'Pink'])

    submit = st.button("Submit")

    if submit:
        st.write("You submitted the form")


    st.markdown("## Party time!")
    st.write("Yay! You're done with this tutorial of Streamlit. Click below to celebrate.")
    btn = st.button("Celebrate!")
    if btn:
        st.balloons()
