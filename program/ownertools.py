import os
import shutil
import sys
import heroku3
import traceback
from functools import wraps
from os import environ, execle

import psutil
from pyrogram import Client, filters
from pyrogram.types import Message

from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_ID,
    U_BRANCH,
    UPSTREAM_REPO,
)
from zaidmusic.song import get_text, humanbytes
from helpers.filters import command
from helpers.database import db
from helpers.dbtools import main_broadcast_handler
from helpers.decorators import sudo_users_only


# Stats Of Your Bot
@Client.on_message(command("stats"))
@sudo_users_only
async def botstats(_, message: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    total_users = await db.total_users_count()
    await message.reply_text(
        text=f"**📊 ɪꜱᴛᴀᴛɪꜱᴛɪᴋʟᴇʀɪ @{BOT_USERNAME}** \n\n**🤖 ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ:** `v6.5` \n\n**🙎🏼 ᴛᴏᴘʟᴀᴍ ᴋᴜʟʟᴀɴɪᴄɪ:** \n » **ʙᴏᴛ ᴘᴍ'ᴅᴇ:** `{total_users}` \n\n**💾 ᴅɪꜱᴋ ᴋᴜʟʟᴀɴɪᴍɪ:** \n » **ᴅɪꜱᴋ ᴀʟᴀɴɪ:** `{total}` \n » **ᴋᴜʟʟᴀɴɪʟᴍɪꜱ:** `{used}({disk_usage}%)` \n » **ʙᴇᴅᴀᴠᴀ:** `{free}` \n\n**🎛 ᴅᴏɴᴀɴɪᴍ ᴋᴜʟʟᴀɴɪᴍɪ:** \n » **ᴄᴘᴜ ᴋᴜʟʟᴀɴɪᴍɪ:** `{cpu_usage}%` \n » **ʀᴀᴍ ᴋᴜʟʟᴀɴɪᴍɪ:** `{ram_usage}%`",
        parse_mode="Markdown",
        quote=True,
    )


@Client.on_message(
    filters.private
    & filters.command("broadcast")
    & filters.user(OWNER_ID)
    & filters.reply
)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)


@Client.on_message(filters.private & filters.command("block"))
@sudo_users_only
async def ban(c: Client, m: Message):
    if len(m.command) == 1:
        await m.reply_text(
            "» ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ʙᴏᴛᴜɴᴜᴢᴜ ᴋᴜʟʟᴀɴᴍᴀꜱɪɴɪ ʏᴀꜱᴀᴋʟᴀᴍᴀᴋ ɪᴄɪɴ ʙᴜ ᴋᴏᴍᴜᴛ, ᴏᴋᴜʏᴜɴ /help ᴅᴀʜᴀ ꜰᴀᴢʟᴀ ʙɪʟɢɪ ɪᴄɪɴ !",
            quote=True,
        )
        return
    try:
        user_id = int(m.command[1])
        ban_duration = m.command[2]
        ban_reason = " ".join(m.command[3:])
        ban_log_text = f"🔁 ᴋᴜʟʟᴀɴɪᴄɪʏɪ ʏᴀꜱᴀᴋʟᴀᴍᴀᴋ... \n\nᴋᴜʟʟᴀɴɪᴄɪ ᴋɪᴍʟɪɢɪ: `{user_id}` \ꜱᴜʀᴇ: `{ban_duration}` \nɴᴇᴅᴇɴ: `{ban_reason}`"
        try:
            await c.send_message(
                user_id,
                f"ᴜᴢɢᴜɴᴜᴍ, ʏᴀꜱᴀᴋʟᴀɴᴅɪɴ!** \n\nɴᴇᴅᴇɴ: `{ban_reason}` \nꜱᴜʀᴇ: `{ban_duration}` ɢᴜɴ(s). \n\n**💬 ꜱᴀʜɪʙɪɴᴇ ᴍᴇꜱᴀᴊ ɢᴏɴᴅᴇʀ @{GROUP_SUPPORT} ᴇɢᴇʀ ʙᴜɴᴜɴ ʙɪʀ ʜᴀᴛᴀ ᴏʟᴅᴜɢᴜɴᴜ ᴅᴜꜱᴜɴᴜʏᴏʀꜱᴀɴ.",
            )
            ban_log_text += "\n\n✅ ʙᴜ ʙɪʟᴅɪʀɪᴍ ᴏ ᴋᴜʟʟᴀɴɪᴄɪʏᴀ ɢᴏɴᴅᴇʀɪʟᴅɪ"
        except:
            traceback.print_exc()
            ban_log_text += f"\n\n❌ **ʙᴜ ʙɪʟᴅɪʀɪᴍ ᴏ ᴋᴜʟʟᴀɴɪᴄɪʏᴀ ɢᴏɴᴅᴇʀɪʟᴇᴍᴇᴅɪ** \n\n`{traceback.format_exc()}`"
        await db.ban_user(user_id, ban_duration, ban_reason)
        print(ban_log_text)
        await m.reply_text(ban_log_text, quote=True)
    except:
        traceback.print_exc()
        await m.reply_text(
            f"❌ ʙɪʀ ʜᴀᴛᴀ ᴏʟᴜꜱᴛᴜ, ɢᴇʀɪ ɪᴢʟᴇᴍᴇ ᴀꜱᴀɢɪᴅᴀ ᴠᴇʀɪʟᴍɪꜱᴛɪʀ:\n\n`{traceback.format_exc()}`",
            quote=True,
        )


