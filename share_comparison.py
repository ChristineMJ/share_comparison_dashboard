import streamlit as st
import pandas as pd
import yfinance as yf
import sqlite3
import sqlalchemy

st.title('Dow Jones Shares Comparison Dashboard')
engine = sqlalchemy.create_engine('sqlite:///Fundamentals.db')
df = pd.read_sql('Fundamentalstable', engine, index_col = ['symbol'])
dropdown_1 = st.selectbox('Select the sector', df.sector.unique())
dropdown_2 = st.selectbox('Select the metric', df.columns[df.columns !='sector'])
values = df[df.sector == dropdown_1][[dropdown_2]]
st.bar_chart(values)

st.title('Share Comparison by a Company')
tickers = ('LMT','MSFT','AAPL','GOOGL','ASML','JNJ','PFE','NKE','KO')
dropdown = st.multiselect('Select your company share', tickers)

start = st.date_input('Start',value = pd.to_datetime('2019-01-01'))
end = st.date_input('End', value = pd.to_datetime('today'))

if len(dropdown) > 0:
    df_1 = yf.download(dropdown,start, end)['Adj Close']
    st.line_chart(df_1)

