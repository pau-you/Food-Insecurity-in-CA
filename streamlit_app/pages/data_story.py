import streamlit as st
import streamlit.components.v1 as components
import datetime
import pandas as pd
import numpy as np

def app():

    st.title("The State of Food Security in California")

    CA_counties = """<div class='tableauPlaceholder' id='viz1626125213787' style='position: relative'><noscript><a href='#'><img alt='CA Food Insecurity Rates Apr2020-Oct2020  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;se&#47;secure_the_bag&#47;2020CArates&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='secure_the_bag&#47;2020CArates' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;se&#47;secure_the_bag&#47;2020CArates&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1626125213787');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(CA_counties, height = 500, scrolling = True)

    education_insecurity = """<div class='tableauPlaceholder' id='viz1627344848554' style='position: relative'><noscript><a href='#'><img alt='Educational Attainment &amp; Food Insecurity&#47;Security Relationship ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ed&#47;EducationalAttainmentFoodInsecuritySecurityRelationship&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='EducationalAttainmentFoodInsecuritySecurityRelationship&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ed&#47;EducationalAttainmentFoodInsecuritySecurityRelationship&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1627344848554');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(education_insecurity, height = 500, scrolling = True)

    psych_insecurity = """<div class='tableauPlaceholder' id='viz1627332521958' style='position: relative'><noscript><a href='#'><img alt='Serious Psychological Distress Level &amp; Food Insecurity ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Se&#47;SeriousPsychologicalDistress&#47;Sheet3&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='SeriousPsychologicalDistress&#47;Sheet3' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Se&#47;SeriousPsychologicalDistress&#47;Sheet3&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1627332521958');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(psych_insecurity, height = 500, scrolling = True)

    shap_feature_impact = "https://lh3.googleusercontent.com/pw/AM-JKLUihieYlHfUa6dWxGbNderDZPz57THTRSJofJGSZBiJukFwZKQsGdM3rvmgM3FzIpd45ELbNlUHwl5_eHcejNJ6VfsDzgE7x1aMTn__bZIhp1BmMVhdI75ZFwZvTCxWynT26ZaWBL8JsvXv8rgjM9w=w911-h393-no"
    st.image(shap_feature_impact)

    shap_feature_value = "https://lh3.googleusercontent.com/pw/AM-JKLUK2gHJgdKceH-6gVVnNEyyb7kyMktHuilgG4tvk2QX14f6W6EtsY6962ONVJwY52gWXcpAqzwzX1gzhbw5SQMcg_5beC2n4PRLyi6G6doxwkqnusci9HgvfnZds9kHZNWrzKHSYr4waDK5lE5cgGw=w905-h375-no"
    st.image(shap_feature_value)



    col1, col2 = st.beta_columns([4,1])
    with col1:
        st.line_chart({"data": [1, 5, 2, 6, 2, 1]})
    with col2:
        st.write("Look it's a line chart on the left. With lines. And numbers. And stuff.")

    with st.beta_expander("See explanation"):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
        st.image("https://static.streamlit.io/examples/dice.jpg")
