import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from random import  choice, randint

#writing by teto @G_7_Rr          
                
@app.on_message(filters.command(["السورس","ياسورس","مبرمج السورس","مطور السورس"],""))
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/862ce6e007a09bfd9d2a8.mp4",
        caption=f"""˛ ╭──── • ◈ • ────╮
么 [𝚂𝙾𝚄𝚁𝙲𝙴:𝙼𝚁 . 𝚇](https://t.me/zzxxue)
么 [𝙼𝚁 . 𝚇](https://t.me/W_9_9_9)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 
    سـورس مـيوزك مستر اكس 
• My Official Channel 💚
• I post here Source & New Updates
• My official account Dev¹ : @W_9_9_9 
.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙼𝚁 . 𝚇", url=f"https://t.me/W_9_9_9"), 
                 ],[
                   InlineKeyboardButton(
                        "𝚂𝙾𝚄𝚁𝙲𝙴:𝙼𝚁 . 𝚇", url=f"https://t.me/zzxxue"),
                ],

            ]

        ),

    )
    
