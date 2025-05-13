import streamlit as st
from multiapp import MultiApp
from pages import data_overview, eda, model, prediction

# Set page configuration with a background image
st.set_page_config(
    page_title="China Air Pollution Dashboard",
    layout="wide"
)

# Set background image using custom HTML
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

# ------------------ 🏁 Introduction Section ------------------ #
st.markdown("""
#  **China Air Pollution Analysis Dashboard**

##  *"Unmasking the air we breathe"*

Air pollution is a major environmental concern in China, affecting millions of people every day. The increasing concentration of pollutants like **PM2.5**, **NO₂**, and **SO₂** due to urbanization and industrialization poses serious health risks.

By analyzing data from selected regions, we aim to explore trends, assess air quality, and aid better decision-making.

---

 **Selected Stations for Analysis**

To ensure geographical and environmental diversity, we selected **4 representative stations** from the Beijing region:

1. **Guanyuan** – ️ *Urban*
- **Location**: Central Beijing
- **Why**: Represents dense urban traffic and pollution load.

2. **Shunyi** –  *Suburban*
- **Location**: Northeast suburb of Beijing
- **Why**: Shows suburban growth and industrial influence.

3. **Changping** – ️ *Semi-Rural*
- **Location**: Northern fringe of Beijing
- **Why**: Useful for comparing urban vs agricultural pollution sources.

4. **Dingling** –  *Rural/Historic*
- **Location**: Near mountains, north Beijing
- **Why**: Offers a cleaner environment for baseline comparison.

---

This selection allows us to compare **urban vs rural**, **high vs low pollution**, and understand **geospatial air quality trends**.

---

## Map

![Air Pollution China Map](https://aqli.epic.uchicago.edu/wp-content/uploads/2021/02/China_2023-screen-shot.png)

""", unsafe_allow_html=True)

# ------------------ 🚀 Run the App ------------------ #
app = MultiApp()
app.add_app("📄 Data Overview", data_overview.app)
app.add_app("📊 Exploratory Data Analysis", eda.app)
app.add_app("🤖 Model Training", model.app)
app.add_app("📈 Predict AQI", prediction.app)
app.run()
