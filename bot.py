import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import os

# Replace 'YOUR_BOT_TOKEN' with your bot token
TOKEN = '7384913755:AAExvRY035Rrhdm4o8foa-ihktWAQ5SJPZY'

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Send me a file, and I will generate a download link!')

def handle_document(update: Update, context: CallbackContext) -> None:
    file = update.message.document.get_file()
    file_path = file.file_path
    file_id = update.message.document.file_id
    download_url = f'https://api.telegram.org/file/bot{TOKEN}/{file_path}'
    # Here, you should implement uploading to GitHub Pages or other hosting service.
    # For GitHub Pages, you'll need to set up a repository to serve the files.
    update.message.reply_text(f'File download link: {download_url}')

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.document, handle_document))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
