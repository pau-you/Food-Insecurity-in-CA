import streamlit as st
import streamlit.components.v1 as components
import datetime
import pandas as pd
import numpy as np

def app():

    st.title("Additional Resources")
    grocery_header = "https://lh3.googleusercontent.com/pw/AM-JKLXObxujfRBnfv6Y40oIbgIdBTZ_ojJmokUsesa0RVaqOHFDrrP-o-xfzJqXSEIMoNhKGWkpuWH7FTFPt3Q7LRFGE3BJkI2QkIrnWqR5aVFtCDpAnzFcZyDylJWUXj69_uKT35zSnK5jywqmxb74-84=w790-h220-no"
    st.image(grocery_header)

    st.header("Resources for California:") # Resources for California
    st.write("")

    with st.beta_expander("Apply for California Food Stamps Online"):
        st.write("GetCalFresh can help you apply for California Food Stamps, also known as CalFresh, SNAP, Food Assistance, or EBT, in as little as ten minutes.")
        st.write("https://www.getcalfresh.org/")

    with st.beta_expander("California Association of Food Banks"):
        st.write("We lead the collective effort to end hunger in California")
        st.write("https://www.cafoodbanks.org/")

    with st.beta_expander("CA Local Food Bank Locator"):
        st.write("Find a Local Food Bank")
        st.write("https://www.cafoodbanks.org/our-members/")

    with st.beta_expander("CA Food Banks Covid-19 Resources"):
        st.write("Here is a list of California Association of Food Banks’ resources specifically for the COVID-19 pandemic.")
        st.write("https://www.cafoodbanks.org/covid-19-resources/")

    with st.beta_expander("Emergency Food Assistance Program (EFAP)"):
        st.write("The Emergency Food Assistance Program (EFAP) is a Federal program that helps supplement the diets of low-income Americans, including elderly people, by providing them with emergency food assistance at no cost.")
        st.write("https://www.cdss.ca.gov/emergency-food")

    with st.beta_expander("About CalFresh Guide in Simplified Chinese (CalFresh 册子)"):
        st.write("在何处以及如何使用CalFresh在当地农贸市场购买新鲜及健康的农场食品")
        st.write("https://www.freshapproach.org/wp-content/uploads/2019/07/2019-Calfresh-FMs-Contra-Costa-Simplified-Chinese-Mandarin.pdf")

    with st.beta_expander("Hmong CalFresh Brochure (Hmong CalFresh Ntawv nthuav qhia)"):
        st.write("Nyiaj CalFresh yuav pab tau koj thiab koj tsev neeg.")
        st.write("https://www.cdss.ca.gov/foodstamps/res/pdf/CalFresh_GenMrkt_Bro_Hmong.pdf")

    with st.beta_expander("Spanish CalFresh Brochure (Folleto de CalFresh en español)"):
        st.write("CalFresh puede ayudarle a usted y a su familia.")
        st.write("https://211sandiego.org/wp-content/uploads/2016/10/CalFreshBrochureSpan.pdf")

    st.header("Resources by County:") # Resources by County
    st.write("")

    with st.beta_expander("LA County Food Security Resources Page"):
        st.write("The Nutrition and Physical Activity Program is partnering with 18 organizations to implement programs and strategies to improve access to healthy foods and provide nutrition education and physical activity opportunities in LA County through the CalFresh Healthy Living grant. These partners represent a variety of sectors, including early childhood education, school districts, higher education, healthcare, food banks, and community-based organizations.")
        st.write("http://publichealth.lacounty.gov/nut/healthcare-food-access.htm")

    with st.beta_expander("211 LA Food Finder Map"):
        st.write("211 LA is your guide to the services, resources, & information you need to navigate life in Los Angeles.")
        st.write("[https://foodfinder.211la.org/] (https://foodfinder.211la.org/-119.084023,33.286823,-117.626762,35.137795?layers=20%2C22%2C18%2C19%2C21)")

    with st.beta_expander("Sacramento Asian Resources Inc. Workshops"):
        st.write("For more than 30 years, ARI has served the needs of the community, starting with the Asian community and expanding to the broader Sacramento County. They have a Get CalFresh workshop, additional language services, and other welfare workshops.")
        st.write("https://asianresources.org/additional-ari-services")

    with st.beta_expander("Orange County Food Assistance Resources"):
        st.write("If you live in Orange County, the Community Action Partnership of Orange County has compiled a list of resources for food aid.")
        st.write("https://www.capoc.org/resources/ ")

    with st.beta_expander("Foodbank of Southern California"):
        st.write("The Foodbank of Southern California obtains and distributes highly nutritional food to charitable community organizations supporting low-income individuals.")
        st.write("https://www.foodbankofsocal.org/services/food-distribution/")

    with st.beta_expander("AAPI Forward Movement Food Roots Campaign"):
        st.write("API Forward Movement works to increase access to fresh produce and nutritious foodstuffs among the AAPI community of LA County. Check out their several resources, workshops, and programs to learn more about their work on food security and access.")
        st.write("https://www.foodroots.co/")

    with st.beta_expander("Alameda County Community Food Bank"):
        st.write("Founded about 30 years ago, Alameda County Community Food Bank has been working to provide fresh produce and foodstuffs to those in need in Alameda County.")
        st.write("https://www.accfb.org/")

    with st.beta_expander("San Francisco-Marin Food Bank "):
        st.write("Providing SF-Marin County with food aid for over 30 years, SF-Marin County Food Bank’s mission is to end hunger in the area by increasing access to fresh produce and foodstuffs.")
        st.write("https://www.sfmfoodbank.org/")

    with st.beta_expander("Alameda County Social Services Food and Health Guideline"):
        st.write("The Alameda Social Services Agency has compiled several resources that walk through the process for applying to food aid and other welfare programs.")
        st.write("https://www.alamedacountysocialservices.org/our-services/Health-and-Food/index")
