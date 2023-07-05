import numpy as np
import pandas as pd
import streamlit as st
import base64
import sys
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# st.markdown(
        # f"""
        #  <style>
        #  .stApp {{
        #      background-image: url("https://e0.pxfuel.com/wallpapers/913/661/desktop-wallpaper-artificial-intelligence-business-analytics.jpg");
        #      background-attachment: fixed;
        #      background-size: cover
        #  }}
        #  </style>
        #  """,
        # unsafe_allow_html=True)
with open('pic.jpg', "rb") as image_file:        
# with open('/home/phantom/Desktop/Project 3/pic.jpg', "rb") as image_file:        
        encoded_string = base64.b64encode(image_file.read())
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )        

# Web App Title
st.markdown('''
# **The EDA App**
A Smart Way to analyse your data
''')

# Upload CSV data
st.header('Upload your CSV file or use Example Dataset')
uploaded_file = st.file_uploader(
    "Upload your input CSV file", type=["csv"])

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**App is preparing your Report, Please Wait**')
    st_profile_report(pr)

else:
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache_data
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**App is Profiling Report, Please Wait**')
        st_profile_report(pr)
