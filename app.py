import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np
import seaborn as sns

df = pd.read_csv("../../sprint4/real_madrid.csv")

st.title('Real Madrid Player Wages')

st.markdown("""
This app webscrapes Real Madrid player wage stats data
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [FBref.com](https://fbref.com/en/squads/53a2f082/2022-2023/wages/Real-Madrid-Wage-Details)
""")

# Sidebar Filter
st.sidebar.header('Season Filters')
season_list = ["2018-2019", "2019-2020", "2020-2021", "2021-2022", "2022-2023"]
selected_season = st.sidebar.selectbox('Season', list(season_list))

# Sidebar - Country Selection
sorted_unique_country = sorted(df.Nation.unique())
selected_country - st.sidebar.multiselect('Country', sorted_unique_country,sorted_unique_country)

# Sidebar - Position Selection
unique_pos = df.Pos
selected_position - st.sidebar.multiselect('Position', unique_pos,unique_pos)

# Filtering Data
df_selection = df[(df.Nation.isin(selected_country)) & (df.Pos.isin(selected_position))]

st.header('Wage Stats')
st.write('Data Dimension:' + str(df_selection.shape[0] + ' rows and ' + str(df_selection.shape[1] + ' columns.')
st.dataframe(df_selection)

# Option to download the CSV file
def filedownload(df):
  csv = df.to_csv(index=False)
  b64 = base64.b64encode(csv.encode()).decode()
  href = f'<a href="data:file/csv;base64,{b64}" download="real_madrid.csv">Download CSV File</a>'
  return href

st.markdown(filedownload(df_selection), unsafe_allow_html=True)
                                 
# Charts
if st.button('Country Histogram'):
    st.header('Player Nationality by Age Group')
    px.histogram(df, x='Age', marginal = 'violin',
             range_x=(14,40), animation_frame='Season',nbins=5,
             color='Nation', height=1000)                                       
    st.plyplot()
