# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web_functions import load_data

# Import pages
from tags import home, data, detect  # visualise

# Configure the app
st.set_page_config(
    page_title='Human Stress Detector',
    page_icon=':worried:',
    layout='wide',
    initial_sidebar_state='auto')

# You can customize the colour of output page by going to settings 
# Dictionary for pages
tags = {
    "Home": home,
    "Data Info": data,
    "Detection": detect,
}

# Create a sidebar
# Add title to sidebar
st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(tags.keys()))

# Loading the dataset.
df, x, y = load_data()

# Call the app function of selected page to run
if page in ["Detection"]:
    tags[page].app(df, x, y)
elif page == "Data Info":
    tags[page].app(df)
else:
    tags[page].app()   # type: ignore
