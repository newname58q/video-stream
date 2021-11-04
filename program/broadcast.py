from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from Efsanestar.config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def bye(client, message):
    sent=0
    failed=0
    if message.from_user.id in SUDO_USERS:
        lol = await message.reply("Gcast Başlatılıyor")
        if not message.reply_to_message:
            await lol.edit("Gcast efendim herhangi bir kısa mesajı yanıtlayın")
            return
        msg = message.reply_to_message.text
        async for dialog in client.iter_dialogs():
            try:
                await client.send_message(dialog.chat.id, msg)
                sent = sent+1
                await lol.edit(f"Gcasting.. Gönderilen: {sent} sohbet. Başarısız: {failed} sohbet.")
            except:
                failed=failed+1
                await lol.edit(f"Gcasting.. Gönderilen: {sent} sohbet. Başarısız: {failed} sohbet.")
            await asyncio.sleep(3)
        await message.reply_text(f"Gcasted iletisi {sent} Sohbet. Başarısız {failed} Sohbet.")
