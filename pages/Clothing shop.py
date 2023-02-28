import numpy as np
import pandas as pd
import streamlit as st

images = pd.read_csv(r'./product_images.csv')
images = images.to_numpy()
labels = pd.read_csv(r'./true_label.csv')
labels = labels.to_numpy()
labeldic = {0: "T-shirt", 1: "Trouser", 2: "Pullover", 3: "Dress", 4: "Coat", 5: "Sandal", 6: "Shirt", 7: "Sneaker", 8: "Bag", 9: "Ankle boot"}
labelkey = {"T-shirt":0, "Trouser":1, "Pullover":2, "Dress":3, "Coat":4, "Sandal":5, "Shirt":6, "Sneaker":7, "Bag":8, "Ankle boot":9}

st.set_page_config(
    page_title="Clothing Shop",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "ballon" not in st.session_state:
    st.balloons()
    st.session_state['ballon'] = True

        
st.markdown('''
            # Clothing Shop 🛒
            ''')
                
st.sidebar.header("Feel free to browse clothes and add favorites to your cart!")
tabs = st.tabs([" All "]+list(labeldic.values()))


if "cart" not in st.session_state:
    st.session_state.cart = []
if "shown" not in st.session_state:
    st.session_state.shown = []
if "reclst" not in st.session_state:
    st.session_state.reclst = []
        
col_num, row_num = 5, 8


for tabidx, tab in enumerate(tabs):
    with tab:
        showname = str(tabidx) +"showlst"
        if showname not in st.session_state:
            if tabidx==0:
                # showlst = np.random.randint(0, len(images), size=(col_num*row_num))
                showlst = np.random.choice(np.setdiff1d(np.array(range(8000)), np.array(st.session_state.shown)), size = col_num*row_num, replace=False)
            else:
                showlst = np.random.choice(np.setdiff1d((labels==(tabidx-1)).nonzero()[0], np.array(st.session_state.shown)), size=col_num*row_num, replace=False)
            st.session_state.shown.extend(list(showlst))
            st.session_state[showname] = showlst
        else:
            showlst = st.session_state[showname]
        # st.write(showlst)
        cols = st.columns(col_num)
        for col_idx, col in enumerate(cols):
            with col:
                for i in range(row_num):
                    # pic_idx = showlst[col_idx*row_num+i]
                    # st.write(col_num*i+col_idx)
                    pic_idx = showlst[col_num*i+col_idx]
                    st.image(255-images[pic_idx].reshape(28,28), width=150)
                    if pic_idx in st.session_state.cart:
                        agree = st.checkbox(label="  I   Like   it   ❤️", value= True, key=showname +str(pic_idx))
                    else:
                        agree = st.checkbox(label="  I   Like   it   ❤️", value= False, key=showname +str(pic_idx))
                    if agree and pic_idx not in st.session_state.cart:
                        st.session_state.cart.append(pic_idx)
                        st.experimental_rerun()
                    elif not agree and pic_idx in st.session_state.cart:
                        if st.session_state.cart.index(pic_idx)<len(st.session_state.reclst):
                            st.session_state.reclst.pop(st.session_state.cart.index(pic_idx))
                        st.session_state.cart.remove(pic_idx)
                        st.experimental_rerun()
                        

# st.button("Refresh for me!", key="refresh")