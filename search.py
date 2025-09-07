import requests
import streamlit as st

## Components --------------------------------------

@st.dialog("Post")
def post_modal(post_title, post_text, post_img): 
    st.markdown("## " + post_title)
    st.markdown(post_text)
    if post_img:
        st.image(post_img)

## -------------------------------------------------

def q (auth, query, sort_mode, num):
    data = {
        'q': query,
        'sort': sort_mode.lower(),
        't': 'all'
    }

    # Apparently this header needs to be unique in order for the API to accept the request
    headers = {'User-Agent': 'PillScrape/0.0.1'}

    res = requests.get('https://www.reddit.com/search.json', auth=auth, params=data, headers=headers)

    st.text(sort_mode)

    # data = res.json()
    children = res.json()["data"]["children"]

    

    for post in children:
        col1, col2, col3, col4 = st.columns([0.5, 1, 0.5, 0.18])
        post_data = post["data"]
        title = post_data["title"]
        author = post_data["author"]
        url = post_data["permalink"]
        subreddit = post_data["subreddit"]

        if str(post["data"]["url"])[-1] != "/":
            img_arg = post["data"]["url"]
        else: 
            img_arg = False
        

        with col1:
            st.container().html("<b >r/"+subreddit+"</b>") 
        with col2:
            st.text(title)
        with col3: 
            st.container(horizontal_alignment="center",vertical_alignment="center", border=None).text(author)
        with col4:
            st.container(horizontal_alignment="right",vertical_alignment="center",border=False).button("Open", on_click=post_modal, args=[title, post["data"]["selftext"], img_arg], key=url)

        st.divider()
