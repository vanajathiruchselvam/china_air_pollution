import streamlit as st

# Set page config FIRST
st.set_page_config(
    page_title="China Air Pollution Dashboard",
    layout="wide"
)

from multiapp import MultiApp
from pages import home, data_overview, eda, model, prediction  # Ensure home is imported

# Background and style
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

# Set up multi-page app
app = MultiApp()
app.add_app("🏠 Home", home.app)
app.add_app("📄 Data Overview", data_overview.app)
app.add_app("📊 Exploratory Data Analysis", eda.app)
app.add_app("🤖 Model Training", model.app)
app.add_app("📈 Predict AQI", prediction.app)
app.run()
