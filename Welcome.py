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

# tab1, tab2 = st.columns(2)
# with tab1:
st.write("# Welcome to Clothing-Rec App! 💕")

# st.sidebar.success("Select a demo above.")
st.markdown(
    """
    Clothing-Rec App is an open-source app built by streamlit, which that can be viewed as a simple demo of the online shopping platform,
    with recommendations using the K-means and the K-nearest neighbor algorithm. (Also my Assignment ^_^ )
    
    **👈 Switching tabs from the sidebar** to see  of what Streamlit can do!
    ### Want can you do?
    - Browse and choose clothes, which in the "[Clothing shop](https://w-caner-clothingrecapp-welcome-2g8n9r.streamlit.app/Clothing_shop)" tab
    - Mark your favorite clothes to the cart, or remove it, which in the "[My cart](https://w-caner-clothingrecapp-welcome-2g8n9r.streamlit.app/My_Cart)" tab
    - Get recommendation, this function also in the "[My cart](https://w-caner-clothingrecapp-welcome-2g8n9r.streamlit.app/My_Cart)" tab
    ### See more information!
    - Series of graphs also provided to show the algorithmic process, visit by clicking the "[Show Analysis](https://w-caner-clothingrecapp-welcome-2g8n9r.streamlit.app/Show_Analysis)" tab
    - The project is open source on github at [https://github.com/W-caner/ClothingRecApp.git](https://github.com/W-caner/ClothingRecApp.git)
    
    # [GETTING START NOW!](https://w-caner-clothingrecapp-welcome-2g8n9r.streamlit.app/Clothing_shop)
"""
)
