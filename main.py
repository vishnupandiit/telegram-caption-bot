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

@app.on_message(filters.video | filters.document)
async def replace_username(client, message):
    caption = message.caption or ""
    new_caption = re.sub(r"@\w+", REPLACE_USERNAME, caption)

    if message.video:
        await message.reply_video(message.video.file_id, caption=new_caption)
    else:
        await message.reply_document(message.document.file_id, caption=new_caption)

app.run()
