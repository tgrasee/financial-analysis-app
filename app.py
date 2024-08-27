import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#Streamlit app title
st.title('Stock Price Analysis App')

#User input for stock symbol
symbol = st.text_input('Enter stock symbol', 'AAPL')

if symbol:
    #Fetch data
    stock = yf.Ticker(symbol)
    data = stock.history(period="1y")

    #Calculate moving averages
    data['20_MA'] = data['Close'].rolling(window=20).mean()
    data['50_MA'] = data['Close'].rolling(window=50).mean()

#Plot data
st.write(f"## {symbol} Stock Price and Moving Averages")
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(data['Close'], label='Close Price')
ax.plot(data['20_MA'], label='20-Day MA')
ax.plot(data['50_MA'], label='50-Day MA')
ax.set_xlabel('Date')
ax.set_ylabel('Price (USD)')
ax.legend()
st.pyplot(fig)