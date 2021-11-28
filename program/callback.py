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
        f"""✨ **Hᴏşɢᴇʟᴅɪɴ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ʏᴇɴɪ ᴛᴇʟᴇɢʀᴀᴍ'ıɴ ɢöʀüɴᴛüʟü ꜱᴏʜʙᴇᴛʟᴇʀɪ ᴀʀᴀᴄıʟığıʏʟᴀ ɢʀᴜᴘʟᴀʀᴅᴀ ᴍüᴢɪᴋ ᴠᴇ ᴠɪᴅᴇᴏ ᴏʏɴᴀᴛᴍᴀɴıᴢᴀ ᴏʟᴀɴᴀᴋ ᴛᴀɴıʀ!**

💡 **📚 Kᴏᴍᴜᴛʟᴀʀ ᴅüɢᴍᴇꜱɪɴɪ ᴛıᴋʟᴀʏᴀʀᴀᴋ ʙᴏᴛ'ᴜɴ ᴛüᴍ ᴋᴏᴍᴜᴛʟᴀʀıɴı ᴠᴇ ɴᴀꜱıʟ çᴀʟışᴛıᴋʟᴀʀıɴı öɢʀᴇɴɪɴ!**

🔖 **Bᴜ ʙᴏᴛᴜɴ ɴᴀꜱıʟ ᴋᴜʟʟᴀɴıʟᴀᴄᴀɢıɴı öɢʀᴇɴᴍᴇᴋ ɪçɪɴ ʟüᴛꜰᴇɴ ᴛıᴋʟᴀʏıɴ » ❓ ʙᴀꜱɪᴛ ᴋᴏᴍᴜᴛʟᴀʀ!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Bᴇɴɪ Gʀᴜʙᴜɴᴀ Eᴋʟᴇ ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Bᴀꜱɪᴛ Kᴏᴍᴜᴛʟᴀʀ", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Kᴏᴍᴜᴛʟᴀʀ", callback_data="cbcmds"),
                    InlineKeyboardButton(" Sᴀʜɪʙɪ ", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Rᴇꜱᴍɪ Gʀᴜᴘ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Rᴇꜱᴍɪ Kᴀɴᴀʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
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

⚡ __ᴄʀᴇᴀᴛᴏʀ by {BOT_NAME} @jackdanielssx""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 ɢᴇʀɪ", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Mᴇʀʜᴀʙᴀ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**


⚡ __ᴄʀᴇᴀᴛᴏʀ by {BOT_NAME} @jackdanielssx""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Aᴅᴍɪɴ ᴋᴏᴍᴜᴛ", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Cʀᴇᴀᴛᴏʀ ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Bᴀꜱɪᴄ ᴋᴏᴍᴜᴛ", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Gᴇʀɪ", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 ʙᴀꜱɪᴛ ᴋᴏᴍᴜᴛʟᴀʀ:

» /oynat => ɪꜱᴛᴇᴅɪɢɪɴ şᴀʀᴋıʏı ᴅɪʀᴇᴋ ᴅɪɴʟᴇᴛɪʀ
» /izle => ɪꜱᴛᴇᴅɪɢɪɴ ꜰɪʟᴍɪ ɪɴᴅɪʀɪᴘ ɪᴢʟᴇᴛɪʀ ᴠᴇ ʏᴏᴜᴛᴜʙᴇᴅᴇɴ ᴄᴀɴʟı ᴀᴋışı ᴏʟᴀɴ ʀᴀᴅʏᴏ ʟɪɴᴋɪɴɪ ᴘᴀʏʟᴀşıɴ
» /ara => ᴠɪᴅᴇᴏ ɪɴᴅɪʀɪʀ
» /bul => ᴍᴜꜱɪᴄ ɪɴᴅɪʀɪʀ
ɴᴏᴛ : /izle ve /oynat ᴋᴏᴍᴜᴛᴜ ᴋᴇɴᴅɪɴɪᴢᴇ ᴀɪᴛ ᴍᴜꜱɪᴄ ᴠᴇ ᴠɪᴅᴇᴏʟᴀʀı ᴅᴀ ᴏʏɴᴀᴛıʀ
⚡️ __ᴄʀᴇᴀᴛᴏʀ {BOT_NAME} @jackdanielssx""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Gᴇʀɪ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 ᴀᴅᴍɪɴ ᴋᴏᴍᴜᴛʟᴀʀı:

» /Durdur - ꜱᴇꜱᴛᴇ ʙᴏᴛᴜ ᴅᴜʀᴅᴜʀᴜʀ
» /Devam - ᴅᴜʀᴅᴜʀᴜʟᴀɴ ʙᴏᴛᴜ ʙᴀşʟᴀᴛıʀ
» /Atla - şᴀʀᴋı ᴠᴇ ᴠɪᴅᴇᴏ ᴀᴛʟᴀʀ
» /Son - ꜱᴇꜱᴛᴇɴ ᴅüşᴇʀ ʜᴇʀşᴇʏɪ ᴅᴜʀᴅᴜʀᴜʀ
» /Reload - ʙᴏᴛᴜ ʏᴇɴɪᴅᴇɴ ʙᴀşʟᴀᴛıᴘ ᴀᴅᴍɪɴ ʟɪꜱᴛᴇꜱɪ ʏᴇɴɪʟᴇʀ
» /Gel - ɢʀᴜʙᴀ ᴋᴀᴛıʟıʀ
» /Git - ɢʀᴜᴘᴛᴀɴ çıᴋᴀʀ

⚡️ __ᴄʀᴇᴀᴛᴏʀ {BOT_NAME} @jackdanielssx""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Gᴇʀɪ", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 ɪşᴛᴇ ꜱᴜᴅᴏ ᴋᴏᴍᴜᴛʟᴀʀı:
» /Rmw - ᴛüᴍ ʜᴀᴍ ᴅᴏꜱʏᴀʟᴀʀı ᴛᴇᴍɪᴢʟᴇ
» /Rmd - ɪɴᴅɪʀɪʟᴇɴ ᴛüᴍ ᴅᴏꜱʏᴀʟᴀʀı ᴛᴇᴍɪᴢʟᴇ
» /Leaveall - ᴜꜱᴇʀʙᴏᴛ'ᴜɴ ᴛüᴍ ɢʀᴜᴘᴛᴀɴ ᴀʏʀıʟᴍᴀꜱıɴı ᴇᴍʀᴇᴛ

⚡ __ᴄʀᴇᴀᴛᴏʀ {BOT_NAME} @jackdanielssx""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Gᴇʀɪ", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("ꜱᴇɴ ʙɪʀ ᴀɴᴏɴɪᴍ ʏöɴᴇᴛɪᴄɪꜱɪɴ !\n\n» ʏöɴᴇᴛɪᴄɪ ʜᴀᴋʟᴀʀıɴᴅᴀɴ ᴋᴜʟʟᴀɴıᴄı ʜᴇꜱᴀʙıɴᴀ ɢᴇʀɪ ᴅöɴ.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 ʏᴀʟɴıᴢᴄᴀ ʙᴜ ᴅüɢᴍᴇʏᴇ ᴅᴏᴋᴜɴᴀʙɪʟᴇɴ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛʟᴇʀɪ ʏöɴᴇᴛᴍᴇ ɪᴢɴɪɴᴇ ꜱᴀʜɪᴘ ʏöɴᴇᴛɪᴄɪ !", show_alert=True)
    await query.edit_message_text(
        f"⚙️ **Aʏᴀʀʟᴀʀ** {query.message.chat.title}\n\n🔇 : ᴋᴜʟʟᴀɴıᴄı ʙᴏᴛᴜɴᴜ ꜱᴇꜱꜱɪᴢᴇ ᴀʟ\n🔊 : ᴋᴜʟʟᴀɴıᴄı ʙᴏᴛᴜɴᴜɴ ꜱᴇꜱɪɴɪ ᴀç",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("🔇", callback_data="cbunmute"),
                InlineKeyboardButton("🔊", callback_data="cbmute"),
            ],[
                InlineKeyboardButton("🗑 Kᴀᴘᴀᴛ", callback_data="cls")],
            ]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
