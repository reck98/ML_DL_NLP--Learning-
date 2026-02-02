import pandas as pd
import numpy as np
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Iris Flower Classifier", layout="centered")

@st.cache_data
def loadData():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["species"] = iris.target
    return df, iris.target_names

df, targetName = loadData()

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(df.iloc[:, :-1], df["species"])

# UI
st.title("🌸 Iris Flower Species Predictor")
st.sidebar.title("Input Features")

sepalLength = st.sidebar.slider(
    "Sepal Length (cm)",
    float(df["sepal length (cm)"].min()),
    float(df["sepal length (cm)"].max()),
    float(df["sepal length (cm)"].mean())
)

sepalWidth = st.sidebar.slider(
    "Sepal Width (cm)",
    float(df["sepal width (cm)"].min()),
    float(df["sepal width (cm)"].max()),
    float(df["sepal width (cm)"].mean())
)

petalLength = st.sidebar.slider(
    "Petal Length (cm)",
    float(df["petal length (cm)"].min()),
    float(df["petal length (cm)"].max()),
    float(df["petal length (cm)"].mean())
)

petalWidth = st.sidebar.slider(
    "Petal Width (cm)",
    float(df["petal width (cm)"].min()),
    float(df["petal width (cm)"].max()),
    float(df["petal width (cm)"].mean())
)

# Create input DataFrame
input_df = pd.DataFrame(
    [[sepalLength, sepalWidth, petalLength, petalWidth]],
    columns=df.columns[:-1]
)

prediction = model.predict(input_df)
probability = model.predict_proba(input_df)

st.subheader("Prediction")
st.success(f"🌼 Species: **{targetName[prediction[0]]}**")

st.subheader("Prediction Probability")
st.write(pd.DataFrame(probability, columns=targetName))
