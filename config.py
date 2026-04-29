import os
from os import getenv

API_ID = int(os.environ.get(28590286, ""))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("6a68cc6b41219dc57b7a52914032f92f", "")
BOT_TOKEN = os.environ.get("8021113365:AAGQjYo5uaSEsZbycIRXEw-W1NLpZ6Om2KQ", "")

OWNER_ID = int(os.environ.get("6117445553", ""))  # Your Telegram user ID
#SUDO_USERS = list(map(int, os.environ.get("5424499713", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("mongodb+srv://Kailash979933:Lions98@cluster0.af4v4ge.mongodb.net/?appName=Cluster0", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
#CHANNEL_ID = int(os.environ.get("-1002656878420", "-"))  # Telegram channel ID (with -100 prefix)

#PREMIUM_LOGS = os.environ.get("5424499713", "")  # Optional here you'll get all logs
