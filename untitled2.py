import pandas as pd
import streamlit as st
from statsmodels.tsa.arima.model import ARIMA

data=pd.read_csv('final.csv')
data.set_index('year',inplace=True)



def time_series():      
    X = data.values
    X = X.astype('float32')
    model = ARIMA(X,order = (2,0,1))
    model_fit = model.fit()

    year = st.sidebar.slider('Forecasted',min_value=2020,max_value=2040)

    n = 2040-year

    forecast = model_fit.forecast(steps = 26-n)
    future_year = [data.index[-1]+i+1 for i in range(0,26-n)]
    future_df = pd.DataFrame(index = future_year,columns = data.columns )
    future_df['CO2'] = forecast

    df = data.append(future_df)

    st.sidebar.dataframe(future_df)
    st.header("ARIMA model with order = (2,0,1")
    st.line_chart(df)             

time_series()