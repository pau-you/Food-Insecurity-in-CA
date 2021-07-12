import streamlit as st
import streamlit.components.v1 as components
import datetime
import pandas as pd
import numpy as np

def app():

    st.title("Form for the Users")
    st.write("Here, you can answer to some questions in this form.")

    html_temp = """<div class='tableauPlaceholder' id='viz1626125213787' style='position: relative'><noscript><a href='#'><img alt='CA Food Insecurity Rates Apr2020-Oct2020  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;se&#47;secure_the_bag&#47;2020CArates&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='secure_the_bag&#47;2020CArates' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;se&#47;secure_the_bag&#47;2020CArates&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1626125213787');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, height = 600, scrolling = True)

    user_id = st.text_input("ID", value="Your ID", max_chars=7)
    info = st.text_area("Share some information about you", "Put information here",
                        help='You can write about your hobbies or family')
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
    birth_date = st.date_input("Date of Birth", min_value=datetime.date(1921, 1, 1),
                               max_value=datetime.date(2003, 12, 31))
    smoke = st.checkbox("Do you smoke?")
    genre = st.radio("Which movie genre do you like?",
                     options=['horror', 'adventure', 'romantic'])
    weight = st.slider("Choose your weight", min_value=40., max_value=150., step=0.5)
    physical_form = st.selectbox("Select level of your physical condition",
                                 options=["Bad", "Normal", "Good"])
    colors = st.multiselect('What are your favorite colors',
                            options=['Green', 'Yellow', 'Red', 'Blue', 'Pink'])
    image = st.file_uploader("Upload your photo", type=['jpg', 'png'])

    col1, col2 = st.beta_columns(2)
    with col1:
        st.image("https://static.streamlit.io/examples/cat.jpg", width=300)
        st.button("Like cats")
    with col2:
        st.image("https://static.streamlit.io/examples/dog.jpg", width=355)
        st.button("Like dogs")

    submit = st.button("Submit")

    if submit:
        st.write("You submitted the form")

    click = st.sidebar.button('Click me!')
    if click:
        st.sidebar.write("You clicked the button")

    st.markdown("## Party time!")
    st.write("Yay! You're done with this tutorial of Streamlit. Click below to celebrate.")
    btn = st.button("Celebrate!")
    if btn:
        st.balloons()
