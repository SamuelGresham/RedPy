import requests
import requests.auth
import os 
from dotenv import load_dotenv
import streamlit as st

@st.cache_data
def go ():
    # Load the .env file
    load_dotenv()

    # Load .env variables into storage
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_SECRET")
    username = os.getenv("REDDIT_USERNAME")
    password = os.getenv("REDDIT_PASSWORD")

    # Set up initial authentication header
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

    # Set up username and password for authentication
    data = {
        'grant_type': 'password',
        'username': username,
        'password': password
    }

    # Apparently this header needs to be unique in order for the API to accept the request
    headers = {'User-Agent': 'PillScrape/0.0.1'}

    # Make initial auth request and add the token to future request headers
    try: 
        res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
        TOKEN = res.json()['access_token']
        headers['Authorization'] = f'bearer {TOKEN}'

        # Make a test request
        res = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
        data = res.json()
    except: 
        return 0
    else:
        return (username, auth)