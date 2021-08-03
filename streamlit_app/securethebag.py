import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports
from multipage import MultiPage
from pages import home, data_story, about, form, resources # import your pages here

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Secure the Bag: Diagnosing Food Insecurity in California")
st.markdown("***")


# Add all your applications (pages) here
app.add_page("Home", home.app)
app.add_page("Food Security by the Numbers", data_story.app)
app.add_page("Food Security Diagnostic Quiz", form.app)
app.add_page("Additional Resources", resources.app)
app.add_page("About Us", about.app)



# The main app
logo = "https://lh3.googleusercontent.com/pw/AM-JKLVK3nJUmYf8VHU1vZ0uMQ_1wrLqrRh0zBk561yFvcOC4_geTjza7VEXBpdF2GvYx8Nn4xyKenKtMGJbrWdPybv_D_sNVRYpVDfOpqe0XzNJs34fbOzEy0cw-11hq_dqpCTvM0SV6vvVSG_6w_vwf54=w497-h275-no"
sidebar_logo = st.sidebar.image(logo)
app.run()
