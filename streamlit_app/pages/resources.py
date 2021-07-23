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

    st.header("Resources for California:")

    with st.beta_expander("Apply for California Food Stamps Online | GetCalFresh.org"):
        st.write("GetCalFresh can help you apply for California Food Stamps, also known as CalFresh, SNAP, Food Assistance, or EBT, in as little as ten minutes.")
        st.write("https://www.getcalfresh.org/")

    with st.beta_expander("California Association of Food Banks"):
        st.write("We lead the collective effort to end hunger in California")
        st.write("https://www.cafoodbanks.org/")

    with st.beta_expander("CA Local Food Bank Locator"):
        st.write("Find a Local Food Bank")
        st.write("https://www.cafoodbanks.org/our-members/")

    with st.beta_expander("CA Food Banks Covid-19 Resources"):
        st.write("Our food bank network remains committed to keeping critical food resources moving to people who need them. We remain committed to providing them with the latest information, resources, and guidance. We are monitoring this evolving crisis and responding to ensure we are following the guidelines and recommendations of the Center for Disease Control (CDC) and local health departments.")
        st.write("https://www.cafoodbanks.org/covid-19-resources/")

    with st.beta_expander("Emergency Food Assistance Program (EFAP)"):
        st.write("The Emergency Food Assistance Program (EFAP) is a Federal program that helps supplement the diets of low-income Americans, including elderly people, by providing them with emergency food assistance at no cost.")
        st.write("https://www.cdss.ca.gov/emergency-food")

    with st.beta_expander("About CalFresh Guide in Simplified Chinese (关于CalFresh)"):
        st.write("在何处以及如何使用CalFresh在当地农贸市场购买新鲜及健康的农场食品")
        st.write("https://www.freshapproach.org/wp-content/uploads/2019/07/2019-Calfresh-FMs-Contra-Costa-Simplified-Chinese-Mandarin.pdf")

    with st.beta_expander("Hmong CalFresh Brochure (Hmong CalFresh Ntawv nthuav qhia)"):
        st.write("Nyiaj CalFresh yuav pab tau koj thiab koj tsev neeg.")
        st.write("https://www.cdss.ca.gov/foodstamps/res/pdf/CalFresh_GenMrkt_Bro_Hmong.pdf")

    with st.beta_expander("Spanish CalFresh Brochure (Folleto de CalFresh en español)"):
        st.write("CalFresh puede ayudarle a usted y a su familia.")
        st.write("https://211sandiego.org/wp-content/uploads/2016/10/CalFreshBrochureSpan.pdf")

    st.header("Resources by County:")

    with st.beta_expander("LA County Food Security Resources Page"):
        st.write("The Nutrition and Physical Activity Program is partnering with 18 organizations to implement programs and strategies to improve access to healthy foods and provide nutrition education and physical activity opportunities in LA County through the CalFresh Healthy Living grant. These partners represent a variety of sectors, including early childhood education, school districts, higher education, healthcare, food banks, and community-based organizations.")
        st.write("http://publichealth.lacounty.gov/nut/healthcare-food-access.htm")

    with st.beta_expander("211 LA Food Finder Map"):
        st.write("211 LA is your guide to the services, resources, & information you need to navigate life in Los Angeles.")
        st.write("[https://foodfinder.211la.org/] (https://foodfinder.211la.org/-119.084023,33.286823,-117.626762,35.137795?layers=20%2C22%2C18%2C19%2C21)")

    with st.beta_expander("Sacramento Asian Resources Inc. Workshops"):
        st.write("For more than 30 years, ARI has served the needs of the community. ARI has a budget of over $2.5M in funding to offer the various programs and resources at no cost to the community.  ARI also offers a variety of programs that will continue to cater to the needs of the community.")
        st.write("https://asianresources.org/additional-ari-services")

    with st.beta_expander("Orange County Food Assistance Resources"):
        st.write("Various food resources to help families prevent hunger throughout Orange County.")
        st.write("https://www.capoc.org/resources/ ")

    with st.beta_expander("Foodbank of Southern California"):
        st.write("The Foodbank obtains and distributes highly nutritional food to charitable community organizations supporting low-income individuals.")
        st.write("https://www.foodbankofsocal.org/services/food-distribution/")

    with st.beta_expander("AAPI Forward Movement Food Roots Campaign"):
        st.write("Our mission is to connect local and sustainably grown Asian specialty foods to communities and businesses in the greater Los Angeles area while supporting Asian American small farms and other farmers of color in California. To create a just, equitable, and sustainable local food system focused on reconnecting people to their food, the land, and the people who grow it.")
        st.write("https://www.foodroots.co/")

    with st.beta_expander("Alameda County Community Food Bank"):
        st.write("Food is a basic human right. We work towards a stronger, more nourished Alameda County, where no one worries where their next meal will come from.")
        st.write("https://www.accfb.org/")

    with st.beta_expander("San Francisco-Marin Food Bank "):
        st.write("Together, we can end hunger in San Francisco and Marin. The Food Bank continues to be here as a steadfast beacon of community, compassion, and care as we provide food for the hungry.")
        st.write("https://www.sfmfoodbank.org/")

    with st.beta_expander("Alameda County Social Services Food and Health Guideline"):
        st.write("Assistance for individuals and families to purchase nutritious food")
        st.write("https://www.alamedacountysocialservices.org/our-services/Health-and-Food/index")
