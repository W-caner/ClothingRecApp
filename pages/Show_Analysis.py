import streamlit as st
st.set_page_config(
    page_title="Show Analysis",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.sidebar.header("Here are some visualizations of the analysis!")
st.markdown('''
            # Show Analysis 📈
            ''')


col1, col2 = st.columns(2)
with col1:
    st.header("Feature extraction methods")
    st.write('1 row: original&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; 2 row: binarization according to threshold')
    st.write('3 row: GRID divition method  &nbsp;  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 4 row: PCA method')
    st.image("./pic/1.png",width=420)
    st.header("Visual clustering")
    st.write('Using TSNE dimension reduction, colors represent different categories.')
    st.image("./pic/2.png", width=420)
with col2:
    st.header("Clustering quality")
    st.write("\n")
    st.image("./pic/3.png")
    st.write('\nThe first line of each category represents the real tag and the original image, and the second line represents the cluster tag and the feature image.')