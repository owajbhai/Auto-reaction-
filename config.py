import os
from typing import List

API_ID = os.environ.get("API_ID", "23621595")
API_HASH = os.environ.get("API_HASH", "de904be2b4cd4efe2ea728ded17ca77d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7675882405:AAHYIOpMI6xyrMqUEGuf9IIxJ-wcPy5FDTU")
ADMIN = int(os.environ.get("ADMIN", "1249672673"))
PICS = (os.environ.get("PICS", "")).split()

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001860172104"))

DB_URI = os.environ.get("DB_URI", "Cluster0")
DB_NAME = os.environ.get("DB_NAME", "mongodb+srv://Botmaster2ndmongo:Botmaster2ndmongo@cluster0737374838.gbhwiw2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0737374838")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002046895970").split())) # Add Multiple channel ids

EMOJIS = [
    "👍", "❤️", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "😢",
    "🎉", "🤩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🤷‍♂️",
    "❤️‍🔥", "🌚", "💯", "🤣", "⚡", "🏆", "🗿", "😐", "🤨", "🍾",
    "💋", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🙈", "🤷‍♀️",
    "😇", "🤝", "✍️", "🤗", "🫡", "😨", "🧑‍🎄", "🎄", "⛄", "🤪",
    "🆒", "💘", "🙊", "🦄", "😘", "🙉", "💊", "😎", "👾", "🤷"
]
