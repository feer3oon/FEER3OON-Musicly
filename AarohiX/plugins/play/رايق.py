import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from AarohiX import app
from random import  choice, randint


@app.on_message(filters.command(["جمالي"], ""))
async def madison(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.get_chat_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**⭓ᴍᴜꜱɪᴄ✘ᠻꫀꫀ𝘳3ꪮꪮꪀ♪
╮⦿ هل خلق الجمال لتختصره عيناك اما
│᚜⦿ عيناك خلقت لتقنعني ان لا جمال بعدها
╯⦿ جمال عيناك (60) % ❤️**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
