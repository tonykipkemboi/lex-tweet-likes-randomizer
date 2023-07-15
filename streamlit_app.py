import streamlit as st
from utils.twitter_api import get_liking_users
from utils.db import create_users_table, get_random_user
import requests
import streamlit.components.v1 as components

st.set_page_config(page_icon="💰", page_title="", layout='wide')


@st.cache_data
def get_tweet_html(tweet_url):
    """
    Returns the HTML for embedding a tweet.
    """
    response = requests.get(
        "https://publish.twitter.com/oembed",
        params={"url": tweet_url},
    )
    return response.json()["html"]


if __name__ == "__main__":
    st.markdown("<h1 style='text-align: center; color: red; font-size: 100px; font-family: sans-serif, Arial, Verdana;'>🎡 Mr. Beast's Twitter Challenge!</h1>",
                unsafe_allow_html=True)
    st.divider()

    # Ensure that the "users" table exists in the database
    create_users_table()

    tweet_id = st.secrets.twituh.TWEET_ID
    bearer_token = st.secrets.twituh.BEARER_TOKEN

    col1, col2 = st.columns([1, 2])

    with col1:
        st.info('💬 :red[The Tweet]')
        tweet_url = f"https://twitter.com/lexfridman/status/{tweet_id}"
        tweet_html = get_tweet_html(tweet_url)
        components.html(tweet_html, height=600)

    with col2:
        st.info('🚥 :red[Play!]')
        tweet_id = st.text_input(
            "Enter the Tweet ID:", value=tweet_id, type='password')
        bearer_token = st.text_input(
            "Enter your Twitter Bearer Token:", value=bearer_token, type="password")

        if st.button("Select Random Liker"):
            if not tweet_id or not bearer_token:
                st.warning(
                    "Please provide both Tweet ID and Twitter Bearer Token.")
            else:
                get_liking_users(tweet_id, bearer_token)
                user = get_random_user()
                if user:
                    st.success(
                        f"The winner is: :red[{user['name']} (@{user['username']})]! 🙌", icon="✅")
                    st.balloons()
    st.divider()
