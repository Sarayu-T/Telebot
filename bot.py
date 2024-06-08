import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    filters
)

load_dotenv()
token = os.getenv("TELEBOT_TOKEN")
if not token:
    raise ValueError("No token provided. Set the TELEBOT_TOKEN environment variable.")

application = Application.builder().token(token).build()
print("Successfully connected to Telegram API")

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I am a bot that is going to mimic you :)")

application.add_handler(CommandHandler('start', start))

async def mimic(update: Update, context: CallbackContext):
    incoming_text = update.message.text
    await update.message.reply_text(incoming_text + "💔")

application.add_handler(MessageHandler(filters=filters.TEXT, callback=mimic))
application.run_polling()
