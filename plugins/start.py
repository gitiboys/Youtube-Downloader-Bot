from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("❤️ SHARE IT ❤️", url="https://t.me/share/url?url=Check%20this%20🤩%20amazing%20bot%20✅:%20https://t.me/MohithaVarma999_Bot")]
    ])
    welcomed = f"Hey {message.from_user.first_name}\n\nThis is Youtube Downloader 📽\n\nHit 👉 /help"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
