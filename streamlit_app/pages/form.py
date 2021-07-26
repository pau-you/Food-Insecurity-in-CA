import streamlit as st
import streamlit.components.v1 as components
import datetime
import pandas as pd
import numpy as np

def app():

    st.title("Food Security Diagnostic Quiz")
    st.write("Here, you can answer a few questions to assess your predicted food security situation.")

    # Beginning of Input Questions
    age = st.radio("What is your age?",
                     options=['60-64 YEARS', '65-69 YEARS', '55-59 YEARS', '70-74 YEARS',
        '18-25 YEARS', '50-54 YEARS', '75-79 YEARS', '45-49 YEARS', '85+ YEARS',
        '80-84 YEARS', '35-39 YEARS', '40-44 YEARS', '30-34 YEARS',
        '26-29 YEARS'])

    race = st.radio("Which of the following best describes you?",
                     options=['WHITE', 'LATINO', 'OTHER SINGLE/MULTIPLE RACE', 'ASIAN',
       'AFRICAN AMERICAN', 'AMERICAN INDIAN/ALASKA NATIVE'], help="UCLA CHPR definition")

    education = st.radio("What is the highest grade of education you have completed and received credit for?",
                     options=['BA OR BS DEGREE/SOME GRAD SCHOOL', 'GRADE 12/H.S. DIPLOMA',
       'SOME COLLEGE', 'MA OR MS DEGREE', 'AA OR AS DEGREE',
       'PH.D. OR EQUIVALENT', 'NO FORMAL EDUCATION OR GRADE 1-8', 'GRADE 9-11',
       'VOCATIONAL SCHOOL'])

    city = st.radio("Rural Urban question",
                     options=['URBAN', 'SUBURBAN', 'MIXED', 'TOWN', 'RURAL', '2ND CITY'])

    born = st.radio("Were you born in the United States?",
                     options=['BORN IN U.S.', 'BORN OUTSIDE U.S.'])

    english = st.radio("Would you say you speak English...",
                     options=['INAPPLICABLE', 'VERY WELL', 'WELL', 'NOT WELL', 'NOT AT ALL'])

    gender = st.radio("Are you male or female?",
                     options=['FEMALE', 'MALE'], help="CHIS Interview Gender Options")

    working = st.radio("What is your current employment status?",
                     options=['UNEMPLOYED, NOT LOOKING FOR WORK',
       'FULL-TIME EMPLOYMENT (21+ HRS/WEEK)',
       'PART-TIME EMPLOYMENT (0-20 HRS/WEEK)', 'UNEMPLOYED, LOOKING FOR WORK',
       'OTHER EMPLOYED'])

    medical = st.radio("For your health plan, are you covered by Medi-Cal?",
                     options=['NO', 'YES'])

    psych = st.slider("Psychological stress question", min_value=0., max_value=24., step=1.)

    married = st.radio("Are you now married, living with a partner in a marriage-like relationship, widowed, divorced, separated, or never married?",
                     options=['MARRIED', 'WID/SEP/DIV', 'NEVER MARRIED', 'LIVING W/ PARTNER'])

    # End of Input Questions
    st.error("End of Form")

    features = ['RACE - UCLA CHPR DEFINITION, UNABRIDGED (PUF 1 YR RECODE)', 'EDUCATIONAL ATTAINMENT (PUF 1 YR RECODE)',
            'RURAL AND URBAN - CLARITAS (BY CENSUS TRACT) (6 LVLS)', 'BORN IN U.S.', 'LEVEL OF ENGLISH PROFICIENCY: GENERAL ', 'SELF-REPORTED AGE (PUT 1 YR RECODE)',
            'SELF-REPORTED GENDER', 'WORKING STATUS (PUF 1 YR RECODE)','COVERED BY MEDI-CAL', 'SERIOUS PSYCHOLOGICAL DISTRESS', 'MARITAL STATUS- 4 CATEGORIES']

    df = pd.DataFrame()












    smoke = st.checkbox("Do you smoke?")
    genre = st.radio("R",
                     options=['horror', 'adventure', 'romantic'])
    weight = st.slider("Choose your weight", min_value=40., max_value=150., step=0.5)
    physical_form = st.selectbox("Select level of your physical condition",
                                 options=["Bad", "Normal", "Good"])
    colors = st.multiselect('What are your favorite colors',
                            options=['Green', 'Yellow', 'Red', 'Blue', 'Pink'])

    submit = st.button("Submit")

    if submit:
        st.write("You submitted the form")


    st.markdown("## Party time!")
    st.write("Yay! You're done with this tutorial of Streamlit. Click below to celebrate.")
    btn = st.button("Celebrate!")
    if btn:
        st.balloons()
