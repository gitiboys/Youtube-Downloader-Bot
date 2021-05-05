from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/TeluguBots")]
    ])
    welcomed = f"Hey {message.from_user.first_name}\n\nThis is Youtube Downloader 📽\n\nHit 👉 /help"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
