# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Forecast Dashboard", layout="centered")

# Title
st.title("📊 Sales Forecasting Dashboard")

# Load data
actual = pd.read_csv("actual_sales.csv")
forecast = pd.read_csv("forecast_sales.csv")

# Convert date column to datetime
actual['ds'] = pd.to_datetime(actual['ds'])
forecast['ds'] = pd.to_datetime(forecast['ds'])

# Line chart
st.subheader("📈 Sales Over Time")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(actual['ds'], actual['y'], label='Actual Sales')
ax.plot(forecast['ds'], forecast['yhat'], label='Forecast Sales', linestyle='--')
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
ax.set_title("Actual vs Forecasted Sales")
ax.legend()
st.pyplot(fig)

# View raw tables
st.subheader("📋 Raw Data")
with st.expander("Show Actual Sales Data"):
    st.dataframe(actual.tail(12))

with st.expander("Show Forecasted Data"):
    st.dataframe(forecast.tail(12))
