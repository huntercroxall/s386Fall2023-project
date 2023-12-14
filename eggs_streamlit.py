import streamlit as st
import pandas as pd
import altair as alt

st.title("Dashboard for FDA Egg-Related Food Recalls from the Years of 2012-2023")

df = pd.read_csv("FDA_egg_stats.csv")



st.subheader("Table of the Data Used to Analyze Egg-Related Recall Events")
st.dataframe(df)

scatter = alt.Chart(df).mark_circle().encode(x = "dt_report_date", y = 'dt_termination_date', color = "status").interactive().properties(height=300, width=300)
st.altair_chart(scatter, use_container_width=True)

year_count = df['report_year'].value_counts().reset_index()
year_count.columns = ['report_year', 'year_count']

line = alt.Chart(year_count).mark_line(point=True, ).encode(x = 'report_year', 
    y = 'year_count')
st.altair_chart(line, use_container_width=True)

