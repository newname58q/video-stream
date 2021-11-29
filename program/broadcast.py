# Copyright (C) 2021 By VeezProject
# Originally written by levina on github
# Broadcast function


import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from driver.veez import user as USER
from driver.veez import bot as BOT
from pyrogram import client as veez
from config import SUDO_USERS


@Client.on_message(filters.command(["gcast"]))
async def broadcast(_, message: Message):
    sent = 0
    failed = 0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("ʙʀᴏᴀᴅᴄᴀꜱᴛ ʙᴀꜱʟᴀᴅɪ...")
        if not message.reply_to_message:
            await wtf.edit("ʟᴜᴛꜰᴇɴ ʏᴀʏɪɴɪ ʙᴀꜱʟᴀᴛᴍᴀᴋ ɪᴄɪɴ ʙɪʀ ᴍᴇꜱᴀᴊᴀ ᴄᴇᴠᴀᴘ ᴠᴇʀɪɴ!")
            return
        lmao = message.reply_to_message.text
        try:
            async for dialog in USER.iter_dialogs():
                try:
                    await BOT.send_message(dialog.chat.id, lmao)
                    sent = sent + 1
                    await wtf.edit(
                        f"ʙʀᴏᴀᴅᴄᴀꜱᴛ... \n\nɢᴏɴᴅᴇʀɪʟᴅɪ: {sent} ᴄʜᴀᴛ \nʙᴀꜱᴀʀɪꜱɪᴢ: {failed} ᴄʜᴀᴛ"
                    )
                    await asyncio.sleep(3)
                except:
                    failed = failed + 1
            await message.reply_text(
                f"ʙʀᴏᴀᴅᴄᴀꜱᴛ ʙᴀꜱᴀʀɪʟɪ \n\nɢᴏɴᴅᴇʀɪʟᴅɪ: {sent} ᴄʜᴀᴛ \nʙᴀꜱᴀʀɪꜱɪᴢ: {failed} chats"
            )
        except:
            pass