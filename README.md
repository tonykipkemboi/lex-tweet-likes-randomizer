# 🎡 Mr. Beast's Twitter Challenge

Welcome to the Mr. Beast's Twitter Challenge!

This application is a fun project inspired by the famous YouTuber [Mr. Beast](https://twitter.com/MrBeast) and AI researcher [Lex Fridman](https://twitter.com/lexfridman).

This application selects a random user who liked a particular tweet, making it a perfect tool for online Twitter challenges or giveaways.

## ⚙️ How it works

The application uses the Twitter API to fetch the users who have liked a specific tweet and stores them in an SQLite database. When the "Select Random Liker" button is pressed, a random user from the database is chosen as the "winner".

This application is created using Python, Streamlit for the web interface, and SQLite for data storage.

## 🎬 Getting Started

### Prerequisites

- Python 3.7 or above
- Streamlit
- SQLite
- Requests
- A Twitter Developer Account

### Installation

Clone the repository:

```bash
git clone https://github.com/your_username_/MrBeast-Twitter-Challenge.git
cd MrBeast-Twitter-Challenge
```

Install the necessary packages:

```bash
pip install -r requirements.txt
```

### Configuration

In `secrets.toml`, replace `BEARER_TOKEN` and `TWEET_ID` with your actual Twitter Bearer Token and the ID of the tweet you want to analyze.

```toml
[twituh]
BEARER_TOKEN = "YOUR_TWITTER_BEARER_TOKEN"
TWEET_ID = "YOUR_TWEET_ID"
```

### Running the App

To run the app, navigate to the project directory in your terminal and enter:

```bash
streamlit run app.py
```

## 🫸🏾 Limitations

- Twitter API imposes rate limits, which restrict the number of requests you can make within a certain time period.
- Twitter API uses pagination for endpoints that could return large amounts of data, meaning you may need to make multiple requests to fetch all the data.
- SQLite databases are not designed to handle high levels of concurrent read/writes and lack certain features found in other DBMS.
- Twitter's Developer Policy requires that you respect user privacy and not hold onto data longer than necessary.

## ➕ Contributing

Contributions are welcome! 🎉

## 🪪 License

This project is licensed under the terms of the MIT license. See the LICENSE file for details.

## 👍🏾 Acknowledgments

- [Mr. Beast](https://twitter.com/MrBeast), for his fun and creative challenges
- [Lex Fridman](https://twitter.com/lexfridman), for inspiring the project with his use of Python scripts for Twitter challenges
- [Twitter](https://developer.twitter.com/en/docs/twitter-api/tweets/likes/introduction), for their API which makes this project possible

For any questions or comments, please open an issue on this repository.

## ⛔️ Disclaimer

This project is intended for educational and entertainment purposes only. It should not be used for any activities that violate Twitter's terms of service or any local laws. Use responsibly.
