from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"<i>Send any Youtube link...</i>"
    await message.reply_text(helptxt)   
