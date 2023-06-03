import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import seaborn as sns

st.title('Real Madrid Player Wages')

st.markdown("""
This app webscrapes Real Madrid player wage stats data
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [FBref.com](https://fbref.com/en/squads/53a2f082/2022-2023/wages/Real-Madrid-Wage-Details)
""")

st.sidebar('Data Filters')
season_list = ["2013-2014", "2014-2015", "2015-2016", "2016-2017", "2017-2018", 
               "2018-2019", "2019-2020", "2020-2021", "2021-2022", "2022-2023"]
selected_season = st.sidebar.selectbox('Season', list(season_list))

# Scraping the data source of Real Madrid wages
# https://www.capology.com/club/real-madrid/salaries/2022-2023/
@st.cache
def load_data(season):
    url = "https://fbref.com/en/squads/53a2f082/" + str(season) + "/wages/Real-Madrid-Wage-Details"
    html = pd.read_html(url, header = 1) # web scraping
    df = html[0]
    # data processing

