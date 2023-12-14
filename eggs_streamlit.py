import streamlit as st
import pandas as pd

st.title("Dashboard for FDA Egg-Related Food Recalls from the Years of 2012-2023")

df = pd.read_csv("FDA_egg_stats.csv")

st.subheader("Table of the Data Used to Analyze Egg-Related Recall Events")
st.dataframe(df)