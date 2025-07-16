import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Bot Token
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    
    # Telegram API
    API_ID = int(os.getenv("API_ID", 0))
    API_HASH = os.getenv("API_HASH")
    
    # Database
    MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb://localhost:27017")
    DB_NAME = os.getenv("DB_NAME", "MusicBot")
    
    # Owner and Admins
    OWNER_ID = int(os.getenv("OWNER_ID", 0))
    SUDO_USERS = set(int(x) for x in os.getenv("SUDO_USERS", "").split())
    
    # Music Settings
    DURATION_LIMIT = int(os.getenv("DURATION_LIMIT", 5400))  # 90 minutes
    SONG_DOWNLOAD_DIR = os.getenv("SONG_DOWNLOAD_DIR", "downloads")
    
    # Logging
    LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", 0))
    
    # Performance
    THUMBNAIL = os.getenv("THUMBNAIL", "https://i.imgur.com/4Q34V8u.png")
    COMMAND_PREFIXES = list(os.getenv("COMMAND_PREFIXES", "/ !").split())
    
    # Services
    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
    SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

class Production(Config):
    pass

class Development(Config):
    DEBUG = True