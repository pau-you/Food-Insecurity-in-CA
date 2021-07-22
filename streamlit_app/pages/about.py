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
        josh_head = "https://lh3.googleusercontent.com/pw/AM-JKLUuuHZ1-v2E_yXtZg-H9wY_HDm42K-Cyo1OMWBdh41xGNvKIp6t5c15uqeqTtuIy9C_tP9tsRhlhSAge4EFDC9P4zrcLaKvstV8QyDnWtEaQh4sRMvT3hBeI--P5VTfGkiCVISbejuWfY9q2CTbWrc=s944-no"
        st.image(josh_head)
        st.button("Josh")
    with col2:
        hannah_head = "https://lh3.googleusercontent.com/pw/AM-JKLVZ3o72EHS6ft_z8q029J7brY0w3ICwle2eP8jOSd5Ali9MKzq0E1JUKJdAThQXA-fKhkbJZZPw8qR6hYMEKgpKUDftDUzJ5gJamM7yNZ1NtLoLJo2N6bDx5bvIP0wsfqq0wiW6iq4ky5LRRX5rihY=w884-h844-no"
        st.image(hannah_head)
        st.button("Hannah")
    with col3:
        jeff_head = "https://lh3.googleusercontent.com/pw/AM-JKLUB1fq0an9MiQmLFh6L1VxYrBmY1Ih9uxH5HR8alvdWyu6-lr0Z4y5R3ybf_qw390HAbo6kIUouovRPQoQLDlV2GbxbA-UZmfpZ5kTi60kynTTySxsr2LflHkX5epbfhn2qJ41Kjpr6gNVol4N69iA=w473-h439-no"
        st.image(jeff_head)
        st.button("Jeff")
    with col4:
        pauline_head = "https://lh3.googleusercontent.com/pw/AM-JKLVZp45v2_nj6gBgHK12ps3MP4Mo_d8fgs-HYGnQrlLurZZ8wDwrhCAtE7KDNhzE3PytJ_XIw6pdhwrb6ib3Ss1zIa8kBjdRbb9NfObhYUJnCgteO78GQI7TSnn6DllVfCDNkNqv4kyIkNPh_p-0QO4=w600-h520-no"
        st.image(pauline_head)
        st.button("Pauline")
