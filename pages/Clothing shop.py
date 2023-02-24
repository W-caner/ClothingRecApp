import numpy as np
import pandas as pd
import streamlit as st

images = pd.read_csv(r'./product_images.csv')
images = images.to_numpy()
labels = pd.read_csv(r'./true_label.csv')
labels = labels.to_numpy()
labeldic = {0: "T-shirt", 1: "Trouser", 2: "Pullover", 3: "Dress", 4: "Coat", 5: "Sandal", 6: "Shirt", 7: "Sneaker", 8: "Bag", 9: "Ankle boot"}

st.set_page_config(
    page_title="Clothing Shop",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.balloons()

st.markdown("# Plotting Demo")
# st.sidebar.header("Plotting Demo")

tabs = st.tabs([" All "]+list(labeldic.values()))
cols = st.columns(4)
showlst = np.random.randint(0, len(images), size=(16))
for col in cols:
    with col:
        for i in range(4):
            st.image(255-images[showlst[i]].reshape(28,28),width=150)
        
# with col2:
#     st.image(images[0].reshape(28,28),width=100)