import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
from handlers.player import play_music, skip_track, pause_music, resume_music
from handlers.queue import show_queue
from handlers.admin import auth_users
from utilities.decorators import admin_only

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Client(
    "MusicBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# Start command
@app.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    await message.reply_text(
        "🎵 Welcome to Music Bot!\n\n"
        "I can play music in your group's voice chat.\n"
        "Add me to a group and use /play to start music!"
    )

# Help command
@app.on_message(filters.command("help"))
async def help(client: Client, message: Message):
    help_text = """
🎶 **Music Bot Commands:**

▷ /play [song name/url] - Play a song
▷ /skip - Skip current song
▷ /pause - Pause playback
▷ /resume - Resume playback
▷ /queue - Show current queue
▷ /auth - Add auth user (admin only)
▷ /unauth - Remove auth user (admin only)
▷ /authlist - Show auth users
"""
    await message.reply_text(help_text)

# Register handlers
app.add_handler(play_music)
app.add_handler(skip_track)
app.add_handler(pause_music)
app.add_handler(resume_music)
app.add_handler(show_queue)
app.add_handler(auth_users)

if __name__ == "__main__":
    # Create download directory if not exists
    import os
    if not os.path.exists(Config.SONG_DOWNLOAD_DIR):
        os.makedirs(Config.SONG_DOWNLOAD_DIR)
    
    logger.info("Starting Music Bot...")
    app.run()