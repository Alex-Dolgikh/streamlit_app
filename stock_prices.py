import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# My stock prices app
         
This app shows Apple **closing** price and **volume**

""")

ticker_symbol = 'AAPL'
stock_data = yf.Ticker(ticker_symbol)
stock_df = stock_data.history(period='1d',start='2013-10-17',end='2023-10-17')

st.write("""
## Closing price
""")
st.line_chart(stock_df.Close)
st.write("""
## Volume
""")
st.line_chart(stock_df.Volume)