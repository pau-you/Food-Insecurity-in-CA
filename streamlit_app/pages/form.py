import streamlit as st
import streamlit.components.v1 as components
import datetime
import pandas as pd
import numpy as np

def app():

    st.title("Food Security Diagnostic Quiz")
    st.write("Here, you can answer a few questions to assess your predicted food security situation.")

    # Beginning of Input Questions
    gender = st.radio("Are you male or female?",
                     options=['FEMALE', 'MALE'], help="CHIS Interview Gender Options")

    age = st.selectbox("What is your age?",
                     options=['18-25 YEARS', '26-29 YEARS', '30-34 YEARS', '35-39 YEARS', '40-44 YEARS',
                            '45-49 YEARS', '50-54 YEARS', '55-59 YEARS', '60-64 YEARS', '65-69 YEARS',
                            '70-74 YEARS', '75-79 YEARS', '80-84 YEARS', '85+ YEARS'])

    race = st.selectbox("Which of the following best describes you?",
                     options=['WHITE', 'LATINO', 'OTHER SINGLE/MULTIPLE RACE', 'ASIAN',
       'AFRICAN AMERICAN', 'AMERICAN INDIAN/ALASKA NATIVE'], index=3,  help="UCLA CHPR definition")

    education = st.selectbox("What is the highest grade of education you have completed and received credit for?",
                     options=['NO FORMAL EDUCATION OR GRADE 1-8', 'GRADE 9-11', 'GRADE 12/H.S. DIPLOMA',
                     'VOCATIONAL SCHOOL', 'SOME COLLEGE', 'AA OR AS DEGREE', 'BA OR BS DEGREE/SOME GRAD SCHOOL',
                     'MA OR MS DEGREE', 'PH.D. OR EQUIVALENT'])

    city = st.radio("Rural Urban question",
                     options=['URBAN', 'SUBURBAN', 'MIXED', 'TOWN', 'RURAL', '2ND CITY'])

    born = st.radio("Were you born in the United States?",
                     options=['BORN IN U.S.', 'BORN OUTSIDE U.S.'])

    english = st.selectbox("Would you say you speak English...",
                     options=['VERY WELL', 'WELL', 'NOT WELL', 'NOT AT ALL', 'INAPPLICABLE'])

    working = st.selectbox("What is your current employment status?",
                     options=['UNEMPLOYED, NOT LOOKING FOR WORK', 'UNEMPLOYED, LOOKING FOR WORK',
                     'PART-TIME EMPLOYMENT (0-20 HRS/WEEK)', 'FULL-TIME EMPLOYMENT (21+ HRS/WEEK)',
                     'OTHER EMPLOYED'])

    medical = st.radio("For your health plan, are you covered by Medi-Cal?",
                     options=['NO', 'YES'])

    psych = st.slider("Psychological stress question", min_value=0., max_value=24., step=1.)

    married = st.selectbox("Are you now married, living with a partner in a marriage-like relationship, widowed, divorced, separated, or never married?",
                     options=['MARRIED', 'WID/SEP/DIV', 'NEVER MARRIED', 'LIVING W/ PARTNER'])

    # End of Input Questions
    st.error("End of Form")

    features = ['RACE - UCLA CHPR DEFINITION, UNABRIDGED (PUF 1 YR RECODE)', 'EDUCATIONAL ATTAINMENT (PUF 1 YR RECODE)',
            'RURAL AND URBAN - CLARITAS (BY CENSUS TRACT) (6 LVLS)', 'BORN IN U.S.', 'LEVEL OF ENGLISH PROFICIENCY: GENERAL ', 'SELF-REPORTED AGE (PUT 1 YR RECODE)',
            'SELF-REPORTED GENDER', 'WORKING STATUS (PUF 1 YR RECODE)','COVERED BY MEDI-CAL', 'SERIOUS PSYCHOLOGICAL DISTRESS', 'MARITAL STATUS- 4 CATEGORIES']

    dvalues = [race, education, city, born, english, age, gender, working, medical, psych, married]
    input_values = dict(zip(features, dvalues))


    df = pd.DataFrame(input_values, index = [0])
    side_dict = {"Variables": features, "Your Responses": [str(i) for i in input_values.values()]}

    submit = st.button("Submit")
    if submit:
        sidebar_df = pd.DataFrame(side_dict)
        st.sidebar.dataframe(sidebar_df)
        st.dataframe(df)
        st.write("You submitted the form")












    smoke = st.checkbox("Do you smoke?")
    weight = st.slider("Choose your weight", min_value=40., max_value=150., step=0.5)
    physical_form = st.selectbox("Select level of your physical condition",
                                 options=["Bad", "Normal", "Good"])
    colors = st.multiselect('What are your favorite colors',
                            options=['Green', 'Yellow', 'Red', 'Blue', 'Pink'])

    btn = st.button("Celebrate!")
    if btn:
        st.balloons()
