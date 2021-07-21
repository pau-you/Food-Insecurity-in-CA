import streamlit as st
import streamlit.components.v1 as components
import datetime
import pandas as pd
import numpy as np
from PIL import Image


def app():

    st.title("About Secure the Bag")
    st.header("Mission Statement")
    st.write("_Recognizing that individuals and communities have been marginalized on the basis of socioeconomic status, race/ethnicity, gender, sexuality, and location, we seek to improve food access by giving voice to those without._")

    st.header("Team Members")
    
    col1, col2, col3, col4 = st.beta_columns(4)
    with col1:
        josh_head = Image.open('./photos/IMG_8800 (2).jpg')
        st.image(josh_head)
        st.button("Josh")
    with col2:
        hannah_head = Image.open('./photos/Hannah_Headshot.png')
        st.image(hannah_head)
        st.button("Hannah")
    with col3:
        jeff_head = Image.open('./photos/Jeff_Head.png')
        st.image(jeff_head)
        st.button("Jeff")
    with col4:
        pauline_head = Image.open('./photos/Pauline_Headshot.png')
        st.image(pauline_head)
        st.button("Pauline")
