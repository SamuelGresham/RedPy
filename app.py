import streamlit as st
import pandas as pd
import numpy as np

import build_ui as UI
import authentication
import search

st.session_state["cache_updated"] = False

username, auth = authentication.go()
status = "Logged in as u/" + username
if username:
    sort_selection, query_num, query = UI.build()

    # Check if the cache was updated.
    # If the cache was updated, that means the user was (re-)authenticated and the authentication message should show.
    if st.session_state.get("cache_updated", False):
        success = st.toast(status, icon="✅")
        st.session_state["cache_updated"] = False


    if query != "":
        search.q(auth, query, sort_selection, query_num)

    

else: 
    fail = st.warning("Authentication error. Check your .env file.")




