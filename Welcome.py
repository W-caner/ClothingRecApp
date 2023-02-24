import streamlit as st
import numpy as np
import pandas as pd

import streamlit as st

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.write("# Welcome to Clothing-Rec App! 🎉")

# st.sidebar.success("Select a demo above.")
st.markdown(
    """
    Clothing-Rec App is an open-source app built by streamlit, which that can be viewed as a simple demo of the online shopping platform,
     with recommendations using the K-means and the K-nearest neighbor algorithm.
    
    **👈 Switching tabs from the sidebar** to see  of what Streamlit can do!
    ### Want can you do?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more information!
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    
    # [GETTING START NOW!](http://localhost:8501/Clothing_shop)
"""
)
