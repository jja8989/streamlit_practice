import streamlit as st
import streamlit as st
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

def main():

    df = pd.read_csv("./data/world-happiness-report.csv")
    df = df.dropna()
    st.title("World Happiness Treemap")

    st.write(df)


    #Fill in here
    year = st.slider('Select year', int(df['year'].min()), int(df['year'].max()), step=1)
    countries = st.multiselect("Select Countries", df['Country name'].unique())

    data_filtered = df[df['year'] == year]


    if countries:
        data_filtered = data_filtered[data_filtered['Country name'].isin(countries)]

    # Create plot
    fig = px.treemap(data_filtered, path=['Country name'], values=data_filtered['Healthy life expectancy at birth'],
                    color='Log GDP per capita', hover_data=['Life Ladder', 'Social support', 'Freedom to make life choices'],
                    color_continuous_scale='RdBu')
    
    st.plotly_chart(fig, use_container_width=True)

if __name__ == '__main__':
    main()

