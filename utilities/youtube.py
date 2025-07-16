import yt_dlp
from config import Config
import asyncio

async def search_youtube(query: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'extract_flat': True,
        'noplaylist': True,
        'default_search': 'ytsearch'
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)
            if not info or 'entries' not in info or not info['entries']:
                return None
            
            entry = info['entries'][0]
            return {
                'title': entry.get('title', 'Unknown Title'),
                'url': entry.get('url'),
                'duration': entry.get('duration', 0),
                'thumbnail': entry.get('thumbnails', [{}])[0].get('url')
            }
        except Exception as e:
            print(f"Error searching YouTube: {e}")
            return None

async def download_audio(url: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f"{Config.SONG_DOWNLOAD_DIR}/%(title)s.%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')
        return file_path