import streamlit as st
import pandas as pd
import numpy as np

import build_ui as UI
import authentication
import search

username, auth = authentication.go()
status = "Logged in as u/" + username
if username:
    sort_selection, query_num, query = UI.build()
    success = st.success(status)
    if query != "":
        search.q(auth, query, sort_selection, query_num)

else: 
    fail = st.warning("Authentication error. Check your .env file.")




