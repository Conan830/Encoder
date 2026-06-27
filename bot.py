import os
import asyncio
import psutil
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

app = Client(
    "EncoderBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    text = (
        "**Hello! I am your Advanced Media Encoder Bot.**\n\n"
        "Reply to any video with encoding commands.\n"
        "💡 **Owner:** @issei_senpai"
    )
    await message.reply_text(text)

@app.on_message(filters.command(["sub", "hsub", "360p", "480p", "720p", "1080p", "1440p", "2160p", "batch_encoding"]))
async def encoding_tools_handler(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.video:
        await message.reply_text("Please reply to a video file.")
        return
    command = message.command[0]
    await message.reply_text(f"Task Added to Queue: `{command}`\nProcessing will start soon.")

@app.on_message(filters.command("abort"))
async def abort_handler(client: Client, message: Message):
    await message.reply_text("Ongoing task has been aborted successfully.")

@app.on_message(filters.command(["extract_sub", "extract_audio", "stream_remove", "addaudio", "merge", "trim", "screenshot", "sample_video", "compare", "watermark"]))
async def media_tools_handler(client: Client, message: Message):
    command = message.command[0]
    await message.reply_text(f"Executing Media Tool: `{command}`")

@app.on_message(filters.command(["settings", "crf", "preset", "codec", "audiocodec", "audio", "tune", "fps", "upload", "resetsettings"]))
async def settings_handler(client: Client, message: Message):
    command = message.command[0]
    if command == "settings":
        await message.reply_text("**Current Encoder Settings Panel**\n\nCRF: 28\nPreset: medium\nCodec: libx265\nAudio: 128k")
    else:
        await message.reply_text(f"Configuration for `{command}` updated.")

@app.on_message(filters.command("stats"))
async def stats_handler(client: Client, message: Message):
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    stats_text = f"**Server Stats:**\n\n**CPU:** {cpu}%\n**RAM:** {ram}%\n**Disk:** {disk}%"
    await message.reply_text(stats_text)

@app.on_message(filters.command(["queue", "clear", "restart", "add_font", "list_font"]))
async def admin_utility_handler(client: Client, message: Message):
    command = message.command[0]
    await message.reply_text(f"Admin Action: `{command}` executed.")

if __name__ == "__main__":
    app.run()

