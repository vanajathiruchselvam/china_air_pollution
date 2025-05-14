# multiapp.py
import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Sidebar selectbox (not radio)
        app_titles = [app["title"] for app in self.apps]
        selected_app = st.sidebar.selectbox("Navigation", app_titles)

        # Run the selected app
        for app in self.apps:
            if app["title"] == selected_app:
                app["function"]()

