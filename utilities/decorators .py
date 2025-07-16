from pyrogram.types import Message
from pyrogram import Client
from functools import wraps
from config import Config

def auth_only(func):
    @wraps(func)
    async def wrapper(client: Client, message: Message):
        if not message.from_user:
            return
        
        # Check if user is auth or admin
        if message.from_user.id in Config.SUDO_USERS or message.from_user.id == Config.OWNER_ID:
            return await func(client, message)
        
        # Implement your auth check logic here
        # if is_user_auth(message.from_user.id, message.chat.id):
        #    return await func(client, message)
        
        await message.reply_text("❌ You are not authorized to use this command.")
    return wrapper

def admin_only(func):
    @wraps(func)
    async def wrapper(client: Client, message: Message):
        if not message.from_user:
            return
        
        if message.from_user.id in Config.SUDO_USERS or message.from_user.id == Config.OWNER_ID:
            return await func(client, message)
        
        await message.reply_text("❌ This command is only for admins.")
    return wrapper