import pickle
import streamlit as st
import pandas as pd
pd = pd.read_csv('Salary_Data.csv')

model = pickle.load(open('Salary.sav', 'rb'))

st.title('Salary Prediction')
check_data = st.checkbox("Lihat Simpel Data")
if check_data:
    st.write(pd[1:6])

years = st.number_input('years of experience')


predict = ''

if st.button('Calculate Salary'):
    predict = model.predict([[years]]
    )
    st.write ('The Estimated Salary : ', predict)
