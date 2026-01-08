from pyrogram import Client, filters
import os

# ===== ENV VARIABLES =====
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ===== BOT INIT =====
app = Client(
    "buzzfinderbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ===== START COMMAND =====
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply(
        "🔥 *Welcome to BuzzFinderBot*\n\n"
        "Yahan tumhe *Facebook, Instagram, TikTok, Pinterest* ke\n"
        "*latest VIRAL content ideas* milenge 🚀\n\n"
        "Commands:\n"
        "👉 /trending – Aaj ke viral ideas\n"
        "👉 /help – Help & info",
        parse_mode="markdown"
    )

# ===== TRENDING COMMAND =====
@app.on_message(filters.command("trending"))
def trending(client, message):
    message.reply(
        "🔥 *TODAY'S TRENDING CONTENT IDEAS*\n\n"
        "😂 *Comedy*\n"
        "• POV funny situations\n"
        "• Relatable daily life clips\n\n"
        "🤖 *AI*\n"
        "• AI voice reels\n"
        "• Face swap / talking photo\n\n"
        "💼 *Business*\n"
        "• Side income ideas\n"
        "• Money facts shorts\n\n"
        "❤️ *Love / Emotion*\n"
        "• Relatable relationship reels\n"
        "• Emotional quotes with video\n\n"
        "🎮 *Gaming*\n"
        "• Short gameplay moments\n"
        "• Funny fails clips\n\n"
        "⚡ Tip: Short (7–15 sec) videos zyada viral hote hain",
        parse_mode="markdown"
    )

# ===== HELP COMMAND =====
@app.on_message(filters.command("help"))
def help_cmd(client, message):
    message.reply(
        "ℹ️ *BuzzFinderBot Help*\n\n"
        "Ye bot creators ke liye banaya gaya hai.\n"
        "Tumhe yahan *viral topic ideas* milenge jisse tum\n"
        "apna video bana sako 📹\n\n"
        "Commands:\n"
        "/start – Bot start karo\n"
        "/trending – Viral ideas dekho\n\n"
        "🚀 More features coming soon!",
        parse_mode="markdown"
    )

# ===== RUN BOT =====
app.run()
