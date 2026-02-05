from pyrogram import Client, filters
import re
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

REPLACE_USERNAME = "@skillwithcourse"

app = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

def replace(text):
    if not text:
        return text
    return re.sub(r"@\w+", REPLACE_USERNAME, text)

# TEXT
@app.on_message(filters.text & ~filters.command)
async def handle_text(client, message):
    await message.reply_text(replace(message.text))

# PHOTO
@app.on_message(filters.photo)
async def handle_photo(client, message):
    await message.reply_photo(
        message.photo.file_id,
        caption=replace(message.caption)
    )

# VIDEO
@app.on_message(filters.video)
async def handle_video(client, message):
    await message.reply_video(
        message.video.file_id,
        caption=replace(message.caption)
    )

# DOCUMENT
@app.on_message(filters.document)
async def handle_document(client, message):
    await message.reply_document(
        message.document.file_id,
        caption=replace(message.caption)
    )

app.run()
