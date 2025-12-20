import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
from numpy.random import default_rng as rng
import datetime
import time

col_a1, col_a2 = st.columns([0.8, 0.2])
with col_a1:
    st.write("Welcome to My Portofolio")
    st.markdown("**Agus Wijaya**")
    st.write("Student of Data Science and Analyst Bootcamp Dibimbing @2025")
with col_a2:
    st.image("Picture_AW.jpg")

st.write("_________________________________________________________")

col_b1, col_b2 = st.columns(2)
with col_b1:
    st.header("Marketing Channel Analysis")
with col_b2:
    st.image("Picture_Superstore.jpg")

st.write("_________________________________________________________")

st.write("Dataset Name     : Sample Superstore")
st.write("Dataset Source   : www.kaggle.com")
st.write("Dataset Overview : ")
st.write("This is a sample superstore dataset, a kind of a simulation where we can perform extensive data analysis to deliver insights on how the company can increase its profits while minimizing the losses")

st.write("_________________________________________________________")

st.write("Maximum Range of Date     : 2014-01-03 to 2017-12-30")
col_c1, col_c2 = st.columns(2)
with col_c1:
    start_date = st.date_input("Input Start Date of Data Analysis", datetime.date(2014, 1, 3))
with col_c2:
    end_date = st.date_input("Input End Date of Data Analysis", datetime.date(2017, 12, 30))

df = pd.read_csv('Sample_Superstore.csv', encoding = "ISO-8859-1")
df['Order Date'] = pd.to_datetime(df['Order Date']).dt.date

date_mask = (df['Order Date'] > start_date) & (df['Order Date'] <= end_date)
df_date = df.loc[date_mask].sort_values(by = 'Order Date',ascending=True)

total_tsc = df_date['Order ID'].count()
total_rvn = df_date['Sales'].sum().round(1)
total_pft = df_date['Profit'].sum().round(1)

col_d1, col_d2, col_d3 = st.columns(3, border=True, vertical_alignment="center")
with col_d1:
    st.write("Total Transaction")
    st.header(total_tsc)
with col_d2:
    st.write("Total Revenue")
    st.header(total_rvn)
with col_d3:
    st.write("Total Profit")
    st.header(total_pft)
st.write("")

df_tps = df_date.groupby('State')['Order ID'].count().sort_values(ascending=False).reset_index()
df_tps.rename(columns={'Order ID': 'Total Transaction'}, inplace=True)
df_rps = df_date.groupby('State')['Sales'].sum().sort_values(ascending=False).round(1).reset_index()
df_rps.rename(columns={'Sales': 'Total Revenue'}, inplace=True)
df_pps = df_date.groupby('State')['Profit'].sum().sort_values(ascending=False).round(1).reset_index()
df_pps.rename(columns={'Profit': 'Total Profit'}, inplace=True)

st.write("Total Transaction per State")
st.bar_chart(df_tps, x='State', y='Total Transaction', color="#fd0")
st.write("Total Revenue per State")
st.bar_chart(df_rps, x='State', y='Total Revenue')
st.write("Total Profit per State")
st.bar_chart(df_pps, x='State', y='Total Profit',color="#f0f")

st.write("Resume Transaction Data per State")
df_state_1 = pd.merge(df_tps,df_rps, on = 'State', how = 'inner')
df_state_2 = pd.merge(df_state_1,df_pps, on = 'State', how = 'inner')
st.dataframe(df_state_2)

st.write("Detail Transaction Data")
st.dataframe(df_date)
