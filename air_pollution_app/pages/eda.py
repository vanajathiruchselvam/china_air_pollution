import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title("📊 Exploratory Data Analysis")
    df = pd.read_csv("air_pollution_app/data/air_pollution.csv")

    st.subheader("AQI Category Distribution")
    fig1, ax1 = plt.subplots()
    sns.countplot(data=df, x='AQI_PM2.5', ax=ax1)
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    st.subheader("Correlation Heatmap")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax2)
    st.pyplot(fig2)
