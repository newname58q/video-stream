# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **ʜᴏşɢᴇʟᴅɪɴ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ʏᴇɴɪ ᴛᴇʟᴇɢʀᴀᴍ'ıɴ ɢöʀüɴᴛüʟü ꜱᴏʜʙᴇᴛʟᴇʀɪ ᴀʀᴀᴄıʟığıʏʟᴀ ɢʀᴜᴘʟᴀʀᴅᴀ ᴍüᴢɪᴋ ᴠᴇ ᴠɪᴅᴇᴏ ᴏʏɴᴀᴛᴍᴀɴıᴢᴀ ᴏʟᴀɴᴀᴋ ᴛᴀɴıʀ!**

💡 **📚 ᴋᴏᴍᴜᴛʟᴀʀ ᴅüɢᴍᴇꜱɪɴɪ ᴛıᴋʟᴀʏᴀʀᴀᴋ ʙᴏᴛ'ᴜɴ ᴛüᴍ ᴋᴏᴍᴜᴛʟᴀʀıɴı ᴠᴇ ɴᴀꜱıʟ çᴀʟışᴛıᴋʟᴀʀıɴı öɢʀᴇɴɪɴ!**

🔖 **ʙᴜ ʙᴏᴛᴜɴ ɴᴀꜱıʟ ᴋᴜʟʟᴀɴıʟᴀᴄᴀɢıɴı öɢʀᴇɴᴍᴇᴋ ɪçɪɴ ʟüᴛꜰᴇɴ ᴛıᴋʟᴀʏıɴ » ❓ ʙᴀꜱɪᴛ ᴋᴏᴍᴜᴛʟᴀʀ!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ʙᴇɴɪ ɢʀᴜʙᴜɴᴀ ᴇᴋʟᴇ ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ ʙᴀꜱɪᴛ ᴋᴏᴍᴜᴛʟᴀʀ", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 ᴋᴏᴍᴜᴛʟᴀʀ", callback_data="cbcmds"),
                    InlineKeyboardButton(" ꜱᴀʜɪʙɪ ", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 ʀᴇꜱᴍɪ ɢʀᴜᴘ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 ʀᴇꜱᴍɪ ᴋᴀɴᴀʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **ʙᴜ ʙᴏᴛᴜ ᴋᴜʟʟᴀɴᴍᴀᴋ ɪçɪɴ ᴛᴇᴍᴇʟ ᴀɴʟᴀᴛıᴍ:**
1.) **Öɴᴄᴇ ʙᴇɴɪ ɢʀᴜʙᴜɴᴜᴢᴀ ᴇᴋʟᴇʏɪɴ.**
2.) **ᴏ ᴢᴀᴍᴀɴ ʙᴇɴɪ ʏöɴᴇᴛɪᴄɪ ᴏʟᴀʀᴀᴋ ʏüᴋꜱᴇʟᴛ ᴠᴇ ᴀɴᴏɴɪᴍ ʏöɴᴇᴛɪᴄɪ ʜᴀʀɪç ᴛüᴍ ɪᴢɪɴʟᴇʀɪ ᴠᴇʀ.**
3.) **ʙᴇɴɪ ᴛᴇʀꜰɪ ᴇᴛᴛɪʀᴅɪᴋᴛᴇɴ ꜱᴏɴʀᴀ, ʏöɴᴇᴛɪᴄɪ ᴠᴇʀɪʟᴇʀɪɴɪ ʏᴇɴɪʟᴇᴍᴇᴋ ɪçɪɴ /reload ɢʀᴜᴘᴛᴀ ʏᴀᴢıɴ.**
3.) **ɢʀᴜʙᴜɴᴜᴢᴀ @{ASSISTANT_NAME} ᴇᴋʟᴇʏɪɴ ᴠᴇʏᴀ ᴏɴᴜ ᴅᴀᴠᴇᴛ ᴇᴛᴍᴇᴋ ɪçɪɴ /userbotjoin ʏᴀᴢıɴ.**
4.) **ᴠɪᴅᴇᴏ/ᴍüᴢɪᴋ ᴏʏɴᴀᴛᴍᴀʏᴀ ʙᴀşʟᴀᴍᴀᴅᴀɴ öɴᴄᴇ ɢöʀüɴᴛüʟü ꜱᴏʜʙᴇᴛɪ ᴀçıɴ.**
5.) **ʙᴀᴢᴇɴ /reload ᴋᴏᴍᴜᴛᴜɴᴜ ᴋᴜʟʟᴀɴᴀʀᴀᴋ ʙᴏᴛᴜ ʏᴇɴɪᴅᴇɴ ʏüᴋʟᴇᴍᴇᴋ ʙᴀᴢı ꜱᴏʀᴜɴʟᴀʀı çöᴢᴍᴇɴɪᴢᴇ ʏᴀʀᴅıᴍᴄı ᴏʟᴀʙɪʟɪʀ.**

