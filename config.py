import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "19413864"))
API_HASH = getenv("API_HASH", "9e33b9fdf4b840a508be5706104737eb")

BOT_TOKEN = getenv("BOT_TOKEN", None)

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://hunter:hunterop@cluster0.yffzly7.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001821513964")
MUSIC_BOT_NAME = getenv("TBH MUSIC")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5613961045").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Jatindalal875/AnonXMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TEAM_CREMINAL")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/ll_TEAM_CREMINALS_ll")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "18000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "18000"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "240")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "20"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "450"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "450"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/66626cf2dd436cb641242.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://graph.org/file/936936ebde1fb0432405e.jpg",
)

PLAYLIST_IMG_URL = "https://graph.org/file/a9bbcb336d7fa85ea8d2b.jpg"

GLOBAL_IMG_URL = "https://graph.org/file/66626cf2dd436cb641242.jpg"

STATS_IMG_URL = "https://graph.org/file/a9bbcb336d7fa85ea8d2b.jpg"

TELEGRAM_AUDIO_URL = "https://graph.org/file/66626cf2dd436cb641242.jpg"

TELEGRAM_VIDEO_URL = "https://graph.org/file/936936ebde1fb0432405e.jpg"

STREAM_IMG_URL = "https://graph.org/file/a9bbcb336d7fa85ea8d2b.jpg"

SOUNCLOUD_IMG_URL = "https://graph.org/file/66626cf2dd436cb641242.jpg"

YOUTUBE_IMG_URL = "https://graph.org/file/936936ebde1fb0432405e.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/a9bbcb336d7fa85ea8d2b.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/66626cf2dd436cb641242.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/936936ebde1fb0432405e.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://graph.org/file/936936ebde1fb0432405e.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://graph.org/file/66626cf2dd436cb641242.jpg"
