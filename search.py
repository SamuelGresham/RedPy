import requests
import streamlit as st

def q (auth, query, sort_mode, num):
    data = {
        'q': query,
        'sort': sort_mode,
        't': 'all'
    }

    # Apparently this header needs to be unique in order for the API to accept the request
    headers = {'User-Agent': 'PillScrape/0.0.1'}

    res = requests.get('https://www.reddit.com/search.json', auth=auth, params=data, headers=headers)

    # data = res.json()
    children = res.json()["data"]["children"]

    for post in children:
        post_data = post["data"]
        title = post_data["title"]
        author = post_data["author"]
        url = post_data["permalink"]
        subreddit = post_data["subreddit"]

        st.text(f"[{subreddit}] {title} (by {author}) → https://www.reddit.com{url}")
