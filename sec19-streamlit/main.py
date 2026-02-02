import streamlit as st
import pandas as pd
import numpy as np


st.title("reck98")

st.write("Hello World")

df = pd.DataFrame(
    {
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40],
    }
)

st.write(df)

chartData = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"],
)
st.line_chart(chartData)


name = st.text_input("What is your name?")

if name:
    st.write(f'Hello, {name}')
    
age = st.slider("Enter Your Age", 1, 100, 25,  step=1)

st.write(f"Your age is {age}")

options = ['Python', 'ML', 'JS', 'CSS', 'HTML']
choice = st.selectbox("What is your fav lang?", options)
st.write(f"This is choosed option -> {choice}")

uploadedFile = st.file_uploader("Choose a csv file", type=['pdf', 'csv'], accept_multiple_files=True    )

if uploadedFile is not None:
    newDf = pd.DataFrame(uploadedFile)
    st.write(df)

