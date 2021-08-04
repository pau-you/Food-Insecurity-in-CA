import streamlit as st
import streamlit.components.v1 as components
import os
import pandas as pd
import numpy as np
from PIL import Image


def app():

    dining = 'https://lh3.googleusercontent.com/pw/AM-JKLVsQmPFqihJNH3N5Jd5c8vPGmrZGRbHlqNtM01fHhV2xEwXOCxek5YIl65woads13EPvCAm_n_a-4iqIk24yswMqk6wFO-c_OLlnmMWt2cHT6Zn087lIKZrf4S_HT265sJ8qXz10ckVob_qQx7mVAs=w960-h641-no'
    st.image(dining, caption = 'Source: Pexels')

    st.success('_“Call me old-fashioned, but I think ending poverty and hunger on Earth is more important than colonizing Mars.“ - Robert Reich_')

    st.write("Welcome to Secure the Bag, a platform designed to better understand food security within California. Our Food Security by the Numbers page walks you through a closer look at historical and future trends in food security. Feel free to use our Food Security Diagnostic Quiz to gauge your current food security status. Lastly, our Resources page includes a variety of links to additional sources to help you gain access to food aid, benefits, etc.")

    st.write("To navigate the website and access the other pages, use the drop down menu on the left.")
