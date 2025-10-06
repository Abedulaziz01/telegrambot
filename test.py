# registration_bot.py
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import pytz

# Use environment variable for token (no hardcoding)
# filepath: [registration_bot.py](http://_vscodecontentref_/1)
TOKEN = "8487849656:AAGAPSdlqD9sBfpRB4PFi4WAxEr3bD4w5f0"

# Instruction steps with images
steps = [
    {
        "text": """👋 Step 1: Welcome to the bot! 
This step introduces you to the bot and explains its purpose. 
Here you will learn how to navigate through the instructions. 
Take your time to read this carefully before moving to the next step.
Now you are on Step 1.""",
        "image": "AgACAgQAAxkBAAMRaNvObBHnEEY_2Zb9z3vNYN3hUugAAr7IMRsTEeFSgcqV_FlsFpwBAAMCAAN5AAM2BA"
    },
    {
        "text": """📌 Step 2: Understanding the basics. 
In this step, you will learn about the main features and functions of the bot. 
We explain everything in detail so you can fully understand how to interact with the bot. 
Pay attention to each point as it will be important for the following steps.
Now you are on Step 2.""",
        "image": "AgACAgQAAxkBAAMSaNvObECCpAhQC-l6mpFTDHdujJgAAr_IMRsTEeFSKW02ooRhXUgBAAMCAAN5AAM2BA"
    },
    {
        "text": """📘 Step 3: Advanced instructions. 
This step covers more advanced concepts and practical tips. 
You will see examples, recommended actions, and important considerations to follow. 
Make sure to read carefully as this step is critical for successfully completing the guide.
Now you are on Step 3.""",
        "image": "AgACAgQAAxkBAAMTaNvObHAdLGwN7rBwFQW-IBeeBfoAAsDIMRsTEeFSJzWrRvZGr8cBAAMCAAN5AAM2BA"
    },
    {
        "text": """✅ Step 4: Final instructions and summary. 
Congratulations! You have reached the final step. 
Here we summarize all the key points and give final advice on how to proceed. 
Review all previous steps if needed and make sure you understood everything. 
Now you are on Step 4. 🎉 You have completed all instructions!""",
        "image": "AgACAgQAAxkBAAMTaNvObHAdLGwN7rBwFQW-IBeeBfoAAsDIMRsTEeFSJzWrRvZGr8cBAAMCAAN5AAM2BA"
    }
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send Step 1 as a photo + text."""
    await update.message.reply_photo(
        photo=steps[0]["image"],
        caption=steps[0]["text"],
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("➡️ Next", callback_data="1")]
        ])
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle Next and Restart buttons."""
    query = update.callback_query
    await query.answer()
    step = query.data

    if step == "restart":
        # Restart from Step 1
        await query.message.reply_photo(
            photo=steps[0]["image"],
            caption=steps[0]["text"],
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("➡️ Next", callback_data="1")]
            ])
        )
        return

    step_index = int(step)
    if step_index < len(steps):
        # Determine buttons for next step
        if step_index + 1 < len(steps):
            buttons = [
                [InlineKeyboardButton("➡️ Next", callback_data=str(step_index + 1))],
                [InlineKeyboardButton("🔄 Restart", callback_data="restart")]
            ]
        else:
            buttons = [[InlineKeyboardButton("🔄 Restart", callback_data="restart")]]

        await query.message.reply_photo(
            photo=steps[step_index]["image"],
            caption=steps[step_index]["text"],
            reply_markup=InlineKeyboardMarkup(buttons)
        )

def main():
    # Build application using Application.builder(), no Updater
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()

## this is test sample code 
##

##venv\Scripts\activate