# Unblock User
@Client.on_message(
    filters.private & filters.command("unblock") & filters.user(OWNER_ID)
)
async def unban(c: Client, m: Message):
    if len(m.command) == 1:
        await m.reply_text(
            "» ᴋᴜʟʟᴀɴɪᴄɪ ʏᴀꜱᴀɢɪɴɪ ᴋᴀʟᴅɪʀᴍᴀᴋ ɪᴄɪɴ ʙᴜ ᴋᴏᴍᴜᴛ, ᴅᴀʜᴀ ꜰᴀᴢʟᴀ ʙɪʟɢɪ ɪᴄɪɴ /ʜᴇʟᴘ'ɪ ᴏᴋᴜʏᴜɴ !", quote=True
        )
        return
    try:
        user_id = int(m.command[1])
        unban_log_text = f"🔁 ᴋᴜʟʟᴀɴɪᴄɪ ʏᴀꜱᴀɢɪɴɪ ᴋᴀʟᴅɪʀᴍᴀᴋ... \n\n**ᴋᴜʟʟᴀɴɪᴄɪ ᴋɪᴍʟɪɢɪ:**{user_id}"
        try:
            await c.send_message(user_id, "🎊 ᴛᴇʙʀɪᴋʟᴇʀ ʏᴀꜱᴀɢɪɴ ᴋᴀʟᴅɪʀɪʟᴅɪ!")
            unban_log_text += "\n\n✅ ʙᴜ ʙɪʟᴅɪʀɪᴍ ᴏ ᴋᴜʟʟᴀɴɪᴄɪʏᴀ ɢᴏɴᴅᴇʀɪʟᴅɪ"
        except:
            traceback.print_exc()
            unban_log_text += f"\n\n❌ **ʙᴜ ʙɪʟᴅɪʀɪᴍ ᴏ ᴋᴜʟʟᴀɴɪᴄɪʏᴀ ɢᴏɴᴅᴇʀɪʟᴇᴍᴇᴅɪ** \n\n`{traceback.format_exc()}`"
        await db.remove_ban(user_id)
        print(unban_log_text)
        await m.reply_text(unban_log_text, quote=True)
    except:
        traceback.print_exc()
        await m.reply_text(
            f"❌ ʙɪʀ ʜᴀᴛᴀ ᴏʟᴜꜱᴛᴜ, ɢᴇʀɪ ɪᴢʟᴇᴍᴇ ᴀꜱᴀɢɪᴅᴀ ᴠᴇʀɪʟᴍɪꜱᴛɪʀ:\n\n`{traceback.format_exc()}`",
            quote=True,
        )


