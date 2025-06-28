
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📈 Adani Enterprises Stock Market Analysis")

# Load the dataset
df = pd.read_csv("Quote-Equity-ADANIENT-EQ-27-06-2024-to-27-06-2025.csv")  # Use correct filename here

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Convert 'date' column to datetime and sort
df['date'] = pd.to_datetime(df['date'], format='%d-%b-%y')
df = df.sort_values(by='date')

# Sidebar
st.sidebar.header("Options")
show_data = st.sidebar.checkbox("Show Raw Data")

if show_data:
    st.subheader("Raw Data")
    st.write(df)

# Closing price chart
st.subheader("📉 Closing Price Over Time")
fig = px.line(df, x='date', y='close', title='Adani Closing Prices')
st.plotly_chart(fig, use_container_width=True)

# Volume chart
st.subheader("📊 Volume Traded Over Time")
fig2 = px.bar(df, x='date', y='volume', title='Trading Volume')
st.plotly_chart(fig2, use_container_width=True)
