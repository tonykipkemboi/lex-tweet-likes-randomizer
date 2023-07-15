"""DB functions module"""

import sqlite3
import streamlit as st
from sqlite3 import Error


def create_connection():
    conn = None
    try:
        # create a memory database for testing
        conn = sqlite3.connect('twitter_likes.db')
        st.success(
            f'successful connection with sqlite version {sqlite3.version}')
    except Error as e:
        st.error(e, icon="🚨")
    if conn:
        return conn
    else:
        return None


def create_users_table():
    conn = sqlite3.connect('twitter_likes.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT,
            username TEXT
        )
    ''')

    conn.commit()
    conn.close()


def insert_users(conn, users):
    cur = conn.cursor()
    for user in users:
        cur.execute("INSERT OR IGNORE INTO users(id, name, username) VALUES(?, ?, ?)",
                    (user['id'], user['name'], user['username']))
    conn.commit()


def get_random_user():
    conn = sqlite3.connect('twitter_likes.db')
    c = conn.cursor()

    c.execute('SELECT * FROM users ORDER BY RANDOM() LIMIT 1')
    user = c.fetchone()

    conn.close()

    if user is None:
        return None
    else:
        return {'id': user[0], 'name': user[1], 'username': user[2]}
