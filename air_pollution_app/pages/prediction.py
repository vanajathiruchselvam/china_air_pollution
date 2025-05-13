import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def app():
    st.title("📈 AQI Category Prediction")

    df = pd.read_csv("data/air_pollution.csv")
    df = df.drop(columns=['No', 'PM2.5', 'PM2.5_Rolling'], errors='ignore')

    for col in ['station', 'season', 'peak_hour']:
        df[col] = LabelEncoder().fit_transform(df[col])

    X = df.drop(columns=['AQI_PM2.5'])
    y = df['AQI_PM2.5']

    model = RandomForestClassifier()
    model.fit(X, y)

    st.subheader("Enter New Values:")
    input_data = {}
    for col in X.columns:
        val = st.number_input(f"{col}:", value=float(df[col].mean()))
        input_data[col] = val

    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]

    st.success(f"Predicted AQI Category: **{prediction}**")
