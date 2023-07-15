import requests
import time
from .db import insert_users, create_connection
import streamlit as st


def get_liking_users(tweet_id, bearer_token):
    url = f"https://api.twitter.com/2/tweets/{tweet_id}/liking_users"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json",
    }

    # pagination_token = None

    # for _ in range(5):  # Maximum of 5 requests per 15 minutes
    #     params = {}
    #     if pagination_token:
    #         params['pagination_token'] = pagination_token

    #     try:
    #         resp = requests.get(url, headers=headers, params=params)
    #         resp.raise_for_status()
    #     except requests.exceptions.HTTPError as errh:
    #         st.error(f"HTTP Error: {errh}")
    #         return []
    #     except requests.exceptions.ConnectionError as errc:
    #         st.error(f"Error Connecting: {errc}")
    #         return []
    #     except requests.exceptions.Timeout as errt:
    #         st.error(f"Timeout Error: {errt}")
    #         return []
    #     except requests.exceptions.RequestException as err:
    #         st.error(f"Something went wrong: {err}")
    #         return []

    #     data = resp.json()
    #     insert_users(data['data'])

    #     # Check if there's more data to retrieve
    #     if 'meta' in data and 'next_token' in data['meta']:
    #         pagination_token = data['meta']['next_token']
    #     else:
    #         break

    #     # Sleep to respect rate limit (assuming all requests are made back-to-back)
    #     time.sleep(15 * 60 / 5)
    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        st.error(f"HTTP Error: {errh}", icon="🚨")
        return []
    except requests.exceptions.ConnectionError as errc:
        st.error(f"Error Connecting: {errc}", icon="🚨")
        return []
    except requests.exceptions.Timeout as errt:
        st.error(f"Timeout Error: {errt}", icon="🚨")
        return []
    except requests.exceptions.RequestException as err:
        st.error(f"Something went wrong: {err}", icon="🚨")
        return []

    data = resp.json()
    conn = create_connection()
    if conn is not None:
        insert_users(conn, data['data'])
    else:
        st.error("Failed to create database connection.", icon="🚨")
