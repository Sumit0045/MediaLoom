from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from MediaLoom import app, BOT_NAME


buttons = InlineKeyboardMarkup([
                [
                  InlineKeyboardButton("How to use me?", url="https://t.me/MediaLoom")
                ],[
                  InlineKeyboardButton("Repository", url="https://github.com/Sumit0045/MediaLoom")
                ]])

@app.on_message(filters.command("start"))
async def start_(_, message):
    await message.reply_photo(photo="https://graph.org/file/f47e8e58428604cfb989f-61cbdaf8f0b8399ef4.jpg",
        caption=f"Hello, I'm {BOT_NAME}! I can host any type of media, including large files, with unlimited storage. "
        "Feel free to upload your files, and I'll take care of the rest!",
        reply_markup=buttons
    )
