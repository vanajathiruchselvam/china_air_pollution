import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def pm25_aqi_level(value):
    if value <= 50: return 'Good'
    elif value <= 100: return 'Moderate'
    elif value <= 150: return 'Unhealthy for Sensitive'
    elif value <= 200: return 'Unhealthy'
    else: return 'Very Unhealthy'

def app():
    st.title("📊 Exploratory Data Analysis")
    df = pd.read_csv("air_pollution_app/data/air_pollution.csv")

    # AQI Category (recalculate if not in data)
    if 'AQI_PM2.5' not in df.columns:
        df['AQI_PM2.5'] = df['PM2.5'].apply(pm25_aqi_level)

    # AQI Distribution
    st.subheader("AQI Category Distribution")
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    sns.countplot(data=df, x='AQI_PM2.5', ax=ax1, palette='Set2')
    ax1.set_title("Air Quality Levels Based on PM2.5")
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    

    # Seasonal Avg
    st.subheader("Average Pollutant Concentration by Season")
    seasonal_avg = df.groupby('season')[['PM2.5', 'PM10', 'NO2', 'CO', 'O3']].mean()
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    seasonal_avg.plot(kind='bar', colormap='coolwarm', ax=ax3)
    ax3.set_ylabel('Concentration (µg/m³)')
    ax3.set_title('Seasonal Averages')
    plt.xticks(rotation=0)
    st.pyplot(fig3)

    # Monthly Trend
    st.subheader("PM2.5 Monthly Trend Over Years")
    monthly_trend = df.groupby(['year', 'month'])[['PM2.5']].mean().reset_index()
    fig4, ax4 = plt.subplots(figsize=(8, 4))
    sns.lineplot(data=monthly_trend, x='month', y='PM2.5', hue='year', ax=ax4)
    ax4.set_title("PM2.5 Monthly Trend")
    st.pyplot(fig4)

    # Worst Stations
    st.subheader("Worst Stations by Average PM2.5")
    worst_pm = df.groupby('station')['PM2.5'].mean().sort_values(ascending=False).head(5)
    st.dataframe(worst_pm)

    # Peak vs Off-Peak Pollution
    st.subheader("Pollutants During Peak vs Off-Peak Hours")
    df['peak_hour'] = df['hour'].apply(lambda x: 'Peak' if x in range(7,11) or x in range(17,21) else 'Off-Peak')
    peak_pollution = df.groupby('peak_hour')[['PM2.5', 'NO2', 'CO']].mean()
    fig5, ax5 = plt.subplots(figsize=(6, 4))
    peak_pollution.plot(kind='bar', ax=ax5)
    ax5.set_ylabel('Concentration')
    ax5.set_title("Peak vs Off-Peak Pollution")
    st.pyplot(fig5)

    # Pollution by Station
    st.subheader("Pollution by Station")
    station_pollution = df.groupby('station')[['PM2.5', 'NO2', 'O3']].mean().sort_values(by='PM2.5', ascending=False)
    fig6, ax6 = plt.subplots(figsize=(10, 4))
    station_pollution.plot(kind='bar', ax=ax6, colormap='viridis')
    ax6.set_ylabel("Concentration")
    ax6.set_title("Station-wise Pollution")
    plt.xticks(rotation=45)
    st.pyplot(fig6)



    # 30-day Rolling Mean
    st.subheader("30-Day Rolling Average of PM2.5")
    df['PM2.5_Rolling'] = df['PM2.5'].rolling(window=30).mean()
    fig8, ax8 = plt.subplots(figsize=(10, 4))
    df['PM2.5'].plot(alpha=0.4, label='PM2.5', ax=ax8)
    df['PM2.5_Rolling'].plot(label='30-Day Mean', ax=ax8)
    ax8.set_title("PM2.5 with 30-Day Rolling Mean")
    ax8.legend()
    st.pyplot(fig8)

    # Violin Plot: Season
    st.subheader("Distribution by Season")
    fig9, ax9 = plt.subplots(figsize=(8, 3))
    sns.violinplot(data=df, x='No', y='season', inner='box', palette='Dark2', ax=ax9)
    sns.despine()
    st.pyplot(fig9)

    # Scatter: TEMP vs PM2.5
    st.subheader("PM2.5 vs Temperature")
    fig10, ax10 = plt.subplots(figsize=(8, 4))
    sns.scatterplot(data=df, x='TEMP', y='PM2.5', alpha=0.4, ax=ax10)
    st.pyplot(fig10)

    # Scatter: Wind Speed vs PM2.5
    st.subheader("PM2.5 vs Wind Speed")
    fig11, ax11 = plt.subplots(figsize=(8, 4))
    sns.scatterplot(data=df, x='WSPM', y='PM2.5', alpha=0.4, ax=ax11)
    st.pyplot(fig11)

    # Scatter: PM2.5 vs NO2 by Station
    st.subheader("PM2.5 vs NO2 by Station")
    fig12, ax12 = plt.subplots(figsize=(8, 4))
    sns.scatterplot(data=df, x='PM2.5', y='NO2', hue='station', ax=ax12)
    st.pyplot(fig12)
