
import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
import plotly.express as px


st.title('Kmx2r Dashboard')

st.subheader('sub índice')

st.header('Header')

st.text('texto escrito nomralmente')

st.markdown("texto en markdown *negrita*  **cursiva**")

st.markdown("# T1 markdown")
st.markdown("texto en markdown dfsdf")

st.metric(label = "Mñetrica", value = "17.5", delta = "-0.2")

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
st.plotly_chart(fig)


ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')

data = yf.download(ticker,start = start_date, end = end_date)
fig3 = px.line(data, x = data.index, y = data['Adj Close'], title = ticker)
st.plotly_chart(fig3)


fig2 = px.line(data, x = [1, 2, 3], y = [2, 4, 5], title = ticker)
st.plotly_chart(fig2)