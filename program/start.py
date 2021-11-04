from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **ᴍᴇʀʜᴀʙᴀʟᴀʀ {message.from_user.mention()} !**\n
💭 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **ʙᴏᴛᴜ ᴠᴇ ᴀꜱɪꜱᴛᴀɴı ɢʀᴜʙᴀ ᴇᴋʟᴇʏɪᴘ ɢüᴢᴇʟ ꜰʟɪᴍ ɪᴢʟᴇʏᴇʙɪʟɪʀ şᴀʀᴋıʟᴀʀ ᴅɪɴʟᴇʏᴇʙɪʟɪʀꜱɪɴɪᴢ**

ᴅᴀʜᴀ ꜰᴀᴢʟᴀ ʙɪʟɢɪ ɪçɪɴ ᴀşᴀɢıᴅᴀᴋɪ ʙᴜᴛᴏɴʟᴀʀı ᴋᴜʟʟᴀɴıɴ👇
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ʙᴇɴɪ ɢʀᴜʙᴜɴᴀ ᴇᴋʟᴇ ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ ʙᴀꜱɪᴛ ʙɪʟɢɪ", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 ᴋᴏᴍᴜᴛʟᴀʀ", callback_data="cbcmds"),
                    InlineKeyboardButton("❤️ ꜱᴀʜɪᴘ", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 ᴏꜰꜰɪᴄɪᴀʟ ɢʀᴏᴜᴘ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 ᴏғғɪᴄɪᴀʟ ᴋᴀɴᴀʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐 Öᴢᴇʟ ʙᴏᴛ ʏᴀᴘıᴍı", url="https://t.me/jackdanielssx"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨ ɢʀᴏᴜᴘ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "📣 ᴋᴀɴᴀʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**ᴍᴇʀʜᴀʙᴀ {message.from_user.mention()}, ʙᴇɴ {BOT_NAME}**\n\n✨ ʙᴏᴛ ɴᴏʀᴍᴀʟ çᴀʟışıʏᴏʀ\n🍀 ᴄʀᴇᴀᴛᴏʀ: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ ʙᴏᴛ ꜱüʀüᴍü: `v{__version__}`\n🍀 ᴘʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪʏᴏɴᴜ: `{pyrover}`\n✨ ᴘʏᴛʜᴏɴ ꜱüʀüᴍü: `{__python_version__}`\n🍀 ᴘʏᴛɢᴄᴀʟʟꜱ ꜱüʀüᴍü: `{pytover.__version__}`\n✨ Çᴀʟışᴍᴀ ꜱüʀᴇꜱɪ: `{uptime}`\n\n**ʙᴇɴɪ ʙᴜʀᴀʏᴀ ᴇᴋʟᴇᴅɪɢɪɴɪᴢ, ɢʀᴜᴘ ɢöʀüɴᴛüʟü ꜱᴏʜʙᴇᴛɪɴɪᴢᴅᴇ ᴠɪᴅᴇᴏ ᴠᴇ ᴍüᴢɪᴋ çᴀʟᴅıɢıɴıᴢ ɪçɪɴ ᴛᴇşᴇᴋᴋüʀʟᴇʀ** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢ...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `ᴘɪɴɢ!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 ʙᴏᴛ ᴅᴜʀᴜᴍᴜ:\n"
        f"• **çᴀʟışᴍᴀ ꜱüʀᴇꜱɪ:** `{uptime}`\n"
        f"• **ʙᴀşʟᴀɴɢıç ​​ꜱᴀᴀᴛɪ:** `{START_TIME_ISO}`"
    )
@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        """ʙᴏᴛᴜɴ ꜱᴀʜɪʙɪ => @jackdanielssx

🔥 /oynat => ɪꜱᴛᴇᴅɪɢɪɴ şᴀʀᴋıʏı ᴅɪʀᴇᴋ ᴅɪɴʟᴇᴛɪʀ
🔥 /izlet => ɪꜱᴛᴇᴅɪɢɪɴ ꜰɪʟᴍɪ ɪɴᴅɪʀɪᴘ ɪᴢʟᴇᴛɪʀ
🔥 /ara => ᴠɪᴅᴇᴏ ɪɴᴅɪʀɪʀ
🔥 /indir => ᴍᴜꜱɪᴄ ɪɴᴅɪʀɪʀ
🔥 /Utag => üʏᴇʟᴇʀɪ ᴇᴛɪᴋᴇᴛʟᴇʀ
🔥 /Atag => ᴀᴅᴍɪɴʟᴇʀɪ ᴇᴛɪᴋᴇᴛʟᴇʀ
🔥 /cancel => ᴇᴛɪᴋᴇᴛɪ ʙɪᴛɪʀ

ɴᴏᴛ : /izlet ve /oynat ᴋᴏᴍᴜᴛᴜ ᴋᴇɴᴅɪɴɪᴢᴇ ᴀɪᴛ ᴍᴜꜱɪᴄ ᴠᴇ ᴠɪᴅᴇᴏʟᴀʀı ᴅᴀ ᴏʏɴᴀᴛıʀ

🔥 /durdur - ꜱᴇꜱᴛᴇ ʙᴏᴛᴜ ᴅᴜʀᴅᴜʀᴜʀ
🔥 /devam - ᴅᴜʀᴅᴜʀᴜʟᴀɴ ʙᴏᴛᴜ ʙᴀşʟᴀᴛıʀ
🔥 /atla - şᴀʀᴋı ᴠᴇ ᴠɪᴅᴇᴏ ᴀᴛʟᴀʀ
🔥 /son - ꜱᴇꜱᴛᴇɴ ᴅüşᴇʀ ʜᴇʀşᴇʏɪ ᴅᴜʀᴅᴜʀᴜʀ
🔥 /reload - ʙᴏᴛᴜ ʏᴇɴɪᴅᴇɴ ʙᴀşʟᴀᴛıᴘ ᴀᴅᴍɪɴ ʟɪꜱᴛᴇꜱɪ ʏᴇɴɪʟᴇʀ
🔥 /gel - ᴀꜱɪꜱᴛᴀɴ ɢʀᴜʙᴀ ᴋᴀᴛıʟıʀ
🔥 /git - ᴀꜱɪꜱᴛᴀɴ ɢʀᴜᴘᴛᴀɴ çıᴋᴀʀ """
        )


@Client.on_message(filters.command("bot") & ~filters.private & ~filters.channel)
async def bot(_, message: Message):
    await message.reply_text(
""" ꜱᴇʟᴀᴍıɴ ᴀʟᴇʏᴋüᴍ ʙᴇɴ ɢᴇʟᴅɪᴍ ʟᴀɴ , ʜᴀʏıʀᴅıʀ ꜱᴏʀᴜɴ ᴍᴜ ᴠᴀʀ """
   )
@Client.on_message(filters.command("h") & ~filters.private & ~filters.channel)
async def h(_, message: Message):
    await message.reply_text(
""" ʜᴏᴅʀɪ ᴍᴇʏᴅᴀɴ ᴀꜱʟᴀɴ ᴘᴀʀçᴀꜱı 😉 """ )

