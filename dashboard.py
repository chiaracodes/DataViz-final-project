import streamlit as st
import pandas as pd
import altair as alt
from page1 import page1
from page2 import page2


@st.cache
def load_full_data():
    df = pd.read_csv("data.csv", index_col = 0)
    return df
@st.cache
def map_data():
    df_map = pd.read_csv("data_with_id.csv",index_col = 0)
    return df_map

if __name__ == '__main__':
    df = load_full_data()
    df1 = map_data()
    countries = list(df.Country.unique())
    page = st.select_slider('Navigate across the pages',['Homepage', 'Page 1', 'Page 2'])
    
    if page == 'Homepage':
        st.markdown("## Gender Equality in Employment in Europe \nTeam: PowerPuff Girl")
        st.image("https://www.ilprimatonazionale.it/wp-content/uploads/2019/06/gender-gap.jpg")
    
    if page =="Page 1":
        st.markdown("# Woman in Decision Making")
        page1(df,countries)

    if page == "Page 2":
        page2(df, df1,countries)
