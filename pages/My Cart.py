import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from collections import Counter
from sklearn.neighbors import KNeighborsClassifier


images = pd.read_csv(r'./product_images.csv')
images = images.to_numpy()
images = np.r_[images, [np.zeros_like(images[0])]]

labels = pd.read_csv(r'./true_label.csv')
labels = labels.to_numpy()
labeldic = {0: "T-shirt", 1: "Trouser", 2: "Pullover", 3: "Dress", 4: "Coat", 5: "Sandal", 6: "Shirt", 7: "Sneaker", 8: "Bag", 9: "Ankle boot"}
labelkey = {"T-shirt":0, "Trouser":1, "Pullover":2, "Dress":3, "Coat":4, "Sandal":5, "Shirt":6, "Sneaker":7, "Bag":8, "Ankle boot":9}

res = np.loadtxt('pre_label.csv')

if "cart" not in st.session_state:
    st.session_state.cart = []
if "shown" not in st.session_state:
    st.session_state.shown = []
if "reclst" not in st.session_state:
    st.session_state.reclst = []
    
st.set_page_config(
    page_title="My Cart",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.header("Organize your cart as needed and get recommendations!")
st.markdown('''
            # My Cart ❤️
            ''')
cart = st.session_state.cart.copy()
with st.expander("Click here to expand /collapsed my shopping cart", expanded= True):
    
    col_num, row_num = 5, len(cart)//5
    if len(cart)%5!=0:
        row_num+=1
    for i in range(len(cart), col_num*row_num):
        cart.append(10000)
    cols = st.columns(col_num)
    for col_idx, col in enumerate(cols):
        with col:
            for i in range(row_num):
                # pic_idx = cart[col_idx*row_num+i]
                pic_idx = cart[col_num*i+col_idx]
                st.image(255-images[pic_idx].reshape(28,28,1), width=150)
                if pic_idx!=10000:
                    if pic_idx in st.session_state.cart:
                        agree = st.checkbox(label="  I   Like   it   ❤️", value= True, key="cart"+str(pic_idx))
                    else:
                        agree = st.checkbox(label="  I   Like   it   ❤️", value= False, key="cart"+str(pic_idx))
                    if agree and pic_idx not in st.session_state.cart:
                        st.session_state.cart.append(pic_idx)
                        st.experimental_rerun()
                    elif not agree and pic_idx in st.session_state.cart:
                        st.session_state.reclst.pop(st.session_state.cart.index(pic_idx))
                        # if pic_idx in st.session_state.reclst:
                            # st.write(st.session_state.cart.index(pic_idx))
                        st.session_state.cart.remove(pic_idx)
                        st.experimental_rerun()
                        

    
st.markdown('''
            # Guess you like ⭐
            ''')
reclst = st.session_state.reclst.copy()
with st.expander("Click here to expand /collapsed recommendation", expanded= True):

    for obj in st.session_state.cart[len(reclst):]:
        samelst = list(np.setdiff1d(np.argwhere(res==res[obj]).flatten(), np.array(st.session_state.shown)))
        diff = images[samelst] - images[obj]
        recorder = np.argsort(np.sum(diff*diff, axis=1))
        for recidx in recorder[:1]:
            reclst.append(samelst[recidx])
        st.session_state.shown.extend(reclst)
        
    st.session_state.reclst = reclst.copy()
    # if len(st.session_state.cart)!=0:
        # likeclass = sorted(Counter(res[st.session_state.cart]).items(), key= lambda x:x[1], reverse= True)[0][0]
        # st.write(Counter(res[st.session_state.cart]))
        # st.write(likeclass)
        # reclst.extend(np.random.choice(np.setdiff1d(np.argwhere(res==likeclass).flatten(), np.array(st.session_state.shown)), size=3, replace= False))
    # st.session_state.shown.extend(reclst)   
    
    col_num, row_num = 5, len(reclst)//5
    if len(reclst)%5!=0:
        row_num+=1
    for i in range(len(reclst), col_num*row_num):
        reclst.append(10000)
    cols = st.columns(col_num)
    for col_idx, col in enumerate(cols):
        with col:
            for i in range(row_num):
                # pic_idx = cart[col_idx*row_num+i]
                pic_idx = reclst[col_num*i+col_idx]
                st.image(255-images[pic_idx].reshape(28,28,1), width=150)
                if pic_idx!=10000:
                    if pic_idx in st.session_state.cart:
                        agree = st.checkbox(label="  I   Like   it   ❤️", value= True, key="rec"+str(pic_idx))
                    else:
                        agree = st.checkbox(label="  I   Like   it   ❤️", value= False, key="rec"+str(pic_idx))
                    if agree and pic_idx not in st.session_state.cart:
                        st.session_state.cart.append(pic_idx)
                        st.experimental_rerun()
                    elif not agree and pic_idx in st.session_state.cart:
                        st.session_state.reclst.pop(st.session_state.cart.index(pic_idx))
                        st.session_state.cart.remove(pic_idx)
                        # st.session_state.shown.remove(pic_idx)
                        st.experimental_rerun()
                        
# st.write(st.session_state.cart)
# st.write(st.session_state.reclst)

        
        
    