💡 **ʙᴜ ʙᴏᴛ ʜᴀᴋᴋıɴᴅᴀ ᴛᴀᴋɪᴘ ᴇᴅᴇɴ ʙɪʀ ꜱᴏʀᴜɴᴜᴢ ᴠᴀʀꜱᴀ, ʙᴜɴᴜ ʙᴜʀᴀᴅᴀᴋɪ ᴅᴇꜱᴛᴇᴋ ꜱᴏʜʙᴇᴛɪᴍᴅᴇ ɪʟᴇᴛᴇʙɪʟɪʀꜱɪɴɪᴢ. @jackdanielssx**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 ɢᴇʀɪ", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Merhaba [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**


⚡ __ᴄʀᴇᴀᴛᴏʀ by {BOT_NAME} @jackdanielssx""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 ᴀᴅᴍɪɴ ᴋᴏᴍᴜᴛ", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 ᴄʀᴇᴀᴛᴏʀ ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 ʙᴀꜱɪᴄ ᴋᴏᴍᴜᴛ", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 ɢᴇʀɪ", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 ʙᴀꜱɪᴛ ᴋᴏᴍᴜᴛʟᴀʀ:

» /oynat => ɪꜱᴛᴇᴅɪɢɪɴ şᴀʀᴋıʏı ᴅɪʀᴇᴋ ᴅɪɴʟᴇᴛɪʀ
» /izlet => ɪꜱᴛᴇᴅɪɢɪɴ ꜰɪʟᴍɪ ɪɴᴅɪʀɪᴘ ɪᴢʟᴇᴛɪʀ
» /ara => ᴠɪᴅᴇᴏ ɪɴᴅɪʀɪʀ
» /indir => ᴍᴜꜱɪᴄ ɪɴᴅɪʀɪʀ
ɴᴏᴛ : /izlet ve /oynat ᴋᴏᴍᴜᴛᴜ ᴋᴇɴᴅɪɴɪᴢᴇ ᴀɪᴛ ᴍᴜꜱɪᴄ ᴠᴇ ᴠɪᴅᴇᴏʟᴀʀı ᴅᴀ ᴏʏɴᴀᴛıʀ
⚡️ __ᴄʀᴇᴀᴛᴏʀ {BOT_NAME} @jackdanielssx""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 ɢᴇʀɪ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 ᴀᴅᴍɪɴ ᴋᴏᴍᴜᴛʟᴀʀı:

» /durdur - ꜱᴇꜱᴛᴇ ʙᴏᴛᴜ ᴅᴜʀᴅᴜʀᴜʀ
» /devam - ᴅᴜʀᴅᴜʀᴜʟᴀɴ ʙᴏᴛᴜ ʙᴀşʟᴀᴛıʀ
» /atla - şᴀʀᴋı ᴠᴇ ᴠɪᴅᴇᴏ ᴀᴛʟᴀʀ
» /son - ꜱᴇꜱᴛᴇɴ ᴅüşᴇʀ ʜᴇʀşᴇʏɪ ᴅᴜʀᴅᴜʀᴜʀ
» /reload - ʙᴏᴛᴜ ʏᴇɴɪᴅᴇɴ ʙᴀşʟᴀᴛıᴘ ᴀᴅᴍɪɴ ʟɪꜱᴛᴇꜱɪ ʏᴇɴɪʟᴇʀ
» /Gel - ɢʀᴜʙᴀ ᴋᴀᴛıʟıʀ
» /Git - ɢʀᴜᴘᴛᴀɴ çıᴋᴀʀ

⚡️ __ᴄʀᴇᴀᴛᴏʀ {BOT_NAME} @jackdanielssx""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 ɢᴇʀɪ", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 ɪşᴛᴇ ꜱᴜᴅᴏ ᴋᴏᴍᴜᴛʟᴀʀı:
ʙᴜɴʟᴀʀɪ ꜱᴇɴ ʏᴀᴘᴀᴍᴀᴢꜱɪɴ ʙᴏşᴀ ɢᴇʟᴅɪɴ ɢᴇʀɪ ɢɪᴛ

⚡ __ᴄʀᴇᴀᴛᴏʀ {BOT_NAME} @jackdanielssx""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 ɢᴇʀɪ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
