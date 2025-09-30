
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8487849656:AAGAPSdlqD9sBfpRB4PFi4WAxEr3bD4w5f0"


async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.photo:
        # The last one is highest resolution
        file_id = update.message.photo[-1].file_id
        await update.message.reply_text(f"File ID: {file_id}")
        print("File ID:", file_id)

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

print("Send a photo to the bot in private chat to get its file_id...")
app.run_polling()


