import streamlit as st
import streamlit.components.v1 as components
import datetime
import pandas as pd
import numpy as np
from PIL import Image


def app():

    st.title("About Secure the Bag")
    st.write("We're a group of 5th Year MIDS students interested in the intersection of data science and social good. We decided to embark on this project due to the limited research on food security, as much of the data is often aggregated and, thus, obscures the lived realities of the food insecure population of California. We hope our project provides the evidence to encourage more action on food aid and policy.")
    st.write('Our team name and project follows the phrase "secure the bag," in the hopes that our work will help to achieve the goal of closing the gap of food insecurity. It is also a play on words on helping "secure" grocery "bags" for individuals who are often lacking food resources. We hope after viewing our website you will also help us in this effort to Secure the Bag!')

    st.header("Mission Statement") # Header
    st.write("_Recognizing that individuals and communities have been marginalized on the basis of socioeconomic status, race/ethnicity, gender, sexuality, and location, we seek to improve food access by giving voice to those without._")

    st.header("Team Members") # Header
    col1, col2, col3, col4 = st.beta_columns(4)
    with col1:
        hannah_link = '''<a href="https://www.linkedin.com/in/hgchoi/" target="_blank">
    <img src="https://lh3.googleusercontent.com/pw/AM-JKLW2uRCacCTZVOHoAmYJJ1vLV_uCxWaEmy4Wu6PSK280IKwOtwA2tuxenBVq5JUq2POfnL2ErxdvUzbanlKNUcGApuMK3A_D-UhU-CWIbGR575RUUajz_r7m70HrW5f_TeM53ynmh8k2LlSuzf0MQeJU=s844-no" title="Click to visit LinkedIn" alt="Hannah Choi" width="100%"/>
</a>'''
        st.markdown(hannah_link, unsafe_allow_html=True)
        st.subheader("Hannah Choi")

    with col2:
        josh_link = '''<a href="https://www.linkedin.com/in/jtlin818/" target="_blank">
    <img src="https://lh3.googleusercontent.com/pw/AM-JKLVkpPG4yJSFjnN-jZo20L0j_gi3YMeWXLt4dPz9eEHrqa4Hdpx8ACSMnWeRwWnbImvKeU5_MZyyzwnvZzh9yuFXw37KBu3ZVocRS2DQSu69cwoIe5Me9osypSJCS_d25dTBz-tKOCzi9jg8qOehwOWY=s944-no" title="Click to visit LinkedIn" alt="Josh Lin" width="100%"/>
</a>'''
        st.markdown(josh_link, unsafe_allow_html=True)
        st.subheader("Joshua Lin")

    with col3:
        pauline_link = '''<a href="https://www.linkedin.com/in/pauline-yue/" target="_blank">
    <img src="https://lh3.googleusercontent.com/pw/AM-JKLW4wkasjbVoaiQ6kEV9bm2-W9LfkNcmol1LquW6u5DWQ-MqUxf2iaiVB6OzJrn3ppG5jXaTUeRgnSbW8EnyRxUcpA2cIy8X8TACW6g1tC8ZbBvBay6dXnEojijlbG9c7cSI4iYzXZ5kQHWVzFaUmjgV=s520-no" title="Click to visit LinkedIn" alt="Pauline Yue" width="100%"/>
</a>'''
        st.markdown(pauline_link, unsafe_allow_html=True)
        st.subheader("Pauline Yue")

    with col4:
        jeff_link = '''<a href="www.linkedin.com/in/jeffry-zheng" target="_blank">
    <img src="https://lh3.googleusercontent.com/pw/AM-JKLUWeiylm9xww74KFuCfXyQeotkzwaLjbsdnNL-BS9ZgmY8EdCOVy_cHCh0R9WOAuIUpNu-KGhJ3jy3edJXK0nC_mZwPD5siAV4Ksig2B6YmNauYw-d98kxLrwqmUAPUyfU7s7s1GYuZCQpgPVyFL8at=s439-no" title="Click to visit LinkedIn" alt="Jeff Zheng" width="100%"/>
</a>'''
        st.markdown(jeff_link, unsafe_allow_html=True)
        st.subheader("Jeff Zheng")

    st.write(" ")
    st.header("Learn More About Our Work") # Header
    with st.beta_expander("Github Repository for Secure the Bag"):
        col5, col6 = st.beta_columns((5,1))
        col5.write("Click the link to view the code we implemented to build out the Secure the Bag platform.")
        col5.write("https://github.com/secure-the-bag-capstone/project")
        with col6:
            git_link = '''<a href="https://github.com/secure-the-bag-capstone/project" target="_blank">
        <img src="https://lh3.googleusercontent.com/pw/AM-JKLXTT1Uj-W8X8kuZEFHPAreupHSIheNhSdusbaQdjyF_YOAl7OsmG0tbn_JFlw-l5Pi_s2-fA0Xfrmo35xVLXxG1OaqE9SijTAaUGKcWqWcmFsao_EKrMRwux6NIwKuQhpyWxa-h-dUcyd3fqR7c6ttd=s225-no" title="Click to visit Github" alt="Github" width="80%"/>
    </a>'''
            st.markdown(git_link, unsafe_allow_html=True)

    with st.beta_expander("Access the CHIS Data"):
        col7, col8 = st.beta_columns((5,1))
        col7.write("Click the link to visit the California Health Interview Survey webpage. On this page, you can access the CHIS data that we used to conduct our analyses and build our diagnostic models.")
        col7.write("https://healthpolicy.ucla.edu/chis/Pages/default.aspx")
        with col8:
            chis_link = '''<a href="https://healthpolicy.ucla.edu/chis/Pages/default.aspx" target="_blank">
        <img src="https://lh3.googleusercontent.com/pw/AM-JKLV71LWqdztA2egoZT-b8dqO-nOoSfC6mh8RDDR9H7c7ECk52tZQz42gMtpb8FZ4Zv3gw4i7B-0y4eJUPWaQBwD5rHvDo86gR0qULZA85vycIa4Ozpydx39M0ClgSNeIiiPQxe1tpNyDuKAlaHtTHwZt=s166-no" title="Click to visit CHIS" alt="CHIS" width="95%"/>
    </a>'''
            st.markdown(chis_link, unsafe_allow_html=True)
