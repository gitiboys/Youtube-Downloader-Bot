from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"<iSend any Youtube link...</i>"
    await message.reply_text(helptxt)
