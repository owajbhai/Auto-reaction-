from os import environ

API_HASH = environ.get("API_HASH", "72cc7062951f56abb5240994690e49de")
API_ID = int(environ.get("API_ID", "25811007"))
BOT_TOKEN = environ.get("BOT_TOKEN", "7789014828:AAHCFG1-ZswdY8nJUAC4HAwnUrT3O0GWxjE")
BOT_OWNER = int(environ.get("BOT_OWNER", "7240555847"))
BOT_USERNAME = environ.get("BOT_USERNAME", "tymchomapbot")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002236728519"))
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002271972643"))
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://nguyenkhactam5:q1231234@cluster0.srj0a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Define default emojis list
EMOJIS = [
    "👍", "🤷‍♂", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", 
    "🥶", "🤩", "🥳", "😎", "🙏", "👌", "🤣", "😇", "🥱", "🥴", "😍", "🤓", 
    "❤‍🔥", "🌚", "😐", "💯", "🦄", "⚡", "👾", "🏆", "💔", "🤨", "🌟", "😡", 
    "👅", "🆒", "😘", "😈", "😴", "😭", "👻", "🌈", "👨‍💻", "👀", "🎃", "🙄", 
    "🤧", "😨", "🤝", "🤐", "🤗", "🫡", "🤭", "🥸", "🤫", "😶‍🌫", "🤪", "😏"
]
