import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def set_background():
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://static.independent.co.uk/2023/03/17/04/Pictures_of_the_Week_Asia_Photo_Gallery_90004.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.7);
    }

    h1, h2, h3 {
        color: #002B5B;
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

def load_data():
    df = pd.read_csv('air_pollution_app/data/air_pollution.csv')
    st.write("Column Names in DataFrame:", df.columns)
    return df

def plot_box(df, col):
    fig, ax = plt.subplots(figsize=(10, 4))
    if col not in df.columns:
        st.error(f"Column {col} not found in the data")
        return
    sns.boxplot(data=df, x='station', y=col, ax=ax)
    ax.set_title(f"{col} Distribution by Station")
    return fig

# ✅ Use app(), not main()
def app():
    set_background()
    st.title(" Air Quality Data Overview")
    st.markdown("Here is an overview of PM2.5, PM10, and other pollutants across selected stations.")

    df = load_data()
    if df.empty:
        return

    st.subheader(" Summary Statistics")
    st.dataframe(df.describe().T.style.highlight_max(axis=0), use_container_width=True)

    st.subheader("📦 Distribution of Pollutants by Station")
    pollutant = st.selectbox("Select Pollutant", ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'])
    st.pyplot(plot_box(df, pollutant))

    st.subheader("🔍 Useful Insights")
    st.markdown(f"""
    - The average PM2.5 level across all stations is **{df['PM2.5'].mean():.2f} µg/m³**.
    - The highest recorded PM2.5 is **{df['PM2.5'].max():.2f} µg/m³** at station **{df[df['PM2.5'] == df['PM2.5'].max()]['station'].values[0]}**.
    """)
