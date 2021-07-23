import streamlit as st
import streamlit.components.v1 as components
import datetime
import pandas as pd
import numpy as np

def app():

    st.title("Additional Resources")

    st.header("Resources for California:")

    st.write("- [Get CalFresh] (https://www.getcalfresh.org/)")
    st.write("- [CA Food Banks] (https://www.cafoodbanks.org/)")
    st.write("- [CA Local Food Bank Locator] (https://www.cafoodbanks.org/our-members/)")
    st.write("- [CA Food Banks Covid-19 Resources] (https://www.cafoodbanks.org/covid-19-resources/)")
    st.write("- [CA Emergency Food Assistance Program] (https://www.cdss.ca.gov/emergency-food)")
    st.write("- [211 Food Finder Map] (https://foodfinder.211la.org/-119.050952,33.735518,-117.636654,34.702715/project?layers=20%2C22%2C18%2C19%2C21)")
    st.write("- [About CalFresh Guide in Simplified Chinese] (https://www.freshapproach.org/wp-content/uploads/2019/07/2019-Calfresh-FMs-Contra-Costa-Simplified-Chinese-Mandarin.pdf)")
    st.write("- [Hmong CalFresh Brochure] (https://www.cdss.ca.gov/foodstamps/res/pdf/CalFresh_GenMrkt_Bro_Hmong.pdf)")
    st.write("- [Spanish CalFresh Brochure] (https://211sandiego.org/wp-content/uploads/2016/10/CalFreshBrochureSpan.pdf)")

    st.header("Resources by County:")

    st.write("- [LA County Food Security Resources Page] (http://publichealth.lacounty.gov/nut/healthcare-food-access.htm)")
    st.write("- [Sacramento Asian Resources Inc. Workshops] (https://asianresources.org/additional-ari-services)")
    st.write("- [Orange County Food Assistance Resources] (https://www.capoc.org/resources/)")
    st.write("- [Foodbank of SoCal] (https://www.foodbankofsocal.org/services/food-distribution/)")
    st.write("- [AAPI Forward Movement Food Roots Campaign] (https://www.foodroots.co/)")
    st.write("- [Alameda County Community Food Bank] (https://www.accfb.org/)")
    st.write("- [SF Marin Food Bank] (https://www.sfmfoodbank.org/)")
    st.write("- [Alameda County Social Services Food and Health Guideline] (https://www.alamedacountysocialservices.org/our-services/Health-and-Food/index)")
