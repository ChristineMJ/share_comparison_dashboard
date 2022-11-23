import streamlit as st
import pandas as pd
import sqlite3
import sqlalchemy

st.title('Dow Jones Shares Comparison')
engine = sqlalchemy.create_engine('sqlite:///Fundamentals.db')
df = pd.read_sql('Fundamentalstable', engine, index_col = ['symbol'])
dropdown_1 = st.selectbox('Select the sector', df.sector.unique())
dropdown_2 = st.selectbox('Select the metric', df.columns[df.columns !='sector'])
values = df[df.sector == dropdown_1][[dropdown_2]]
st.bar_chart(values)