# Blocked User List
@Client.on_message(
    filters.private & filters.command("blocklist") & filters.user(OWNER_ID)
)
async def _banned_usrs(_, m: Message):
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ""
    async for banned_user in all_banned_users:
        user_id = banned_user["id"]
        ban_duration = banned_user["ban_status"]["ban_duration"]
        banned_on = banned_user["ban_status"]["banned_on"]
        ban_reason = banned_user["ban_status"]["ban_reason"]
        banned_usr_count += 1
        text += f"⫸ **ᴋᴜʟʟᴀɴɪᴄɪ ᴋɪᴍʟɪɢɪ**: `{user_id}`,⫸ **ʏᴀꜱᴀᴋ ꜱᴜʀᴇꜱɪ**: `{ban_duration}`,⫸ **ʏᴀꜱᴀᴋʟɪ ᴛᴀʀɪʜ**: `{banned_on}`,⫸ **ʙᴀɴ ꜱᴇʙᴇʙɪ**: `{ban_reason}`\n\n"
    reply_text = f"⫸ **ᴛᴏᴘʟᴀᴍ ʏᴀꜱᴀᴋ:** `{banned_usr_count}`\n\n{text}"
    if len(reply_text) > 4096:
        with open("banned-user-list.txt", "w") as f:
            f.write(reply_text)
        await m.reply_document("banned-user-list.txt", True)
        os.remove("banned-user-list.txt")
        return
    await m.reply_text(reply_text, True)


# ====== UPDATER ======

REPO_ = UPSTREAM_REPO
BRANCH_ = U_BRANCH


