import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def app():
    st.title("📈 AQI Category Prediction")

    df = pd.read_csv("air_pollution_app/data/air_pollution.csv")
    df = df.drop(columns=['No', 'PM2.5', 'PM2.5_Rolling'], errors='ignore')

    # Encode categorical variables
    label_encoders = {}
    for col in ['station', 'season', 'peak_hour']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    X = df.drop(columns=['AQI_PM2.5'])
    y = df['AQI_PM2.5']

    model = RandomForestClassifier()
    model.fit(X, y)

    # Prediction input section
    st.subheader("Enter New Values:")
    input_data = {}
    for col in X.columns:
        val = st.number_input(f"{col}:", value=float(df[col].mean()))
        input_data[col] = val

    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]

    st.success(f"Predicted AQI Category: **{prediction}**")

    # ----------------------------------
    # AQI Summary by Station
    # ----------------------------------
    st.subheader("📊 AQI Summary by Station")

    # Decode station names for readability
    if 'station' in label_encoders:
        df['station_name'] = label_encoders['station'].inverse_transform(df['station'])

    # AQI count per station
    aqi_distribution = df.groupby('station_name')['AQI_PM2.5'].value_counts().unstack().fillna(0)
    st.markdown("**AQI Category Counts per Station**")
    st.dataframe(aqi_distribution)

    # Average AQI "level" by assigning scores
    aqi_score_map = {
        'Good': 1,
        'Moderate': 2,
        'Unhealthy for Sensitive': 3,
        'Unhealthy': 4,
        'Very Unhealthy': 5
    }
    df['AQI_Score'] = df['AQI_PM2.5'].map(aqi_score_map)
    avg_scores = df.groupby('station_name')['AQI_Score'].mean().sort_values(ascending=False)

    st.markdown("**Average AQI Score per Station**")
    fig, ax = plt.subplots(figsize=(10, 4))
    avg_scores.plot(kind='bar', ax=ax, color='coral')
    ax.set_ylabel("Average AQI Score (1=Good, 5=Very Unhealthy)")
    ax.set_title("Average AQI Severity by Station")
    plt.xticks(rotation=45)
    st.pyplot(fig)
