import streamlit as st
import pandas as pd
import altair as alt

st.title("Dashboard for FDA Egg-Related Food Recalls from the Years of 2012-2023")

df = pd.read_csv("FDA_egg_stats.csv")

df['report_year'] = df['report_year'].astype(str)


st.markdown("#")
st.markdown("#")
st.subheader("Table of the Data Used to Analyze Egg-Related Recall Events")
st.dataframe(df)

Q1,Q2 = st.columns(2)

with Q1:
    st.subheader("Scatterplot of Length of Recall Events")

    scatter = alt.Chart(df).mark_circle().encode(x = "dt_report_date", y = 'dt_termination_date', color = "status").interactive().properties(height=300, width=300)
    st.altair_chart(scatter, use_container_width=True)

    st.write("This scatterplot compares the date when a egg-related recall is made and when that same recall is terminated. As you can see, most recall events only exist for a period of roughly three months. There are only a few recall events that last much longer than that.")

st.markdown("#")
st.markdown("#")

year_count = df['report_year'].value_counts().reset_index()
year_count.columns = ['report_year', 'year_count']

with Q2:
    st.subheader("Line Chart of Number of Recall Events per Year")

    line = alt.Chart(year_count).mark_line(point=True, ).encode(x = 'report_year', 
    y = 'year_count')
    st.altair_chart(line, use_container_width=True)

    st.write("This line chart shows how many recall events have occurred over the past 11 years. The highest number of events occurred in 2017, and the lowest number is in 2012.")






