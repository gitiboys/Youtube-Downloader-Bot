from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"<i>Send any Youtube link...</i>"
    await message.reply_text(helptxt)
    
    
@Client.on_message(Filters.command(["contact"]))
async def start(client, message):
    contxt = f"<code>Send your feedback through</code> @de5tr0yer_bot 👈"
    await message.reply_text(contxt)    
