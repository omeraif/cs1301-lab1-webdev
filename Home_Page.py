import streamlit as st

st.set_page_config(page_title="Ömer Raif Özoglu | CS 1301 Lab 1", page_icon="📌", layout="centered")

st.title("Ömer Raif Özoglu — CS 1301")
st.subheader("Web Development Lab 1")

st.write(
    "Welcome! Use the sidebar to navigate between pages."
)

st.markdown(
    '''
1. **Portfolio**: A quick overview of me, my interests, and what I'm working on.
2. **Quiz**: An interactive quiz with images that gives you a result at the end.
'''
)

st.info("Make sure the app is **public** when you deploy on Streamlit Community Cloud.")
