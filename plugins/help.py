from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Supports Youtube Single Video (No playlist).</br><i>Just Send Youtube Url...</i>"
    await message.reply_text(helptxt)
