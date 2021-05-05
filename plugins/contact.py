from pyrogram import Client, Filters


@Client.on_message(Filters.command(["contact"]))
async def start(client, message):
    contxt = f"<code>Send your feedback through</code> @de5tr0yer_bot 👈"
    await message.reply_text(contxt) 
