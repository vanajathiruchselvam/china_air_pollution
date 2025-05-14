import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# Set background image using custom HTML
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

# Load the merged air pollution data from a single CSV file
def load_data():
    # Load the merged dataset
    df = pd.read_csv('data/air_pollution.csv')

    # Check the column names to ensure required columns exist
    st.write("Column Names in DataFrame:", df.columns)



    return df

# Draw box plot for pollutants by station
def plot_box(df, col):
    fig, ax = plt.subplots(figsize=(10, 4))

    # Ensure that the station and the selected pollutant column exist
    if col not in df.columns:
        st.error(f"Column {col} not found in the data")
        return
    
    sns.boxplot(data=df, x='station', y=col, ax=ax)
    ax.set_title(f"{col} Distribution by Station")
    return fig

# Main function
def main():
    # Set the background image using custom HTML
    set_background()

    st.title(" Air Quality Data Overview")
    st.markdown("Here is an overview of PM2.5, PM10, and other pollutants across selected stations.")

    # Load the data
    df = load_data()

    # If the DataFrame didn't load correctly, exit
    if df.empty:
        return

    # Basic Statistics
    st.subheader(" Summary Statistics")
    st.dataframe(df.describe().T.style.highlight_max(axis=0), use_container_width=True)

    # Box plot for pollutants
    st.subheader("📦 Distribution of Pollutants by Station")
    pollutant = st.selectbox("Select Pollutant", ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'])
    st.pyplot(plot_box(df, pollutant))

    # Additional insights (Example for PM2.5)
    st.subheader("🔍 Useful Insights")
    st.markdown(f"""
    - The average PM2.5 level across all stations is **{df['PM2.5'].mean():.2f} µg/m³**.
    - The highest recorded PM2.5 is **{df['PM2.5'].max():.2f} µg/m³** at station **{df[df['PM2.5'] == df['PM2.5'].max()]['station'].values[0]}**.
    """)

if __name__ == "__main__":
    main()
