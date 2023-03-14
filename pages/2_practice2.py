import streamlit as st
import pandas as pd
import plotly.express as px
import time

def main():
    # Load data
    df = pd.read_csv("./data/world-happiness-report.csv")
    df = df.dropna()
    st.title("World Happiness Graph")


    year_min = int(df["year"].min())
    year_max = int(df["year"].max())


    #Fill in here
    year_start = year_min
    year_end = year_max
    year_step = 1

    st.sidebar.markdown("## World Happiness Data")
    year_range = st.sidebar.slider("Select Year Range", year_min, year_end, (year_start, year_end), year_step)
    countries = st.sidebar.multiselect("Select Countries", df['Country name'].unique())

    # Filter data based on user selection
    df_filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
    if countries:
        df_filtered = df_filtered[df_filtered['Country name'].isin(countries)]

    # Main app layout
    st.write("Showing data from", year_range[0], "to", year_range[1])

    # Plot data using Plotly Express
    fig = px.scatter(data_frame=df_filtered,
                x="Log GDP per capita",
                y="Healthy life expectancy at birth",
                size="Life Ladder",
                color="Country name",
                range_x=[3, 12],
                range_y=[20, 85],
                animation_frame='year',
                title="World Happiness Report")

    fig.update_layout(title='GDP per capita vs. Life expectancy', xaxis_title='Log GDP per capita', yaxis_title='Life expectancy')
    st.plotly_chart(fig)
    

if __name__ == '__main__':
    main()