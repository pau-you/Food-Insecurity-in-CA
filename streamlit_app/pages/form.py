import streamlit as st
import streamlit.components.v1 as components
import datetime
import pandas as pd
import numpy as np

import pickle
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.preprocessing import OrdinalEncoder, binarize
from io import BytesIO
import requests

def app():

    st.title("Food Security Diagnostic Quiz")
    st.write("Here, you can answer a few questions to assess your predicted food security situation.")

    # Beginning of Input Questions
    gender = st.radio("Are you male or female?",
                     options=['MALE', 'FEMALE', 'OTHER', 'PREFER NOT TO SAY'], help="CHIS Interview Gender Options")

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

    married = st.selectbox("Are you now married, living with a partner in a marriage-like relationship, widowed, divorced, separated, or never married?",
                     options=['MARRIED', 'LIVING W/ PARTNER', 'WID/SEP/DIV', 'NEVER MARRIED'], index=3)

    # Aggregated psych questions
    st.write("The next questions are about how you have been feeling during the past 30 days:")
    ps1 = st.selectbox("About how often during the past 30 days did you feel nervous—Would you say all of the time, most of the time, some of the time, a little of the time, or none of the time?",
                     options=['ALL', 'MOST', 'SOME', 'A LITTLE', 'NONE/NEVER'], index=4, help="Source: CHIS 2018 Adult Questionaire")

    ps2 = st.selectbox("During the past 30 days, about how often did you feel hopeless—all of the time, most of the time, some of the time, a little of the time, or none of the time?",
                     options=['ALL', 'MOST', 'SOME', 'A LITTLE', 'NONE/NEVER'], index=4, help="Source: CHIS 2018 Adult Questionaire")

    ps3 = st.selectbox("During the past 30 days, about how often did you feel restless or fidgety?",
                     options=['ALL', 'MOST', 'SOME', 'A LITTLE', 'NONE/NEVER'], index=4, help="Source: CHIS 2018 Adult Questionaire")

    ps4 = st.selectbox("How often did you feel so depressed that nothing could cheer you up?",
                     options=['ALL', 'MOST', 'SOME', 'A LITTLE', 'NONE/NEVER'], index=4, help="Source: CHIS 2018 Adult Questionaire")

    ps5 = st.selectbox("During the past 30 days, about how often did you feel that everything was an effort?",
                     options=['ALL', 'MOST', 'SOME', 'A LITTLE', 'NONE/NEVER'], index=4, help="Source: CHIS 2018 Adult Questionaire")

    ps6 = st.selectbox("During the past 30 days, about how often did you feel worthless?",
                     options=['ALL', 'MOST', 'SOME', 'A LITTLE', 'NONE/NEVER'], index=4, help="Source: CHIS 2018 Adult Questionaire")

    ps_all = [ps1, ps2, ps3, ps4, ps5, ps6]
    distress_recode = {'ALL':4, 'MOST':3, 'SOME':2, 'A LITTLE':1, 'NONE/NEVER':0}

    psych = 0.0
    for i in ps_all:
        psych += distress_recode[i]

    # End of Input Questions
    st.error("End of Form")

    # Encode user input_values
    features = ['RACE - UCLA CHPR DEFINITION, UNABRIDGED (PUF 1 YR RECODE)', 'EDUCATIONAL ATTAINMENT (PUF 1 YR RECODE)',
            'RURAL AND URBAN - CLARITAS (BY CENSUS TRACT) (6 LVLS)', 'BORN IN U.S.', 'LEVEL OF ENGLISH PROFICIENCY: GENERAL ', 'SELF-REPORTED AGE (PUT 1 YR RECODE)',
            'SELF-REPORTED GENDER', 'WORKING STATUS (PUF 1 YR RECODE)','COVERED BY MEDI-CAL', 'MARITAL STATUS- 4 CATEGORIES']

    enc_cat = [np.array(['AFRICAN AMERICAN', 'AMERICAN INDIAN/ALASKA NATIVE', 'ASIAN',
        'LATINO', 'OTHER SINGLE/MULTIPLE RACE', 'WHITE'], dtype=object),
         np.array(['AA OR AS DEGREE', 'BA OR BS DEGREE/SOME GRAD SCHOOL',
        'GRADE 12/H.S. DIPLOMA', 'GRADE 9-11', 'MA OR MS DEGREE',
        'NO FORMAL EDUCATION OR GRADE 1-8', 'PH.D. OR EQUIVALENT',
        'SOME COLLEGE', 'VOCATIONAL SCHOOL'], dtype=object),
         np.array(['2ND CITY', 'MIXED', 'RURAL', 'SUBURBAN', 'TOWN', 'URBAN'],
               dtype=object),
         np.array(['BORN IN U.S.', 'BORN OUTSIDE U.S.'], dtype=object),
         np.array(['INAPPLICABLE', 'NOT AT ALL', 'NOT WELL', 'VERY WELL', 'WELL'],
               dtype=object),
         np.array(['18-25 YEARS', '26-29 YEARS', '30-34 YEARS', '35-39 YEARS',
                '40-44 YEARS', '45-49 YEARS', '50-54 YEARS', '55-59 YEARS',
                '60-64 YEARS', '65-69 YEARS', '70-74 YEARS', '75-79 YEARS',
                '80-84 YEARS', '85+ YEARS'], dtype=object),
         np.array(['FEMALE', 'MALE'], dtype=object),
         np.array(['FULL-TIME EMPLOYMENT (21+ HRS/WEEK)', 'OTHER EMPLOYED',
                'PART-TIME EMPLOYMENT (0-20 HRS/WEEK)',
                'UNEMPLOYED, LOOKING FOR WORK', 'UNEMPLOYED, NOT LOOKING FOR WORK'],
               dtype=object),
         np.array(['NO', 'YES'], dtype=object),
         np.array(['LIVING W/ PARTNER', 'MARRIED', 'NEVER MARRIED', 'WID/SEP/DIV'],
               dtype=object)]

    encoder = OrdinalEncoder()
    encoder.categories_ = enc_cat

    dvalues = [race, education, city, born, english, age, gender, working, medical, married]
    input_values = dict(zip(features, dvalues))

    df = pd.DataFrame(input_values, index = [0])
    df = pd.DataFrame(encoder.transform(df), columns=features)

    df['SERIOUS PSYCHOLOGICAL DISTRESS'] = psych

    # load the models
    mLink_1 = "https://github.com/secure-the-bag-capstone/project/blob/main/streamlit_app/models/model_1.pickle?raw=true"
    mfile_1 = BytesIO(requests.get(mLink_1).content)
    loaded_model_1 = pickle.load(mfile_1)

    mLink_2 = "https://github.com/secure-the-bag-capstone/project/blob/main/streamlit_app/models/model_2.pickle?raw=true"
    mfile_2 = BytesIO(requests.get(mLink_2).content)
    loaded_model_2 = pickle.load(mfile_2)

    # Predict User Food Security Status
    submit = st.button("Submit")
    if submit:
        st.dataframe(df)
        st.write("You submitted the form")

        user_pred_prob = loaded_model_1.predict_proba(df)[:,1]
        user_pred_prob = user_pred_prob.reshape(1, -1)
        user_pred_class = binarize(user_pred_prob, 0.82)[0]
        user_pred_class.astype(int)

        if user_pred_class[0] == 1:
            st.write("Food Secure")
        else:
            user_pred_second = loaded_model_2.predict(df)
            st.write(user_pred_second[0])
