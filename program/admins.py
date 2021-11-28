from cache.admins import admins
from pyrogram import Client, filters
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL
from driver.decorators import authorized_users_only
from driver.filters import command, other_filters
from driver.queues import QUEUE, clear_queue
from driver.utils import skip_current_song, skip_item
from driver.veez import call_py
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


bttn = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 Gᴇʀɪ", callback_data="cbmenu")]]
)


bcl = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🗑 Kᴀᴘᴀᴛ", callback_data="cls")]]
)

@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        "✅ ʙᴏᴛ **ʏᴇɴɪᴅᴇɴ ʙᴀşʟᴀᴛıʟᴅı !**\n✅ **ᴀᴅᴍɪɴ ʟɪꜱᴛᴇꜱɪ**  **ɢüɴᴄᴇʟʟᴇɴᴅɪ !**"
    )


@Client.on_message(command(["atla", f"atla@{BOT_USERNAME}", "vatla"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="• Mᴇɴᴜ", callback_data="cbmenu"),
                InlineKeyboardButton(text="• Kᴀᴘᴀᴛ", callback_data="cls"),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("❌ şᴜ ᴀɴᴅᴀ ʜɪç ʙɪʀ şᴇʏ ᴏʏɴᴀᴛıʟᴍıʏᴏʀ")
        elif op == 1:
            await m.reply("✅ ʟɪꜱᴛᴇ ʙᴏş.\n\n• ʙᴏᴛ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛᴛᴇɴ ᴀʏʀıʟıʏᴏʀ")
        else:
            await m.reply_photo(
                photo=f"{IMG_3}",
                caption=f"⏭ **ʙɪʀ ꜱᴏɴʀᴀᴋɪ ᴘᴀʀçᴀʏᴀ ᴀᴛʟᴀɴᴅı.**\n\n🔘 **ɪꜱɪᴍ:** [{op[0]}]({op[1]})\n💬 **ꜱᴏʜʙᴇᴛ:** `{chat_id}`\n👁‍🗨 **ᴅᴜʀᴜᴍ:** `Çᴀʟıʏᴏʀ`\n👉 **ᴛᴀʟᴇᴘ ᴇᴅᴇɴ:** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **ꜱıʀᴀᴅᴀɴ şᴀʀᴋı ᴋᴀʟᴅıʀıʟᴅı:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message( 
    command(["son", f"son@{BOT_USERNAME}", "end", f"end@{BOT_USERNAME}", "vson"]) & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("✅ **ᴀᴋış ꜱᴏɴᴀ ᴇʀᴅɪ.**")
        except Exception as e:
            await m.reply(f"🚫 **ʜᴀᴛᴀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ᴀᴋışᴛᴀ ʜɪç ʙɪʀ şᴇʏ ʏᴏᴋ**")


@Client.on_message(
    command(["durdur", f"durdur@{BOT_USERNAME}", "vdurdur"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "⏸ **ᴘᴀʀçᴀ ᴅᴜʀᴀᴋʟᴀᴛıʟᴅı.**"
            )
        except Exception as e:
            await m.reply(f"🚫 **ʜᴀᴛᴀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ᴀᴋışᴛᴀ ʜɪç ʙɪʀ şᴇʏ ʏᴏᴋ**")
        

@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("ʙɪʀ ᴀɴᴏɴɪᴍ ʏöɴᴇᴛɪᴄɪꜱɪɴɪᴢ !\n\n» ʏöɴᴇᴛɪᴄɪ ʜᴀᴋʟᴀʀıɴᴅᴀɴ ᴋᴜʟʟᴀɴıᴄı ʜᴇꜱᴀʙıɴᴀ ɢᴇʀɪ ᴅöɴüɴ.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("❗️ ʏᴀʟɴıᴢᴄᴀ ʙᴜ ᴅüɢᴍᴇʏᴇ ᴅᴏᴋᴜɴᴀʙɪʟᴇɴ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛʟᴇʀɪ ʏöɴᴇᴛᴍᴇ ɪᴢɴɪɴᴇ ꜱᴀʜɪᴘ ʏöɴᴇᴛɪᴄɪ ❗️", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.edit_message_text(
                "🔇 ᴜꜱᴇʀʙᴏᴛ ʙᴀşᴀʀıʏʟᴀ ᴋᴀᴘᴀᴛıʟᴅı", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **ʜᴀᴛᴀ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.edit_message_text("❌ **ᴀᴋışᴛᴀ ʜɪçʙɪʀ şᴇʏ**", reply_markup=bcl)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("ʙɪʀ ᴀɴᴏɴɪᴍ ʏöɴᴇᴛɪᴄɪꜱɪɴɪᴢ !\n\n» ʏöɴᴇᴛɪᴄɪ ʜᴀᴋʟᴀʀıɴᴅᴀɴ ᴋᴜʟʟᴀɴıᴄı ʜᴇꜱᴀʙıɴᴀ ɢᴇʀɪ ᴅöɴüɴ.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 ʏᴀʟɴıᴢᴄᴀ ʙᴜ ᴅüɢᴍᴇʏᴇ ᴅᴏᴋᴜɴᴀʙɪʟᴇɴ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛʟᴇʀɪ ʏöɴᴇᴛᴍᴇ ɪᴢɴɪɴᴇ ꜱᴀʜɪᴘ ʏöɴᴇᴛɪᴄɪ !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.edit_message_text(
                "🔊 ᴜꜱᴇʀʙᴏᴛ ʙᴀşᴀʀıʏʟᴀ ᴀçıʟᴅı", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **ʜᴀᴛᴀ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.edit_message_text("❌ **ᴀᴋışᴛᴀ ʜɪçʙɪʀ şᴇʏ**", reply_markup=bcl)


@Client.on_message(
    command(["devam", f"devam@{BOT_USERNAME}", "vdevam"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "▶️ **ᴘᴀʀçᴀ ᴅᴇᴠᴀᴍ ᴇᴛᴛɪʀɪʟᴅɪ.**"
            )
        except Exception as e:
            await m.reply(f"🚫 **ʜᴀᴛᴀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ᴀᴋışᴛᴀ ʜɪç ʙɪʀ şᴇʏ ʏᴏᴋ**")


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    try:
        await call_py.change_volume_call(chat_id, volume=int(range))
        await m.reply(f"✅ **ꜱᴇꜱ ꜱᴇᴠɪʏᴇꜱɪ** `{range}`%")
    except Exception as e:
        await m.reply(f"🚫 **ʜᴀᴛᴀ:**\n\n{e}")
