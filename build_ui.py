import streamlit as st
import pandas as pd
import numpy as np

def build ():

    st.set_page_config(layout="wide")
    
    st.title('Reddit Scraper')
    if st.button("Clear cache", type="tertiary"):
        st.cache_data.clear()

    col1, col2 = st.columns(2)
    sort_types = ["Best", "Hot", "New", "Top", "Rising"]
    with col1:
        sort_selection = st.segmented_control("Sorting Mode", sort_types, default="Best")
    with col2:
        query_num = st.number_input("Number of results", 1, 100)

    query = st.text_input("Query")

    return (sort_selection, query_num, query)