import streamlit as st
import streamlit.components.v1 as components
import os
import pandas as pd
import numpy as np
from PIL import Image

def app():
    path = os.path.dirname(__file__)
    st.write(path)
    dining = Image.open('./photos/pexels-august-de-richelieu-4262173.jpg')
    st.image(dining)
    st.markdown('_“In this country that grows more food than any other nation on this earth, it is unthinkable that any child should go hungry.”  - Sela Ward_')
    st.write("Welcome to Secure the Bag, a platform designed to better understand food security within California. Our Data Story page walks you through a closer look at historical and future trends in food security. Feel free to use our Food Security Diagnostic Quiz to gauge your current food security status. Lastly, our resources page includes a variety of links to additional sources to help you gain access to food aid, benefits, etc.")
    st.write("To navigate the website and access the other pages, use the drop down menu on the left.")
