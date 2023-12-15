import streamlit as st
import pandas as pd
import altair as alt

st.title("Dashboard for FDA Egg-Related Food Recalls from the Years of 2012-2023")

df = pd.read_csv("FDA_egg_stats.csv")

df['report_year'] = df['report_year'].astype(str)


st.markdown("#")

st.subheader("Table of the Data Used to Analyze Egg-Related Recall Events")
st.dataframe(df)

Q1,Q2 = st.columns(2)

with Q1:
    st.subheader("Scatterplot of Length of Recall Events")

    scatter = alt.Chart(df).mark_circle().encode(x = "dt_report_date", y = 'dt_termination_date', color = "status").interactive().properties(height=300, width=300)
    st.altair_chart(scatter, use_container_width=True)

    st.write("This scatterplot compares the date when a egg-related recall is made and when that same recall is terminated. As you can see, most recall events only exist for a period of roughly three months. There are only a few recall events that last much longer than that.")
    
    st.subheader("Boxplot of Month Separated by Classification")


    box = alt.Chart(df).mark_boxplot(extent='min-max').encode(x = 'classification', y = 'report_month')
    st.altair_chart(box, use_container_width=True)

st.markdown("#")
st.markdown("#")

year_count = df['report_year'].value_counts().reset_index()
year_count.columns = ['report_year', 'year_count']

with Q2:
    st.subheader("Line Chart of Number of Recall Events per Year")

    line = alt.Chart(year_count).mark_line(point=True, ).encode(x = 'report_year', 
    y = 'year_count')
    st.altair_chart(line, use_container_width=True)

    st.dataframe(year_count)
    st.write("This line chart shows how many recall events have occurred over the past 11 years. The highest number of events occurred in 2017, and the lowest number is in 2012.")


state_count = df['state'].value_counts().reset_index()
state_count.columns = ['state', 'state_count']

st.subheader("Bar Chart of the Number of Recall Events per State")

bar = alt.Chart(state_count).mark_bar().encode(x = 'state_count', y = alt.Y('state', sort = '-x')).properties(height=1000)
st.altair_chart(bar, use_container_width=True)

Q3,Q4 = st.columns(2)

with Q4:
    st.dataframe(state_count)

with Q3:
    st.write("This bar chart shows where the most egg-related recall events occur. As you can see, California has the most by a huge margin, followed by many of the other highly populated states of the US.")

st.markdown('#')

Q5,Q6 = st.columns(2)

classify_count = df['classification'].value_counts().reset_index()
classify_count.columns = ['classification', 'classify_count']
with Q5:
    st.dataframe(classify_count)

with Q6:
    st.subheader('Donut Chart of Number of the Classifications of Recall Events')

    donut = alt.Chart(classify_count).mark_arc(innerRadius=50).encode(theta="classify_count", color="classification")
    st.altair_chart(donut, use_container_width=True)


