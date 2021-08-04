import streamlit as st
import streamlit.components.v1 as components
import datetime
import pandas as pd
import numpy as np
from PIL import Image


def app():

    st.title("About Secure the Bag")
    st.write("We're a group of 5th Year MIDS students interested in the intersection of data science and social good. We decided to embark on this project due to the limited research on food security, as much of the data is often aggregated and, thus, obscures the lived realities of the food insecure population of California. We hope our project provides the evidence to encourage more action on food aid and policy.")

    st.header("Mission Statement")
    st.write("_Recognizing that individuals and communities have been marginalized on the basis of socioeconomic status, race/ethnicity, gender, sexuality, and location, we seek to improve food access by giving voice to those without._")

    st.header("Team Members")

    col1, col2, col3, col4 = st.beta_columns(4)
    with col1:
        josh_link = '''<a href="https://www.linkedin.com/in/jtlin818/" target="_blank">
    <img src="https://lh3.googleusercontent.com/pw/AM-JKLVkpPG4yJSFjnN-jZo20L0j_gi3YMeWXLt4dPz9eEHrqa4Hdpx8ACSMnWeRwWnbImvKeU5_MZyyzwnvZzh9yuFXw37KBu3ZVocRS2DQSu69cwoIe5Me9osypSJCS_d25dTBz-tKOCzi9jg8qOehwOWY=s944-no" title="Click to visit LinkedIn" alt="Josh Lin" width="100%"/>
</a>'''
        st.markdown(josh_link, unsafe_allow_html=True)
        st.subheader("Josh Lin")

    with col2:
        hannah_link = '''<a href="https://www.linkedin.com/in/hgchoi/" target="_blank">
    <img src="https://lh3.googleusercontent.com/pw/AM-JKLW2uRCacCTZVOHoAmYJJ1vLV_uCxWaEmy4Wu6PSK280IKwOtwA2tuxenBVq5JUq2POfnL2ErxdvUzbanlKNUcGApuMK3A_D-UhU-CWIbGR575RUUajz_r7m70HrW5f_TeM53ynmh8k2LlSuzf0MQeJU=s844-no" title="Click to visit LinkedIn" alt="Hannah Choi" width="100%"/>
</a>'''
        st.markdown(hannah_link, unsafe_allow_html=True)
        st.subheader("Hannah Choi")

    with col3:
        jeff_link = '''<a href="www.linkedin.com/in/jeffry-zheng" target="_blank">
    <img src="https://lh3.googleusercontent.com/pw/AM-JKLUWeiylm9xww74KFuCfXyQeotkzwaLjbsdnNL-BS9ZgmY8EdCOVy_cHCh0R9WOAuIUpNu-KGhJ3jy3edJXK0nC_mZwPD5siAV4Ksig2B6YmNauYw-d98kxLrwqmUAPUyfU7s7s1GYuZCQpgPVyFL8at=s439-no" title="Click to visit LinkedIn" alt="Jeff Zheng" width="100%"/>
</a>'''
        st.markdown(jeff_link, unsafe_allow_html=True)
        st.subheader("Jeff Zheng")

    with col4:
        pauline_link = '''<a href="https://www.linkedin.com/in/pauline-yue/" target="_blank">
    <img src="https://lh3.googleusercontent.com/pw/AM-JKLW4wkasjbVoaiQ6kEV9bm2-W9LfkNcmol1LquW6u5DWQ-MqUxf2iaiVB6OzJrn3ppG5jXaTUeRgnSbW8EnyRxUcpA2cIy8X8TACW6g1tC8ZbBvBay6dXnEojijlbG9c7cSI4iYzXZ5kQHWVzFaUmjgV=s520-no" title="Click to visit LinkedIn" alt="Pauline Yue" width="100%"/>
</a>'''
        st.markdown(pauline_link, unsafe_allow_html=True)
        st.subheader("Pauline Yue")
