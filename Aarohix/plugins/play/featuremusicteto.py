import asyncio


import random


from AarohiX import app


from pyrogram.types import (InlineKeyboardButton,


                            InlineKeyboardMarkup, Message)


from pyrogram import filters, Client





@app.on_message(
    filters.command(["المميزات"], "")
& filters.group
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**•   قايمه مميزات سورس  :\n
╮•  المطور
│᚜• سؤال
│᚜• مين في الكول 
│᚜• تفعيل الاذان
│᚜• كت
│᚜• احكام
│᚜• افتح الكول
│᚜• احرف
│᚜• الرابط
│᚜• البنك 
│᚜• منع تصفيه تلقائي
│᚜• رفع مشرف
│᚜• شعر
│᚜• نادي المطور
│᚜• زخرفه
│᚜• مميزات
│᚜• همسه
│᚜• يوت
│᚜• تحميل
│᚜• لو خيروك
│᚜• معلومات الجروب
│᚜• طرد كتم
│᚜• تلكراف ميديا
│᚜• اسكرين 
│᚜• صراحه
│᚜• صور
│᚜• صور بنات 
│᚜• صور شباب
│᚜• السورس 
│᚜• كتم
│᚜• اقتباس
│᚜• هيدرات
│᚜• اذكار 
╯•  بث مباشر للقنوات 
[𝗦𝗼𝘂𝗿𝗰𝗲 𝗠𝗥 . 𝗫](https://t.me/zzxxue) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙼𝚁 . 𝚇", url=f"https://t.me/W_9_9_9"),                        
                 ],[
                InlineKeyboardButton(
                        "close", callback_data="close"),
               ],
          ]
        ),
    )

