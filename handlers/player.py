from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client
from config import Config
from utilities.youtube import search_youtube, download_audio
from utilities.decorators import auth_only

@Client.on_message(filters.command("play") & filters.group)
@auth_only
async def play_music(client: Client, message: Message):
    if not message.from_user:
        return
    
    if len(message.command) < 2:
        await message.reply_text("❗ Please provide a song name or YouTube URL.")
        return
    
    query = " ".join(message.command[1:])
    
    try:
        # Search YouTube
        song_info = await search_youtube(query)
        if not song_info:
            await message.reply_text("❌ No results found.")
            return
        
        # Download audio
        file_path = await download_audio(song_info['url'])
        
        # Add to queue (implementation depends on your queue system)
        # await add_to_queue(message.chat.id, song_info, file_path)
        
        await message.reply_text(f"🎵 Added to queue: {song_info['title']}")
        
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")

@Client.on_message(filters.command("skip") & filters.group)
@auth_only
async def skip_track(client: Client, message: Message):
    # Implement your skip logic here
    await message.reply_text("⏭ Skipped current track.")

@Client.on_message(filters.command("pause") & filters.group)
@auth_only
async def pause_music(client: Client, message: Message):
    # Implement pause logic
    await message.reply_text("⏸ Playback paused.")

@Client.on_message(filters.command("resume") & filters.group)
@auth_only
async def resume_music(client: Client, message: Message):
    # Implement resume logic
    await message.reply_text("▶ Playback resumed.")