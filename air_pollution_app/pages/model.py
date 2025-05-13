import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

def app():
    st.title("🤖 Model Training")

    df = pd.read_csv("data/air_pollution.csv")
    df = df.drop(columns=['No', 'PM2.5', 'PM2.5_Rolling'], errors='ignore')

    for col in ['station', 'season', 'peak_hour']:
        if col in df.columns:
            df[col] = LabelEncoder().fit_transform(df[col])

    X = df.drop(columns=['AQI_PM2.5'])
    y = df['AQI_PM2.5']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    st.subheader("Classification Report")
    st.text(classification_report(y_test, y_pred))
