from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config


@app.on_message(
    command(["مطور", "مبرمج السورس", "اكس","مستر اكس"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/77bd924e46880da2b8d38.jpg",
        caption="• Dev Bot ↦ ꪔᖇ . ꪎ \n ━━━━━━━━━━━━ \n • Dev ↦ SoUrce: 𝗠𝗥 . 𝗫 . \n • Bio ↦- 𓏺 Whoever humbles #himself to god will be #exalted 𓏺",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐌𝐑 . 𝐗", url=f"https://t.me/W_9_9_9"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Updates", url=f"https://t.me/zzxxue"
                    ),
                ],
            ]
        ),
    )
