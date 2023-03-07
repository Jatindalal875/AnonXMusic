import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://gyanimusic:GyaniMusic@cluster0.dl60qho.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "⏤͟͞𝑻𝑩𝑯 ダ ᴍᴜsɪᴄ")

OWNER_ID = list(map(int, getenv("OWNER_ID", "1356469075").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Jatindalal875/AnonXMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/THE_BROTHERHOOD_COUNCIL")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/EAGLE_MAFIA_CLUB")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

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


START_IMG_URL = getenv("START_IMG_URL", "")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "",
)

PLAYLIST_IMG_URL = "<a href='https://www.uhdpaper.com/2019/10/sci-fi-digital-art-8k-4956.html'><img src='https://1.bp.blogspot.com/-DzFjO7LHgQw/XZqAwMnS-yI/AAAAAAAAPGw/qrwBZiox-BwKV3aZgk1s3wMvoqSfg_t0gCLcBGAsYHQ/w919-h516-p-k-no-nu/sci-fi-digital-art-uhdpaper.com-8K-4.956-wp.thumbnail.jpg'/></a> <br/>HD Resolution Visit <a href='https://www.uhdpaper.com/2019/10/sci-fi-digital-art-8k-4956.html'>https://www.uhdpaper.com/2019/10/sci-fi-digital-art-8k-4956.html</a>"

GLOBAL_IMG_URL = "https://wallpapershome.com/images/pages/pic_h/12769.jpg"

STATS_IMG_URL = "https://images.hdqwalls.com/download/space-digital-art-8k-2h-7680x4320.jpg"

TELEGRAM_AUDIO_URL = "https://images.hdqwalls.com/wallpapers/astronaut-black-hole-galaxy-space-4k-a0.jpg"

TELEGRAM_VIDEO_URL = "https://wallpapershome.com/images/wallpapers/space-2560x1440-planet-man-dog-4k-19737.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"

YOUTUBE_IMG_URL = "https://i.pinimg.com/originals/ee/ff/43/eeff43c6e8ced2d1f761a8d64ac85312.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://martech.org/wp-content/uploads/2017/09/spotify-logo-1920x1080.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://techcrunch.com/wp-content/uploads/2021/02/alexander-shatov-JlO3-oY5ZlQ-unsplash.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://techcrunch.com/wp-content/uploads/2021/02/alexander-shatov-JlO3-oY5ZlQ-unsplash.jpg"


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
            PING_IMG_URL = "https://cdn.siasat.com/wp-content/uploads/2022/06/New-Project-49.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://static.tnn.in/photo/msid-98430822,imgsize-955840,updatedat-1678019651280,width-1900,height-1400,resizemode-75/98430822.jpg"
