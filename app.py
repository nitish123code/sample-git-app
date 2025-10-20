import streamlit as st

st.title("Campusx")

col1,col2=st.columns(2)

with col1:
    st.image(r"Screen+Shot+2023-08-17+at+3.09.40+PM.webp")

with col2:
    st.header("CampusX is an Indian ed-tech company founded by Nitish Singh that offers online courses and mentorship programs in data science and machine learning. The company provides free educational content on its YouTube channel, with more in-depth, paid programs available on its website.")    
st.header("Course")
st.subheader("DSMP")
st.subheader("DAMP")
st.subheader("DEMP")
st.subheader('DSA')

st.sidebar.title('Menu')
st.sidebar.markdown("""
-Home
-About
-Contact
-Carrer
-Login
""")