@Client.on_message(command("update") & filters.user(OWNER_ID))
async def updatebot(_, message: Message):
    msg = await message.reply_text("**ʙᴏᴛ ɢᴜɴᴄᴇʟʟᴇɴɪʏᴏʀ, ʟᴜᴛꜰᴇɴ ʙɪʀ ꜱᴜʀᴇ ʙᴇᴋʟᴇʏɪɴ...**")
    try:
        repo = Repo()
    except GitCommandError:
        return await msg.edit("**ɢᴇᴄᴇʀꜱɪᴢ ɢɪᴛ ᴋᴏᴍᴜᴛᴜ !**")
    except InvalidGitRepositoryError:
        repo = Repo.init()
        if "upstream" in repo.remotes:
            origin = repo.remote("upstream")
        else:
            origin = repo.create_remote("upstream", REPO_)
        origin.fetch()
        repo.create_head(U_BRANCH, origin.refs.main)
        repo.heads.main.set_tracking_branch(origin.refs.main)
        repo.heads.main.checkout(True)
    if repo.active_branch.name != U_BRANCH:
        return await msg.edit(
            f"**ᴜᴢɢᴜɴᴜᴍ, ᴀᴅʟɪ ᴋᴏꜱᴛᴜᴍ ꜱᴜʙᴇꜱɪɴɪ ᴋᴜʟʟᴀɴɪʏᴏʀꜱᴜɴᴜᴢ:** `{repo.active_branch.name}`!\n\nᴅᴇɢɪꜱᴍᴇᴋ `{U_BRANCH}` ɢᴜɴᴄᴇʟʟᴇᴍᴇʏᴇ ᴅᴇᴠᴀᴍ ᴇᴛᴍᴇᴋ ɪᴄɪɴ ꜱᴜʙᴇ!"
        )
    try:
        repo.create_remote("upstream", REPO_)
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(U_BRANCH)
    if not HEROKU_URL:
        try:
            ups_rem.pull(U_BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        await run_cmd("pip3 install --no-cache-dir -r requirements.txt")
        await msg.edit("**update finished, restarting now...**")
        args = [sys.executable, "main.py"]
        execle(sys.executable, *args, environ)
        sys.exit()
        return
    else:
        await msg.edit("`ʜᴇʀᴏᴋᴜ ᴀʟɢɪʟᴀɴᴅɪ!`")
        await msg.edit(
            "`ɢᴜɴᴄᴇʟʟᴇᴍᴇ ᴠᴇ ʏᴇɴɪᴅᴇɴ ʙᴀꜱʟᴀᴛᴍᴀ ʙᴀꜱʟᴀᴅɪ, ʟᴜᴛꜰᴇɴ 5-10 ᴅᴀᴋɪᴋᴀ ʙᴇᴋʟᴇʏɪɴ!`"
        )
        ups_rem.fetch(U_BRANCH)
        repo.git.reset("--hard", "FETCH_HEAD")
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(HEROKU_URL)
        else:
            remote = repo.create_remote("heroku", HEROKU_URL)
        try:
            remote.push(refspec="HEAD:refs/heads/main", force=True)
        except BaseException as error:
            await msg.edit(f"🚫 **ɢᴜɴᴄᴇʟʟᴇʏɪᴄɪ ʜᴀᴛᴀꜱɪ** \n\nɢᴇʀɪ ɪᴢ : `{error}`")
            return repo.__del__()


# HEROKU LOGS


async def edit_or_send_as_file(
    text: str,
    message: Message,
    client: Client,
    caption: str = "`Result!`",
    file_name: str = "result",
    parse_mode="md",
):
    """ᴍᴇᴛɪɴ ᴜᴢᴜɴʟᴜɢᴜ ᴛɢ ꜱɪɴɪʀɪɴɪ ᴀꜱᴀʀꜱᴀ ᴅᴏꜱʏᴀ ᴏʟᴀʀᴀᴋ ɢᴏɴᴅᴇʀ ᴇʟꜱᴇ ᴍᴇꜱᴀᴊɪ ᴅᴜᴢᴇɴʟᴇ"""
    if not text:
        await message.edit("`ᴍᴇᴛɪɴᴅᴇɴ ʙᴀꜱᴋᴀ ʙɪʀ ꜱᴇʏ ᴠᴀʀ, ɪᴘᴛᴀʟ ᴇᴅɪʟɪʏᴏʀ...`")
        return
    if len(text) <= 1024:
        return await message.edit(text, parse_mode=parse_mode)

    await message.edit("`ᴄɪᴋᴛɪ ᴄᴏᴋ ʙᴜʏᴜᴋ, ᴅᴏꜱʏᴀ ᴏʟᴀʀᴀᴋ ɢᴏɴᴅᴇʀɪʟɪʏᴏʀ!`")
    file_names = f"{file_name}.text"
    open(file_names, "w").write(text)
    await client.send_document(message.chat.id, file_names, caption=caption)
    await message.delete()
    if os.path.exists(file_names):
        os.remove(file_names)
    return


heroku_client = heroku3.from_key(HEROKU_API_KEY) if HEROKU_API_KEY else None


def _check_heroku(func):
    @wraps(func)
    async def heroku_cli(client, message):
        heroku_app = None
        if not heroku_client:
            await message.reply_text("`ʙᴜ ᴏᴢᴇʟʟɪɢɪ ᴋᴜʟʟᴀɴᴍᴀᴋ ɪᴄɪɴ ʟᴜᴛꜰᴇɴ ʜᴇʀᴏᴋᴜ ᴀᴘɪ ᴀɴᴀʜᴛᴀʀɪɴɪ ᴇᴋʟᴇʏɪɴ!`")
        elif not HEROKU_APP_NAME:
            await edit_or_reply(
                message, "`ʙᴜ ᴏᴢᴇʟʟɪɢɪ ᴋᴜʟʟᴀɴᴍᴀᴋ ɪᴄɪɴ ʟᴜᴛꜰᴇɴ ʜᴇʀᴏᴋᴜ ᴀᴘᴘ ᴀᴅɪɴɪ ᴇᴋʟᴇʏɪɴ!`"
            )
        if HEROKU_APP_NAME and heroku_client:
            try:
                heroku_app = heroku_client.app(HEROKU_APP_NAME)
            except:
                await message.reply_text(
                    message,
                    "`ʜᴇʀᴏᴋᴜ ᴀᴘɪ ᴀɴᴀʜᴛᴀʀɪ ᴠᴇ ᴜʏɢᴜʟᴀᴍᴀ ᴀᴅɪ ᴇꜱʟᴇꜱᴍɪʏᴏʀ! ᴛᴇᴋʀᴀʀ ᴋᴏɴᴛʀᴏʟ ᴇᴛ`",
                )
            if heroku_app:
                await func(client, message, heroku_app)

    return heroku_cli


@Client.on_message(command("logs") & filters.user(OWNER_ID))
@_check_heroku
async def logswen(client: Client, message: Message, happ):
    msg = await message.reply_text("`ʟᴜᴛꜰᴇɴ ʙɪʀ ᴅᴀᴋɪᴋᴀ ʙᴇᴋʟᴇʏɪɴ!`")
    logs = happ.get_log()
    capt = f"Heroku logs of `{HEROKU_APP_NAME}`"
    await edit_or_send_as_file(logs, msg, client, capt, "logs")


# Restart Bot
@Client.on_message(command("restart") & filters.user(OWNER_ID))
@_check_heroku
async def restart(client: Client, message: Message, hap):
    await message.reply_text("`ꜱɪᴍᴅɪ ʏᴇɴɪᴅᴇɴ ʙᴀꜱʟᴀᴛɪʟɪʏᴏʀ, ʟᴜᴛꜰᴇɴ ʙᴇᴋʟᴇʏɪɴ...`")
    hap.restart()


# Set Heroku Var
@Client.on_message(command("setvar") & filters.user(OWNER_ID))
@_check_heroku
async def setvar(client: Client, message: Message, app_):
    msg = await message.reply_text(message, "`ʟᴜᴛꜰᴇɴ ʙᴇᴋʟᴇʏɪɴ...`")
    heroku_var = app_.config()
    _var = get_text(message)
    if not _var:
        await msg.edit("**ᴋᴜʟʟᴀɴɪᴍ:** `/setvar (var) (value)`")
        return
    if " " not in _var:
        await msg.edit("**ᴋᴜʟʟᴀɴɪᴍ:** `/setvar (var) (value)`")
        return
    var_ = _var.split(" ", 1)
    if len(var_) > 2:
        await msg.edit("**ᴋᴜʟʟᴀɴɪᴍ:** `/setvar (var) (value)`")
        return
    _varname, _varvalue = var_
    await msg.edit(f"**ᴅᴇɢɪꜱᴋᴇɴ:** `{_varname}` \n**new value:** `{_varvalue}`")
    heroku_var[_varname] = _varvalue


# Delete Heroku Var
@Client.on_message(command("delvar") & filters.user(OWNER_ID))
@_check_heroku
async def delvar(client: Client, message: Message, app_):
    msg = await message.reply_text(message, "`ʟᴜᴛꜰᴇɴ ʙᴇᴋʟᴇʏɪɴ...!`")
    heroku_var = app_.config()
    _var = get_text(message)
    if not _var:
        await msg.edit("`ꜱɪʟᴍᴇᴋ ɪᴄɪɴ ʙɪʀ ᴠᴀʀ ᴀᴅɪ ᴠᴇʀɪɴ!`")
        return
    if _var not in heroku_var:
        await msg.edit("`ʙᴜ ᴠᴀʀ ʏᴏᴋ!`")
        return
    await msg.edit(f"ʙᴀꜱᴀʀɪʏʟᴀ ꜱɪʟɪɴᴅɪ ᴠᴀʀ `{_var}`")
    del heroku_var[_var]
