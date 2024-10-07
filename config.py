import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from  https://api.imgbb.com/
API_KEY = getenv("API_KEY", "3f121b552c3a7a6f0e63aff1c2a423fc") 

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "24710964"))
API_HASH = getenv("API_HASH", "3649c3709c3f34b64286e0d4db28da9b")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7761474583:AAFppZ7FIH9LTxJluNA_KAhK8J0yof8fn1s")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://luckyxdplaypointer:gluUQD73jLB5vLVi@cluster0.nqh72.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002275427766"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6652287427"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/venombolteop/VenomMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/botcarehub")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/botcarechat")


AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "false")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "BQF5DzQAqxCUvpdOyKxZqGj1YiMURPfOEAa24dKJfjyh5W6oztFFwGnMM7Q9RoVefx0Incs8Lx8pqqOsMTbtbYgc-7BlYJtOib05eZ_U0F7xoA6FwW4tNxOwS5Y0kJvENISXICCqxxxK667MvCO2ExWUqQhOusi7Xbgdv9BgEgnw2xrfdsQkhN3nxHT03oSexbK83mFJSMyHlFptM2MkgWxkEJIgbmss6Jd-JzGX0QUaF6b8_BDGltXgB7AUFP4WI0F6o91kp7FnuDOvA0pHFrbNGXeOBT76GI-Sz2Fidsr2GCggONhqZGZcOAyebJDBJ8L7XDTmAWBZdO3m-KIfE8VY7t6gAAAAG5DdWqAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
